import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# Enable CORS for development (SvelteKit runs on 5173/4173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:4173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# 1. BACKEND ROUTES (Must be defined first)
# ==========================================
# By prefixing all your backend routes with "/api", 
# FastAPI instantly knows these belong to Python.

@app.get("/api/v1/transactions")
async def get_transactions():
    return [{"id": "tx_123", "amount": 100.00, "status": "success"}]

@app.post("/api/v1/charge")
async def process_charge():
    return {"status": "processing"}


# ==========================================
# 2. FRONTEND SPA CATCH-ALL (Defined last)
# ==========================================
# This wildcard route catches any URL that didn't match the API routes above.

@app.get("/{catchall:path}")
async def serve_spa(catchall: str):
    # Define the path to your SvelteKit build folder
    frontend_dir = "build"
    file_path = os.path.join(frontend_dir, catchall)

    # A. If the browser is asking for a real file (like /_app/immutable/nodes/0.js or /favicon.png)
    # serve that specific file directly.
    if os.path.isfile(file_path):
        return FileResponse(file_path)

    # B. If it's a directory, check if it has an index.html file
    if os.path.isdir(file_path):
        index_path = os.path.join(file_path, "index.html")
        if os.path.isfile(index_path):
            return FileResponse(index_path)

    # C. Support static adapter's clean routing for pre-rendered pages (e.g. /about -> build/about.html)
    html_path = file_path.rstrip("/") + ".html"
    if os.path.isfile(html_path):
        return FileResponse(html_path)

    # D. Fall back to core 'index.html' for SPA client-side routing
    return FileResponse(os.path.join(frontend_dir, "index.html"))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)