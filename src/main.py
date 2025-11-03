from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from .infrastructure.integrations.aws_client import AWSClient
from .infrastructure.database.postgresdb import check_database, engine
from .api.controllers import client_controller
from .models.client_model import Base

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await check_database()
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Smart CRM", 
              description=" AI Enabled CRM",
              version="1.0.0",
              lifespan=lifespan)

app.include_router(client_controller.router)

@app.get("/health")
def health():
    return "I am healthy and running"