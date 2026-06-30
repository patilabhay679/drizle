import os
import json

AUTH_SECRET_KEY = os.environ.get("AUTH_SECRET_KEY")
if not AUTH_SECRET_KEY:
    raise RuntimeError("AUTH_SECRET_KEY environment variable must be set")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440
DB_NAME = "drizle"


def load_mongo_uri() -> str:
    uri = os.environ.get("MONGODB_URI")
    if uri:
        return uri
    settings_path = os.path.join(os.path.dirname(__file__), "settings.json")
    try:
        with open(settings_path) as f:
            cfg = json.load(f)
        return cfg["MONGODB_URI"]
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        pass
    raise RuntimeError("MONGODB_URI not configured — set env var or add to settings.json")
