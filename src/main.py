from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.infrastructure.database import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.init_db()
    print("Database Initialized")
    yield

app = FastAPI(lifespan=lifespan, title="smart crm", description="AI enabled CRM", version="1.0.0")


@app.get("/health")
async def healthCheck():
    return "I am healthy"