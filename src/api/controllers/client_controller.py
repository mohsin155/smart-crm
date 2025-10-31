"""
Route API endpoint
"""

from fastapi import APIRouter, Depends
from ...schemas.requests.register_client_request import RegisterClientRequest
from ...domain.entities.client_entity import Client
from ...services.client_service import ClientService

router = APIRouter(prefix="/client")

@router.post("/register")
async def register_client(request: RegisterClientRequest, client_service: ClientService = Depends(ClientService())):
    try:
        client = Client(first_name=request.first_name,
                        last_name=request.last_name,
                        dob=request.dob,
                        gender=request.gender,
                        city=request.city,
                        state=request.state,
                        country=request.country,
                        pincode=request.pincode)
        
        client_service.register_client()
        return {}
    except Exception as e:
        return 