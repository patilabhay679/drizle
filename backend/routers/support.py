import uuid
import logging
from datetime import datetime, timezone
from fastapi import APIRouter, Request, HTTPException, status

import jwt
from config import AUTH_SECRET_KEY, ALGORITHM
from models import SupportTicketModel, PublicSupportTicketModel

logger = logging.getLogger("drizle")
router = APIRouter(tags=["support"])


@router.post("/api/v1/support/tickets/public")
async def create_ticket_public(body: PublicSupportTicketModel, request: Request):
    db = request.app.state.db
    doc = body.model_dump()
    doc["_id"] = f"st_{uuid.uuid4().hex[:12]}"
    doc["priority"] = "normal"
    doc["status"] = "open"
    doc["created_at"] = datetime.now(timezone.utc).isoformat()
    await db.support_tickets.insert_one(doc)
    logger.info("Public support ticket from %s", body.email)
    return {k: v for k, v in doc.items() if k != "_id"}


async def _merchant(request: Request) -> dict:
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    try:
        payload = jwt.decode(auth[7:], AUTH_SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        user = await request.app.state.db.users.find_one({"email": email})
        if not user:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


@router.post("/api/v1/support/tickets")
async def create_ticket(body: SupportTicketModel, request: Request):
    merchant = await _merchant(request)
    db = request.app.state.db
    doc = body.model_dump()
    doc["_id"] = f"st_{uuid.uuid4().hex[:12]}"
    doc["email"] = merchant["email"]
    doc["status"] = "open"
    doc["created_at"] = datetime.now(timezone.utc).isoformat()
    await db.support_tickets.insert_one(doc)
    return {k: v for k, v in doc.items() if k != "_id"}


@router.get("/api/v1/support/tickets")
async def list_tickets(request: Request):
    merchant = await _merchant(request)
    db = request.app.state.db
    cursor = db.support_tickets.find({"email": merchant["email"]}).sort("created_at", -1)
    tickets = await cursor.to_list(100)
    return [{k: v for k, v in t.items() if k != "_id"} for t in tickets]
