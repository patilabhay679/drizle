import os
import logging

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

from database import lifespan

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("drizle")

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


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled error: %s", exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.get("/api/v1/health")
async def health():
    return {
        "status": "ok",
        "system":"busy"
        }


from routers.auth import router as auth_router
from routers.me import router as me_router
from routers.contact import router as contact_router
from routers.dashboard import router as dashboard_router
from routers.transactions import router as transactions_router
from routers.payouts import router as payouts_router
from routers.pay_links import router as pay_links_router
from routers.team import router as team_router
from routers.reports import router as reports_router
from routers.support import router as support_router
from routers.onboarding import router as onboarding_router

app.include_router(auth_router)
app.include_router(me_router)
app.include_router(contact_router)
app.include_router(dashboard_router)
app.include_router(transactions_router)
app.include_router(payouts_router)
app.include_router(pay_links_router)
app.include_router(team_router)
app.include_router(reports_router)
app.include_router(support_router)
app.include_router(onboarding_router)


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
