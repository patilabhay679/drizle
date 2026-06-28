import uuid
import logging
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Request

from models import InviteUserModel
from deps import get_current_merchant

logger = logging.getLogger("drizle")
router = APIRouter(tags=["team"])


@router.get("/api/v1/team")
async def list_team(request: Request, merchant: dict = Depends(get_current_merchant)):
    db = request.app.state.db
    cursor = db.team_members.find({"merchant_email": merchant["email"]}).sort("created_at", -1)
    data = await cursor.to_list(100)
    return [{
        "id": m.get("id"), "email": m["email"], "name": m.get("name", ""),
        "role": m.get("role", "member"), "status": m.get("status", "active"),
        "created_at": m.get("created_at"),
    } for m in data]


@router.post("/api/v1/team/invite")
async def invite_team_member(body: InviteUserModel, request: Request, merchant: dict = Depends(get_current_merchant)):
    db = request.app.state.db
    member_id = f"tm_{uuid.uuid4().hex[:12]}"
    member = {
        "id": member_id,
        "merchant_email": merchant["email"],
        "email": body.email,
        "name": "",
        "role": body.role,
        "status": "invited",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    await db.team_members.insert_one(member)
    member.pop("_id", None)
    logger.info("Invited team member: %s (%s)", body.email, body.role)
    return member


@router.delete("/api/v1/team/{member_id}")
async def remove_team_member(member_id: str, request: Request, merchant: dict = Depends(get_current_merchant)):
    db = request.app.state.db
    await db.team_members.delete_one({"id": member_id, "merchant_email": merchant["email"]})
    return {"ok": True}
