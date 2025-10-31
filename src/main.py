from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from .infrastructure.integrations.aws_client import AWSClient
from .infrastructure.database.postgresdb import check_database

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await check_database()
    yield

app = FastAPI(title="Smart CRM", 
              description=" AI Enabled CRM",
              version="1.0.0",
              lifespan=lifespan)

@app.get("/health")
def health():
    return "I am healthy and running"