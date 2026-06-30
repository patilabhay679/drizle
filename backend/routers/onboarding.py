import uuid
import logging
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, Depends, status, Request, UploadFile, File, Form
from faker import Faker

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_CONTENT_TYPES = {
    "image/png",
    "image/jpeg",
    "image/jpg",
    "application/pdf",
}

from models import (
    OnboardingSaveModel,
    OnboardingBusinessType,
    OnboardingBusinessDetails,
    OnboardingRepresentative,
    OnboardingOwner,
    OnboardingExecutive,
    OnboardingProducts,
    OnboardingPublic,
    OnboardingBank,
    OnboardingSecurity,
    OnboardingExtras,
)
from deps import get_current_merchant
from pydantic import ValidationError

logger = logging.getLogger("drizle")
fake = Faker()
router = APIRouter(prefix="/api/v1/onboarding", tags=["onboarding"])


DOC_TYPES = {
    "trade_license",
    "passport_emirates_id",
    "bank_letter",
    "vat_certificate",
    "company_registration",
}

SECTION_MODELS = {
    "business_type": OnboardingBusinessType,
    "business_details": OnboardingBusinessDetails,
    "representative": OnboardingRepresentative,
    "owners": OnboardingOwner,
    "executives": OnboardingExecutive,
    "products": OnboardingProducts,
    "public": OnboardingPublic,
    "bank": OnboardingBank,
    "security": OnboardingSecurity,
    "extras": OnboardingExtras,
}


@router.get("/data")
async def get_onboarding_data(merchant: dict = Depends(get_current_merchant)):
    data = merchant.get("onboarding_data") or {}
    return {
        "onboarding_status": merchant.get("onboarding_status", "not_started"),
        "kyc_documents": merchant.get("kyc_documents", []),
        "data": data,
    }


@router.put("/data")
async def save_onboarding_data(
    body: OnboardingSaveModel,
    request: Request,
    merchant: dict = Depends(get_current_merchant),
):
    db = request.app.state.db
    field_map = {
        "business_type": "onboarding_data.business_type",
        "business_details": "onboarding_data.business_details",
        "representative": "onboarding_data.representative",
        "owners": "onboarding_data.owners",
        "executives": "onboarding_data.executives",
        "products": "onboarding_data.products",
        "public": "onboarding_data.public",
        "bank": "onboarding_data.bank",
        "security": "onboarding_data.security",
        "extras": "onboarding_data.extras",
    }
    key = field_map.get(body.section)
    if not key:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f"Unknown section: {body.section}")

    model_cls = SECTION_MODELS.get(body.section)
    if model_cls:
        try:
            if body.section in ("owners", "executives"):
                if not isinstance(body.data, list):
                    raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f"{body.section} must be an array")
                for item in body.data:
                    model_cls(**item)
            else:
                model_cls(**body.data)
        except ValidationError as e:
            raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.errors(include_context=False))

    await db.users.update_one(
        {"email": merchant["email"]},
        {"$set": {key: body.data}},
    )

    if merchant.get("onboarding_status") == "not_started":
        await db.users.update_one(
            {"email": merchant["email"]},
            {"$set": {"onboarding_status": "in_progress"}},
        )

    updated = await db.users.find_one({"email": merchant["email"]})
    return {
        "ok": True,
        "onboarding_status": updated.get("onboarding_status", "in_progress"),
    }


@router.post("/upload-document")
async def upload_document(
    request: Request,
    doc_type: str = Form(...),
    file: UploadFile = File(...),
    merchant: dict = Depends(get_current_merchant),
):
    if doc_type not in DOC_TYPES:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid doc_type. Must be one of: {', '.join(sorted(DOC_TYPES))}",
        )

    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file type '{file.content_type}'. Allowed: PNG, JPEG, PDF",
        )

    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail=f"File too large ({len(contents)} bytes). Maximum allowed: 10 MB",
        )
    await file.seek(0)

    db = request.app.state.db
    doc_id = f"kyc_{uuid.uuid4().hex[:12]}"
    doc = {
        "id": doc_id,
        "doc_type": doc_type,
        "filename": file.filename,
        "content_type": file.content_type,
        "uploaded_at": datetime.now(timezone.utc).isoformat(),
        "status": "processed",
    }

    await db.users.update_one(
        {"email": merchant["email"]},
        {"$push": {"kyc_documents": doc}},
    )

    ocr_sections = _ocr_for_doc_type(doc_type)

    # Merge each section individually so earlier uploads aren't wiped
    update = {}
    for section, section_data in ocr_sections.items():
        update[f"onboarding_data.{section}"] = section_data
    await db.users.update_one({"email": merchant["email"]}, {"$set": update})

    if merchant.get("onboarding_status") == "not_started":
        await db.users.update_one(
            {"email": merchant["email"]},
            {"$set": {"onboarding_status": "in_progress"}},
        )

    updated = await db.users.find_one({"email": merchant["email"]})
    return {
        "ok": True,
        "document": doc,
        "populated_sections": list(ocr_sections.keys()),
        "onboarding_status": updated.get("onboarding_status", "in_progress"),
    }


@router.post("/submit")
async def submit_onboarding(
    request: Request,
    merchant: dict = Depends(get_current_merchant),
):
    db = request.app.state.db
    data = merchant.get("onboarding_data") or {}

    required_sections = [
        "business_type", "business_details", "representative",
        "owners", "executives", "products", "public", "bank",
    ]
    missing = []
    for s in required_sections:
        section_data = data.get(s, {})
        if isinstance(section_data, dict) and not any(v for v in section_data.values()):
            missing.append(s)
        elif isinstance(section_data, list) and len(section_data) == 0:
            missing.append(s)

    if missing:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail=f"Complete these sections before submitting: {', '.join(missing)}",
        )

    await db.users.update_one(
        {"email": merchant["email"]},
        {"$set": {"onboarding_status": "submitted"}},
    )
    return {"ok": True, "onboarding_status": "submitted"}


# ─── Mock OCR generators ───

def _phone():
    return f"+9715{fake.msisdn()[3:11]}"


def _ocr_for_doc_type(doc_type: str) -> dict:
    """Return only the relevant onboarding sections for a given document type."""
    dispatch = {
        "trade_license": _ocr_trade_license,
        "passport_emirates_id": _ocr_passport_or_id,
        "bank_letter": _ocr_bank_letter,
        "vat_certificate": _ocr_vat_certificate,
        "company_registration": _ocr_company_registration,
    }
    fn = dispatch.get(doc_type)
    return fn() if fn else {}


def _ocr_trade_license():
    phone = _phone()
    return {
        "business_type": {
            "type": fake.random_element(["sole_proprietorship", "llc", "corporation", "partnership"]),
            "subtype": fake.random_element(["ecommerce", "saas", "retail", "fintech", "consulting"]),
        },
        "business_details": {
            "legal_name": fake.company(),
            "trading_name": fake.company(),
            "registration_number": f"CR-{fake.bothify(text='########')}",
            "tax_id": "",
            "emirates_id": "",
            "website": fake.url(),
            "phone": phone,
            "address": fake.address().replace("\n", ", "),
            "city": fake.random_element(["Dubai", "Abu Dhabi", "Sharjah", "Riyadh", "Doha"]),
            "country": "UAE",
        },
        "public": {
            "public_name": fake.company(),
            "support_email": fake.email(),
            "support_phone": phone,
            "support_url": fake.url(),
            "terms_url": fake.url() + "/terms",
            "privacy_url": fake.url() + "/privacy",
        },
    }


def _ocr_passport_or_id():
    phone = _phone()
    return {
        "representative": {
            "name": fake.name(),
            "email": fake.email(),
            "phone": phone,
            "job_title": fake.random_element(["CEO", "CFO", "Founder", "Managing Director", "Owner"]),
        },
        "owners": [
            {
                "name": fake.name(),
                "email": fake.email(),
                "phone": _phone(),
                "nationality": "UAE",
                "ownership_pct": round(fake.random_element([100, 51, 75, 100, 100]), 0),
            }
        ],
        "executives": [
            {
                "name": fake.name(),
                "email": fake.email(),
                "job_title": fake.random_element(["CEO", "CTO", "COO", "CFO"]),
                "nationality": "UAE",
            }
        ],
    }


def _ocr_bank_letter():
    return {
        "bank": {
            "bank_name": fake.random_element(["Emirates NBD", "ADCB", "Mashreq", "FAB", "Dubai Islamic Bank"]),
            "account_name": fake.company(),
            "account_number": fake.bothify(text="##########").ljust(8, "0")[:16],
            "iban": f"AE{fake.bothify(text='#####################')}"[:23],
            "swift": fake.bothify(text="EBILAEADXXX")[:11],
        },
    }


def _ocr_vat_certificate():
    return {
        "business_details": {
            "legal_name": "",
            "trading_name": "",
            "registration_number": "",
            "tax_id": fake.bothify(text="#############").ljust(15, "0")[:15],
            "emirates_id": "",
            "website": "",
            "phone": "",
            "address": "",
            "city": "",
            "country": "",
        },
    }


def _ocr_company_registration():
    return {
        "business_details": {
            "legal_name": fake.company(),
            "trading_name": fake.company(),
            "registration_number": f"CR-{fake.bothify(text='########')}",
            "tax_id": "",
            "emirates_id": f"784-{fake.bothify(text='########?')}"[:8] + f"-{fake.bothify(text='#######')}",
            "website": "",
            "phone": "",
            "address": fake.address().replace("\n", ", "),
            "city": fake.random_element(["Dubai", "Abu Dhabi", "Sharjah"]),
            "country": "UAE",
        },
        "business_type": {
            "type": "",
            "subtype": "",
        },
    }
