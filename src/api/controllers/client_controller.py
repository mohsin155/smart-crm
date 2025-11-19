"""
Route API endpoint
"""

from fastapi import APIRouter, Depends
from ...schemas.requests.register_client_request import RegisterClientRequest
from ...domain.entities.client_entity import ClientEntity
from ...services.client_service import ClientService
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
                        dob=request.dob,
                        gender=request.gender,
                        city=request.city,
                        state=request.state,
                        country=request.country,
                        pincode=request.pincode)
        client = await client_service.register_client(client)
        return {"data": {"id":client.id} }
    except Exception as e:
        print(f"Error : {e}")
        return {"error": "Something wrong"}
    
    