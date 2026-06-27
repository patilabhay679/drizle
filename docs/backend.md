# Drizle Pay — Backend

## Stack
- **Python 3.13+** — FastAPI + uvicorn
- **MongoDB Atlas** — via `pymongo` 4.17+ `AsyncMongoClient`
- **JWT** — `PyJWT` HS256, 24-hour tokens
- **Auth** — `bcrypt` password hashing, `HTTPBearer` header

## Setup

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py   # → http://localhost:8000
```

`settings.json` (gitignored) holds `MONGODB_URI`. You can also set it as `MONGODB_URI` env var.

## Project Structure

```
backend/
├── app.py              # FastAPI app — routes, models, lifespan
├── requirements.txt    # Python deps
├── build/              # Built frontend (served by FastAPI)
├── settings.json       # MongoDB credentials (gitignored)
└── .venv/              # Virtual env
```

## API Routes

### Auth (public)

| Method | Path | Body | Returns |
|--------|------|------|---------|
| POST | `/api/v1/auth/register` | `{email, password, name, company?}` | `{access_token, merchant}` |
| POST | `/api/v1/auth/login` | `{email, password}` | `{access_token, merchant}` |
| POST | `/api/v1/auth/verify-email?token=` | — | `{verified, email}` |
| POST | `/api/v1/auth/forgot-password` | `{email}` | `{ok}` |
| POST | `/api/v1/auth/reset-password` | `{token, new_password}` | `{ok}` |

### Auth (Bearer token required)

| Method | Path | Body | Returns |
|--------|------|------|---------|
| GET | `/api/v1/me` | — | merchant profile |
| PUT | `/api/v1/me` | `{name?, company?}` | updated merchant |
| PUT | `/api/v1/auth/change-password` | `{current_password, new_password}` | `{ok}` |
| POST | `/api/v1/auth/rotate-api-keys` | — | `{publishable, secret}` |
| GET | `/api/v1/me/api-keys` | — | `{publishable, secret}` |

### Data (Bearer token required)

| Method | Path | Body | Returns |
|--------|------|------|---------|
| GET | `/api/v1/transactions?page=&limit=` | — | `{data[], total, page, limit}` |
| GET | `/api/v1/payouts?page=&limit=` | — | `{data[], total, page, limit}` |

### Public

| Method | Path | Body | Returns |
|--------|------|------|---------|
| POST | `/api/v1/contact` | `{name, email, company?, phone?, message}` | `{ok}` |

### SPA Catch-all
`GET /*` — serves built frontend from `build/` directory.

## MongoDB Collections

- **users** — merchants, auth, profile, api_keys
- **transactions** — per-merchant payment records
- **payouts** — per-merchant payout records
- **contact_submissions** — contact form entries

Demo merchant `demo@drizlepay.com` / `demo123` seeds automatically on first run with 25 sample transactions and 8 payouts.

## Architecture Notes

- `lifespan` context manager handles MongoDB connection lifecycle
- `_serialize()` strips `_id` from MongoDB docs before returning JSON
- All DB operations use native `async/await` via `AsyncMongoClient`
- CORS allows `localhost:5173/4173` and `drizlepay.com`
