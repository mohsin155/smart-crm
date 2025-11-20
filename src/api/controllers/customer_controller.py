from fastapi import APIRouter, Depends
from src.schemas.requests.create_customer_request import CreateCustomerRequest
from src.services.customer_service import CustomerService
from src.infrastructure.database.postgresdb import get_db
from sqlalchemy.orm import Session
from src.domain.entities.customer_entity import CustomerEntity

router = APIRouter(prefix="/customers")

def get_service_dependency(db: Session = Depends(get_db)):
    customer_service = CustomerService(db=db)
    return customer_service

@router.post("/create")
async def create_customer(request: CreateCustomerRequest, customer_service: CustomerService = Depends(get_service_dependency)):
    customer_entity = CustomerEntity(first_name=request.first_name, last_name=request.last_name, email=request.email)
    await customer_service.create_customer(customer_entity=customer_entity) 
    return {"message": "Customer created successfully", "data": customer_entity}

@router.get("/getDetails/{customer_id}")
async def get_customer_by_id(customer_id: int, customer_service: CustomerService = Depends(get_service_dependency)):
    customer = await customer_service.get_customer_details(customer_id=customer_id)
    return {"data": customer}

@router.put("/update/{customer_id}")
async def update_customer(customer_id: int, customer_service: CustomerService = Depends(get_service_dependency)):
    await customer_service.update_customer(customer_id=customer_id)
    return {"message": " Update successfully"}

