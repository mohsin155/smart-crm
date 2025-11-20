from src.domain.entities.customer_entity import CustomerEntity
from src.infrastructure.repositories.customer_repository import CustomerRepository

class CustomerService():
    
    def __init__(self, db):
        self.db = db

    async def create_customer(self, customer_entity: CustomerEntity):
        cust_repo = CustomerRepository(db=self.db)
        customer_entity = await cust_repo.create_customer(customer=customer_entity)
        print(f"Customer Entity {customer_entity}")
        return customer_entity
    
    async def get_customer_details(self, customer_id: int)-> CustomerEntity :
        cust_repo = CustomerRepository(db=self.db)
        customer = await cust_repo.get_customer_details(customer_id=customer_id)
        return customer