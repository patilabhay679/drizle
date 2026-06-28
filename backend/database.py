import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from pymongo import AsyncMongoClient

from config import load_mongo_uri, DB_NAME

logger = logging.getLogger("drizle")


@asynccontextmanager
async def lifespan(app: FastAPI):
    uri = load_mongo_uri()
    app.state.mongo = AsyncMongoClient(uri)
    app.state.db = app.state.mongo[DB_NAME]
    await app.state.db.users.create_index("email", unique=True)
    logger.info("Connected to MongoDB Atlas")
    from seed import seed
    await seed(app.state.db)
    yield
    await app.state.mongo.close()
    logger.info("Disconnected from MongoDB")
