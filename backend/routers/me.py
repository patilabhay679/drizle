from fastapi import APIRouter, HTTPException, Depends, status, Request

from models import UpdateProfileModel
from deps import get_current_merchant, merchant_safe

router = APIRouter(tags=["me"])


@router.get("/api/v1/me")
async def get_me(merchant: dict = Depends(get_current_merchant)):
    return merchant_safe(merchant)


@router.put("/api/v1/me")
async def update_me(body: UpdateProfileModel, request: Request, merchant: dict = Depends(get_current_merchant)):
    db = request.app.state.db
    updates = {}
    if body.name is not None:
        updates["name"] = body.name
    if body.company is not None:
        updates["company"] = body.company
    if updates:
        await db.users.update_one({"email": merchant["email"]}, {"$set": updates})
    updated = await db.users.find_one({"email": merchant["email"]})
    return merchant_safe(updated)


@router.get("/api/v1/me/api-keys")
async def get_api_keys(merchant: dict = Depends(get_current_merchant)):
    return merchant.get("api_keys", {
        "publishable": "dp_pub_demo_sample_key",
        "secret": "dp_sec_••••••••••••••••••••••",
    })
