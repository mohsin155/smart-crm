"""
Route API endpoint
"""

from fastapi import APIRouter, Depends, HTTPException, status
from ...schemas.requests.register_client_request import RegisterClientRequest
from ...schemas.requests.login_client_request import LoginClientRequest
from ...schemas.responses.login_response import LoginResponse
from ...domain.entities.client_entity import ClientEntity
from ...services.client_service import ClientService
from ...utils.jwt_utils import create_access_token
from sqlalchemy.orm import Session
from ...infrastructure.database.postgresdb import get_db

router = APIRouter(prefix="/client")
def get_service_dependency(db: Session = Depends(get_db)):
    client_service = ClientService(db)
    return client_service

@router.post("/register")
async def register_client(request: RegisterClientRequest, client_service :ClientService = Depends(get_service_dependency)):
    try:
        client = ClientEntity(first_name=request.first_name,
                        last_name=request.last_name,
                        email=request.email,
                        dob=request.dob,
                        gender=request.gender,
                        password=request.password,
                        city=request.city,
                        state=request.state,
                        country=request.country,
                        pincode=request.pincode)
        client = await client_service.register_client(client)
        return {"data": {"id":client.id} }
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error : {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.post("/login", response_model=LoginResponse)
async def login_client(request: LoginClientRequest, client_service: ClientService = Depends(get_service_dependency)):
    client = await client_service.login_client(request.email, request.password)
    
    access_token = create_access_token(data={"sub": client.email, "client_id": client.id})
    
    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
        client_id=client.id
    )