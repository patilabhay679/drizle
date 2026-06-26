# Project Status: Drizle Pay

## Environment & OS
- **OS**: macOS
- **Node.js**: `v22.18.0`
- **Python**: `3.13.7`
- **Git status**: Diverged branch local vs origin/main.

---

## Workspace Structure
The project is split into two major parts: [backend](file:///Users/abhay/Desktop/drizle/backend) and [frontend](file:///Users/abhay/Desktop/drizle/frontend).

### 1. [Backend](file:///Users/abhay/Desktop/drizle/backend) (FastAPI)
- **[app.py](file:///Users/abhay/Desktop/drizle/backend/app.py)**: Running on port `8000` with CORS configured for the frontend.
- **[requirements.txt](file:///Users/abhay/Desktop/drizle/backend/requirements.txt)**: Python package list (fastapi, uvicorn, requests).

### 2. [Frontend](file:///Users/abhay/Desktop/drizle/frontend) (SvelteKit)
- **Vite & SvelteKit**: Running on port `5173`. Configured with `server.proxy` pointing to `localhost:8000` for api routing.
- **Build Output**: Static adapter page targets `../backend/build`.
- **[src/routes/+page.svelte](file:///Users/abhay/Desktop/drizle/frontend/src/routes/+page.svelte)**: Integrated custom Drizle Pay landing page.
