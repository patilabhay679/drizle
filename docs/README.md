# Drizle Pay

Full-stack payment platform — FastAPI backend + SvelteKit frontend.

## Quick Start

```bash
# Backend
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py                    # → http://localhost:8000

# Frontend (separate terminal)
cd frontend
npm install
npm run dev                      # → http://localhost:5173
```

Demo login: `demo@drizlepay.com` / `demo123`

## Documentation

- [Backend](./backend.md) — API routes, MongoDB, auth, setup
- [Frontend](./frontend.md) — routing, components, state, conventions

## Architecture

```
Browser ──┬── /api/v1/* ──→ FastAPI ──→ MongoDB Atlas
          └── /* ──────→ FastAPI serves built SvelteKit (SPA)
```

In dev, Vite proxies `/api` → `http://localhost:8000`. In production, FastAPI serves both the API and the built frontend from `backend/build/`.

## Build

```bash
cd frontend && npm run build    # outputs to ../backend/build
cd ../backend && python app.py  # serves API + frontend on :8000
```
