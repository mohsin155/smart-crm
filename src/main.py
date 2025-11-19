from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Request, status
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

# Overriding the default validation error handler
# Custom Exception Handler for Request Validation Errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    custom_errors = []
    for err in exc.errors():
        field = ".".join(str(x) for x in err["loc"] if x != "body")
        field = field if len(field) > 0 else err["type"]
        custom_errors.append({
            "field": field,
            "message": f"Invalid value for '{field}': {err['msg']}"
        })
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": True, "details": custom_errors},
    )

@app.get("/health")
def health():
    return "I am healthy and running"

