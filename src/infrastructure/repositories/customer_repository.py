from sqlalchemy.orm import Session
from src.domain.entities.customer_entity import CustomerEntity
from src.infrastructure.mappers.customer_mapper import create_model, create_entity
from src.models.customer_model import CustomerModel

class CustomerRepository:

    def __init__(self, db : Session):
        self.db = db

    async def create_customer(self, customer: CustomerEntity):
        customer_model = create_model(customer_entity=customer)
        self.db.add(customer_model)
        self.db.commit()
        self.db.refresh(customer_model)
        customer.id = customer_model.id
        return customer

    async def get_customer_details(self, customer_id: int) -> CustomerEntity:
        customer_model = self.db.get(CustomerModel, customer_id)
        return create_entity(customer_model=customer_model) if customer_model else None