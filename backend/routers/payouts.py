from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Request

from deps import get_current_merchant

router = APIRouter(tags=["payouts"])


@router.get("/api/v1/payouts")
async def get_payouts(
    request: Request,
    page: int = 1,
    limit: int = 20,
    status_filter: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
    search: str | None = None,
    merchant: dict = Depends(get_current_merchant),
):
    db = request.app.state.db
    query: dict = {"email": merchant["email"]}
    if status_filter:
        query["status"] = status_filter
    if start_date or end_date:
        date_filter = {}
        if start_date:
            date_filter["$gte"] = datetime.fromisoformat(start_date).replace(tzinfo=timezone.utc).isoformat()
        if end_date:
            date_filter["$lte"] = datetime.fromisoformat(end_date).replace(tzinfo=timezone.utc).isoformat()
        query["created_at"] = date_filter
    if search:
        query["reference"] = {"$regex": search, "$options": "i"}
    cursor = db.payouts.find(query).sort("created_at", -1).skip((page - 1) * limit).limit(limit)
    data = await cursor.to_list(length=limit)
    total = await db.payouts.count_documents(query)
    clean = [{k: v for k, v in doc.items() if k != "_id"} for doc in data]
    return {"data": clean, "total": total, "page": page, "limit": limit}
