import uuid
import logging
from datetime import datetime, timedelta, timezone

import bcrypt
from fastapi import APIRouter, HTTPException, Depends, status, Request

from models import UserModel, LoginModel, ForgotPasswordModel, ResetPasswordModel, ChangePasswordModel, TokenResponse
from deps import create_access_token, get_current_merchant, merchant_safe

logger = logging.getLogger("drizle")
router = APIRouter(prefix="/api/v1/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse)
async def register(body: UserModel, request: Request):
    db = request.app.state.db
    existing = await db.users.find_one({"email": body.email})
    if existing:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Email already registered")
    verify_token = uuid.uuid4().hex
    user = {
        "email": body.email,
        "password": bcrypt.hashpw(body.password.encode(), bcrypt.gensalt()).decode(),
        "name": body.name,
        "company": body.company or "",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "email_verified": False,
        "verify_token": verify_token,
        "active": False,
        "onboarding_status": "not_started",
        "onboarding_data": {},
        "kyc_documents": [],
        "test_mode": False,
        "api_keys": {
            "publishable": f"dp_pub_{uuid.uuid4().hex[:16]}",
            "secret": f"dp_sec_{uuid.uuid4().hex[:32]}",
        },
    }
    await db.users.insert_one(user)
    token = create_access_token({"sub": body.email})
    logger.info("Verification link (dev): /verify-email?token=%s", verify_token)
    return TokenResponse(access_token=token, merchant=merchant_safe(user))


@router.post("/login", response_model=TokenResponse)
async def login(body: LoginModel, request: Request):
    db = request.app.state.db
    user = await db.users.find_one({"email": body.email})
    if not user or not bcrypt.checkpw(body.password.encode(), user["password"].encode()):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    token = create_access_token({"sub": body.email})
    return TokenResponse(access_token=token, merchant=merchant_safe(user))


@router.post("/verify-email")
async def verify_email(token: str, request: Request):
    db = request.app.state.db
    result = await db.users.find_one_and_update(
        {"verify_token": token},
        {"$set": {"email_verified": True}, "$unset": {"verify_token": ""}},
    )
    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Invalid or expired verification token")
    return {"verified": True, "email": result["email"]}


@router.post("/forgot-password")
async def forgot_password(body: ForgotPasswordModel, request: Request):
    db = request.app.state.db
    user = await db.users.find_one({"email": body.email})
    if user:
        reset_token = uuid.uuid4().hex
        expires = datetime.now(timezone.utc) + timedelta(hours=1)
        await db.users.update_one(
            {"email": body.email},
            {"$set": {"reset_token": reset_token, "reset_expires": expires.isoformat()}},
        )
        logger.info("Password reset link (dev): /reset-password?token=%s", reset_token)
    return {"ok": True}


@router.post("/reset-password")
async def reset_password(body: ResetPasswordModel, request: Request):
    db = request.app.state.db
    user = await db.users.find_one({"reset_token": body.token})
    if not user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Invalid or expired reset token")
    expires = datetime.fromisoformat(user["reset_expires"])
    if datetime.now(timezone.utc) > expires:
        await db.users.update_one({"_id": user["_id"]}, {"$unset": {"reset_token": "", "reset_expires": ""}})
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Token expired")
    new_hash = bcrypt.hashpw(body.new_password.encode(), bcrypt.gensalt()).decode()
    await db.users.update_one(
        {"_id": user["_id"]},
        {"$set": {"password": new_hash}, "$unset": {"reset_token": "", "reset_expires": ""}},
    )
    return {"ok": True}


@router.put("/change-password")
async def change_password(body: ChangePasswordModel, request: Request, merchant: dict = Depends(get_current_merchant)):
    if not bcrypt.checkpw(body.current_password.encode(), merchant["password"].encode()):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Current password is incorrect")
    new_hash = bcrypt.hashpw(body.new_password.encode(), bcrypt.gensalt()).decode()
    await request.app.state.db.users.update_one({"email": merchant["email"]}, {"$set": {"password": new_hash}})
    return {"ok": True}


@router.post("/rotate-api-keys")
async def rotate_api_keys(request: Request, merchant: dict = Depends(get_current_merchant)):
    keys = {
        "publishable": f"dp_pub_{uuid.uuid4().hex[:16]}",
        "secret": f"dp_sec_{uuid.uuid4().hex[:32]}",
    }
    await request.app.state.db.users.update_one({"email": merchant["email"]}, {"$set": {"api_keys": keys}})
    return keys
