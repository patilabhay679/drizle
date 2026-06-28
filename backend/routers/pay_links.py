import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Request

from models import CreatePayLinkModel
from deps import get_current_merchant

router = APIRouter(tags=["pay_links"])


@router.post("/api/v1/pay-links")
async def create_pay_link(body: CreatePayLinkModel, request: Request, merchant: dict = Depends(get_current_merchant)):
    db = request.app.state.db
    link = {
        "id": f"dpl_{uuid.uuid4().hex[:12]}",
        "email": merchant["email"],
        "url": f"https://drizlepay.com/pay/{uuid.uuid4().hex[:16]}",
        "amount": body.amount,
        "currency": body.currency,
        "description": body.description or "",
        "is_static": body.is_static,
        "is_recurring": body.is_recurring,
        "recurring_interval": body.recurring_interval,
        "status": "active",
        "payment_count": 0,
        "total_collected": 0,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    await db.pay_links.insert_one(link)
    link.pop("_id", None)
    return link


@router.get("/api/v1/pay-links")
async def list_pay_links(
    request: Request,
    page: int = 1,
    limit: int = 20,
    is_static: bool | None = None,
    is_recurring: bool | None = None,
    merchant: dict = Depends(get_current_merchant),
):
    db = request.app.state.db
    query: dict = {"email": merchant["email"]}
    if is_static is not None:
        query["is_static"] = is_static
    if is_recurring is not None:
        query["is_recurring"] = is_recurring
    cursor = db.pay_links.find(query).sort("created_at", -1).skip((page - 1) * limit).limit(limit)
    data = await cursor.to_list(length=limit)
    total = await db.pay_links.count_documents(query)
    clean = [{k: v for k, v in doc.items() if k != "_id"} for doc in data]
    return {"data": clean, "total": total, "page": page, "limit": limit}


@router.get("/api/v1/pay-links/stats")
async def pay_link_stats(request: Request, merchant: dict = Depends(get_current_merchant)):
    db = request.app.state.db
    pipeline = [
        {"$match": {"email": merchant["email"]}},
        {"$group": {
            "_id": None,
            "total_links": {"$sum": 1},
            "active_links": {"$sum": {"$cond": [{"$eq": ["$status", "active"]}, 1, 0]}},
            "total_collected": {"$sum": "$total_collected"},
            "total_payments": {"$sum": "$payment_count"},
        }},
    ]
    cursor = await db.pay_links.aggregate(pipeline)
    result = await cursor.to_list(1)
    stats = result[0] if result else {"total_links": 0, "active_links": 0, "total_collected": 0, "total_payments": 0}
    stats.pop("_id", None)
    return stats
