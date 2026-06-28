import logging
from datetime import datetime, timezone

from fastapi import APIRouter, Request

from models import ContactModel

logger = logging.getLogger("drizle")
router = APIRouter(tags=["contact"])


@router.post("/api/v1/contact")
async def contact(body: ContactModel, request: Request):
    db = request.app.state.db
    doc = body.model_dump()
    doc["created_at"] = datetime.now(timezone.utc).isoformat()
    await db.contact_submissions.insert_one(doc)
    logger.info("Contact form submission from %s", body.email)
    return {"ok": True}
