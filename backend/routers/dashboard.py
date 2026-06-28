from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, Request

from deps import get_current_merchant

router = APIRouter(tags=["dashboard"])


@router.get("/api/v1/dashboard/metrics")
async def dashboard_metrics(
    request: Request,
    start_date: str | None = None,
    end_date: str | None = None,
    merchant: dict = Depends(get_current_merchant),
):
    db = request.app.state.db
    email = merchant["email"]
    now = datetime.now(timezone.utc)

    if end_date:
        end = datetime.fromisoformat(end_date)
    else:
        end = now
    if start_date:
        start = datetime.fromisoformat(start_date)
    else:
        start = end - timedelta(days=30)

    period_start = start.isoformat()
    period_end = end.isoformat()
    prev_end = start
    prev_start = prev_end - (end - start)

    pipeline_current = [
        {"$match": {"email": email, "status": "success", "created_at": {"$gte": period_start, "$lte": period_end}}},
        {"$group": {
            "_id": None,
            "total_amount": {"$sum": "$amount"},
            "count": {"$sum": 1},
            "avg_amount": {"$avg": "$amount"},
        }},
    ]
    pipeline_prev = [
        {"$match": {"email": email, "status": "success", "created_at": {"$gte": prev_start.isoformat(), "$lte": prev_end.isoformat()}}},
        {"$group": {
            "_id": None,
            "total_amount": {"$sum": "$amount"},
            "count": {"$sum": 1},
        }},
    ]

    cursor_current = await db.transactions.aggregate(pipeline_current)
    cur = await cursor_current.to_list(1)
    cursor_prev = await db.transactions.aggregate(pipeline_prev)
    prev = await cursor_prev.to_list(1)

    cur_data = cur[0] if cur else {"total_amount": 0, "count": 0, "avg_amount": 0}
    prev_data = prev[0] if prev else {"total_amount": 0, "count": 0}

    def pct_change(cur_val, prev_val):
        if prev_val == 0:
            return 0
        return round(((cur_val - prev_val) / prev_val) * 100, 2)

    return {
        "transaction_amount": {"value": round(cur_data["total_amount"], 2), "change": pct_change(cur_data["total_amount"], prev_data["total_amount"]), "currency": "AED"},
        "transaction_count": {"value": cur_data["count"], "change": pct_change(cur_data["count"], prev_data["count"])},
        "average_transaction": {"value": round(cur_data["avg_amount"], 2), "change": pct_change(cur_data["avg_amount"], prev_data["total_amount"] / max(prev_data["count"], 1)), "currency": "AED"},
    }


@router.get("/api/v1/dashboard/charts")
async def dashboard_charts(
    request: Request,
    start_date: str | None = None,
    end_date: str | None = None,
    merchant: dict = Depends(get_current_merchant),
):
    db = request.app.state.db
    email = merchant["email"]
    now = datetime.now(timezone.utc)

    if end_date:
        end = datetime.fromisoformat(end_date)
    else:
        end = now
    if start_date:
        start = datetime.fromisoformat(start_date)
    else:
        start = end - timedelta(days=30)

    period_start = start.isoformat()
    period_end = end.isoformat()

    pipeline = [
        {"$match": {"email": email, "status": "success", "created_at": {"$gte": period_start, "$lte": period_end}}},
        {"$group": {
            "_id": {"$dateToString": {"format": "%Y-%m-%d", "date": {"$dateFromString": {"dateString": "$created_at"}}}},
            "volume": {"$sum": "$amount"},
            "count": {"$sum": 1},
        }},
        {"$sort": {"_id": 1}},
    ]
    cursor = await db.transactions.aggregate(pipeline)
    volume_data = await cursor.to_list(100)
    volume = [{"date": v["_id"], "volume": round(v["volume"], 2), "count": v["count"]} for v in volume_data]

    scheme_pipeline = [
        {"$match": {"email": email, "created_at": {"$gte": period_start, "$lte": period_end}}},
        {"$group": {"_id": "$scheme", "volume": {"$sum": "$amount"}, "count": {"$sum": 1}}},
        {"$sort": {"volume": -1}},
        {"$limit": 5},
    ]
    scheme_cursor = await db.transactions.aggregate(scheme_pipeline)
    scheme_data = await scheme_cursor.to_list(5)
    schemes = [{"name": s["_id"], "volume": round(s["volume"], 2), "count": s["count"]} for s in scheme_data]

    return {"volume_over_time": volume, "top_schemes": schemes}


@router.get("/api/v1/payouts/recent")
async def recent_payouts(
    request: Request,
    limit: int = 5,
    merchant: dict = Depends(get_current_merchant),
):
    db = request.app.state.db
    cursor = db.payouts.find({"email": merchant["email"]}).sort("created_at", -1).limit(limit)
    data = await cursor.to_list(length=limit)
    return [{
        "id": p["id"],
        "amount": p["amount"],
        "currency": p.get("currency", "AED"),
        "date": p.get("paid_at") or p.get("created_at"),
        "status": p.get("status", "pending"),
        "net_amount": p.get("net_amount", p["amount"]),
        "tx_count": p.get("tx_count", 0),
        "iban": p.get("iban", "AE770260001014273931915"),
    } for p in data]
