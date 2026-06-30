import re
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Request

from deps import get_current_merchant

router = APIRouter(tags=["transactions"])


@router.get("/api/v1/transactions")
async def get_transactions(
    request: Request,
    page: int = 1,
    limit: int = 20,
    scheme: str | None = None,
    txn_type: str | None = None,
    search: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
    merchant: dict = Depends(get_current_merchant),
):
    db = request.app.state.db
    query: dict = {"email": merchant["email"]}
    if scheme:
        query["scheme"] = scheme
    if txn_type:
        query["type"] = txn_type
    if start_date or end_date:
        date_filter = {}
        if start_date:
            date_filter["$gte"] = datetime.fromisoformat(start_date).replace(tzinfo=timezone.utc).isoformat()
        if end_date:
            date_filter["$lte"] = datetime.fromisoformat(end_date).replace(tzinfo=timezone.utc).isoformat()
        query["created_at"] = date_filter
    if search:
        escaped = re.escape(search)
        query["$or"] = [
            {"reference": {"$regex": escaped, "$options": "i"}},
            {"id": {"$regex": escaped, "$options": "i"}},
        ]
    cursor = db.transactions.find(query).sort("created_at", -1).skip((page - 1) * limit).limit(limit)
    data = await cursor.to_list(length=limit)
    total = await db.transactions.count_documents(query)
    clean = [{k: v for k, v in doc.items() if k != "_id"} for doc in data]
    return {"data": clean, "total": total, "page": page, "limit": limit}
