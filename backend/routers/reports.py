from fastapi import APIRouter, Depends, Request

from deps import get_current_merchant

router = APIRouter(tags=["reports"])


@router.get("/api/v1/reports/tax-invoices")
async def list_tax_invoices(
    request: Request,
    page: int = 1,
    limit: int = 20,
    merchant: dict = Depends(get_current_merchant),
):
    db = request.app.state.db
    query = {"email": merchant["email"]}
    cursor = db.tax_invoices.find(query).sort("period", -1).skip((page - 1) * limit).limit(limit)
    data = await cursor.to_list(length=limit)
    total = await db.tax_invoices.count_documents(query)
    clean = [{k: v for k, v in doc.items() if k != "_id"} for doc in data]
    return {"data": clean, "total": total, "page": page, "limit": limit}


@router.get("/api/v1/reports/monthly-statements")
async def list_monthly_statements(
    request: Request,
    page: int = 1,
    limit: int = 20,
    merchant: dict = Depends(get_current_merchant),
):
    db = request.app.state.db
    query = {"email": merchant["email"]}
    cursor = db.monthly_statements.find(query).sort("period", -1).skip((page - 1) * limit).limit(limit)
    data = await cursor.to_list(length=limit)
    total = await db.monthly_statements.count_documents(query)
    clean = [{k: v for k, v in doc.items() if k != "_id"} for doc in data]
    return {"data": clean, "total": total, "page": page, "limit": limit}
