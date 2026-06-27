import os
import json
import uuid
import logging
from datetime import datetime, timedelta, timezone
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr
import jwt
import bcrypt

from pymongo import AsyncMongoClient
from pymongo.errors import DuplicateKeyError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("drizle")

AUTH_SECRET_KEY = os.environ.get("AUTH_SECRET_KEY", "drizle-dev-secret-change-in-prod")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

# ---------------------------------------------------------------------------
# MongoDB
# ---------------------------------------------------------------------------

def _load_mongo_uri() -> str:
    uri = os.environ.get("MONGODB_URI")
    if uri:
        return uri
    settings_path = os.path.join(os.path.dirname(__file__), "settings.json")
    try:
        with open(settings_path) as f:
            cfg = json.load(f)
        return cfg["MONGODB_URI"]
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        pass
    raise RuntimeError("MONGODB_URI not configured — set env var or add to settings.json")

MONGO_URI = _load_mongo_uri()
DB_NAME = "drizle"

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.mongo = AsyncMongoClient(MONGO_URI)
    app.state.db = app.state.mongo[DB_NAME]
    await app.state.db.users.create_index("email", unique=True)
    logger.info("Connected to MongoDB Atlas")
    await _seed()
    yield
    await app.state.mongo.close()
    logger.info("Disconnected from MongoDB")

app = FastAPI(title="Drizle Payments API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:4173",
        "https://drizlepay.com",
        "https://www.drizlepay.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer(auto_error=False)

# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

class UserModel(BaseModel):
    email: str
    password: str
    name: str
    company: str | None = None

class LoginModel(BaseModel):
    email: str
    password: str

class UpdateProfileModel(BaseModel):
    name: str | None = None
    company: str | None = None

class ChangePasswordModel(BaseModel):
    current_password: str
    new_password: str

class ForgotPasswordModel(BaseModel):
    email: str

class ResetPasswordModel(BaseModel):
    token: str
    new_password: str

class ContactModel(BaseModel):
    name: str
    email: str
    company: str | None = None
    phone: str | None = None
    message: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    merchant: dict

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _serialize(doc: dict) -> dict:
    """Convert MongoDB doc to JSON-safe dict."""
    return {k: v for k, v in doc.items() if k != '_id'}

def create_access_token(data: dict):
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode({**data, "exp": expire}, AUTH_SECRET_KEY, algorithm=ALGORITHM)

async def get_current_merchant(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    try:
        payload = jwt.decode(credentials.credentials, AUTH_SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        user = await app.state.db.users.find_one({"email": email})
        if not user:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def _merchant_safe(user: dict) -> dict:
    return {
        "email": user["email"],
        "name": user["name"],
        "company": user.get("company", ""),
        "email_verified": user.get("email_verified", False),
    }

def _db():
    return app.state.db

# ---------------------------------------------------------------------------
# Auth routes
# ---------------------------------------------------------------------------

@app.post("/api/v1/auth/register")
async def register(body: UserModel):
    db = _db()
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
        "api_keys": {
            "publishable": f"dp_pub_{uuid.uuid4().hex[:16]}",
            "secret": f"dp_sec_{uuid.uuid4().hex[:32]}",
        },
    }
    await db.users.insert_one(user)
    token = create_access_token({"sub": body.email})
    logger.info("Verification link (dev): /verify-email?token=%s", verify_token)
    return TokenResponse(access_token=token, merchant=_merchant_safe(user))

@app.post("/api/v1/auth/login")
async def login(body: LoginModel):
    db = _db()
    user = await db.users.find_one({"email": body.email})
    if not user or not bcrypt.checkpw(body.password.encode(), user["password"].encode()):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    token = create_access_token({"sub": body.email})
    return TokenResponse(access_token=token, merchant=_merchant_safe(user))

@app.post("/api/v1/auth/verify-email")
async def verify_email(token: str):
    db = _db()
    result = await db.users.find_one_and_update(
        {"verify_token": token},
        {"$set": {"email_verified": True}, "$unset": {"verify_token": ""}},
    )
    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Invalid or expired verification token")
    return {"verified": True, "email": result["email"]}

@app.post("/api/v1/auth/forgot-password")
async def forgot_password(body: ForgotPasswordModel):
    db = _db()
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

@app.post("/api/v1/auth/reset-password")
async def reset_password(body: ResetPasswordModel):
    db = _db()
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

@app.get("/api/v1/me")
async def get_me(merchant: dict = Depends(get_current_merchant)):
    return _merchant_safe(merchant)

@app.put("/api/v1/me")
async def update_me(body: UpdateProfileModel, merchant: dict = Depends(get_current_merchant)):
    db = _db()
    updates = {}
    if body.name is not None:
        updates["name"] = body.name
    if body.company is not None:
        updates["company"] = body.company
    if updates:
        await db.users.update_one({"email": merchant["email"]}, {"$set": updates})
    updated = await db.users.find_one({"email": merchant["email"]})
    return _merchant_safe(updated)

@app.put("/api/v1/auth/change-password")
async def change_password(body: ChangePasswordModel, merchant: dict = Depends(get_current_merchant)):
    db = _db()
    if not bcrypt.checkpw(body.current_password.encode(), merchant["password"].encode()):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Current password is incorrect")
    new_hash = bcrypt.hashpw(body.new_password.encode(), bcrypt.gensalt()).decode()
    await db.users.update_one({"email": merchant["email"]}, {"$set": {"password": new_hash}})
    return {"ok": True}

@app.post("/api/v1/auth/rotate-api-keys")
async def rotate_api_keys(merchant: dict = Depends(get_current_merchant)):
    db = _db()
    keys = {
        "publishable": f"dp_pub_{uuid.uuid4().hex[:16]}",
        "secret": f"dp_sec_{uuid.uuid4().hex[:32]}",
    }
    await db.users.update_one({"email": merchant["email"]}, {"$set": {"api_keys": keys}})
    return keys

@app.get("/api/v1/me/api-keys")
async def get_api_keys(merchant: dict = Depends(get_current_merchant)):
    return merchant.get("api_keys", {
        "publishable": "dp_pub_demo_sample_key",
        "secret": "dp_sec_••••••••••••••••••••••",
    })

@app.post("/api/v1/contact")
async def contact(body: ContactModel):
    db = _db()
    doc = body.model_dump()
    doc["created_at"] = datetime.now(timezone.utc).isoformat()
    await db.contact_submissions.insert_one(doc)
    logger.info("Contact form submission from %s", body.email)
    return {"ok": True}

# ---------------------------------------------------------------------------
# Merchant data routes
# ---------------------------------------------------------------------------

@app.get("/api/v1/transactions")
async def get_transactions(
    page: int = 1, limit: int = 20, merchant: dict = Depends(get_current_merchant)
):
    db = _db()
    cursor = db.transactions.find({"email": merchant["email"]}).sort("created_at", -1).skip((page - 1) * limit).limit(limit)
    data = await cursor.to_list(length=limit)
    total = await db.transactions.count_documents({"email": merchant["email"]})
    return {"data": data, "total": total, "page": page, "limit": limit}

@app.get("/api/v1/payouts")
async def get_payouts(
    page: int = 1, limit: int = 20, merchant: dict = Depends(get_current_merchant)
):
    db = _db()
    cursor = db.payouts.find({"email": merchant["email"]}).sort("created_at", -1).skip((page - 1) * limit).limit(limit)
    data = await cursor.to_list(length=limit)
    total = await db.payouts.count_documents({"email": merchant["email"]})
    return {"data": data, "total": total, "page": page, "limit": limit}

# ---------------------------------------------------------------------------
# Seed demo data
# ---------------------------------------------------------------------------

async def _seed():
    db = _db()
    demo_email = "demo@drizlepay.com"
    existing = await db.users.find_one({"email": demo_email})
    if not existing:
        await db.users.insert_one({
            "email": demo_email,
            "password": bcrypt.hashpw("demo123".encode(), bcrypt.gensalt()).decode(),
            "name": "Demo Merchant",
            "company": "Demo SaaS Ltd",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "email_verified": True,
            "api_keys": {
                "publishable": "dp_pub_demo_sample_key",
                "secret": "dp_sec_demo_secret_key_replace_in_prod",
            },
        })
        txns = []
        for i in range(25):
            txns.append({
                "email": demo_email,
                "id": f"dp_tx_{i:04d}",
                "amount": round(50 + (i * 13.7), 2),
                "currency": "AED",
                "status": "success" if i % 5 != 0 else "refunded",
                "method": ["card", "tabby", "apple_pay", "google_pay", "aani"][i % 5],
                "customer": f"cust_{i:04d}@example.com",
                "created_at": (datetime.now(timezone.utc) - timedelta(hours=i * 3)).isoformat(),
            })
        if txns:
            await db.transactions.insert_many(txns)
        ps = []
        for i in range(8):
            ps.append({
                "email": demo_email,
                "id": f"po_{i:04d}",
                "amount": round(2500 + (i * 1200), 2),
                "currency": "AED",
                "status": "paid" if i < 5 else "pending",
                "period": "June 2026",
                "paid_at": (datetime.now(timezone.utc) - timedelta(days=i * 4)).isoformat() if i < 5 else None,
            })
        if ps:
            await db.payouts.insert_many(ps)
        logger.info("Seeded demo merchant: %s", demo_email)


# ---------------------------------------------------------------------------
# SPA catch-all
# ---------------------------------------------------------------------------

@app.api_route("/{catchall:path}", methods=["GET", "HEAD"])
async def serve_spa(catchall: str):
    frontend_dir = "build"
    file_path = os.path.join(frontend_dir, catchall)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    if os.path.isdir(file_path):
        index_path = os.path.join(file_path, "index.html")
        if os.path.isfile(index_path):
            return FileResponse(index_path)
    html_path = file_path.rstrip("/") + ".html"
    if os.path.isfile(html_path):
        return FileResponse(html_path)
    return FileResponse(os.path.join(frontend_dir, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
