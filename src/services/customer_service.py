from src.domain.entities.customer_entity import CustomerEntity
from src.infrastructure.repositories.customer_repository import CustomerRepository

class CustomerService():
    
    def __init__(self, db):
        self.db = db
        self.cust_repo = CustomerRepository(db=self.db)

    async def create_customer(self, customer_entity: CustomerEntity):
        customer_entity = await self.cust_repo.create_customer(customer=customer_entity)
        print(f"Customer Entity {customer_entity}")
        return customer_entity
    
    async def get_customer_details(self, customer_id: int)-> CustomerEntity :
        customer = await self.cust_repo.get_customer_details(customer_id=customer_id)
        return customer
    
    async def update_customer(self, customer_id: int)-> CustomerEntity :
        customer = await self.cust_repo.get_customer_details(customer_id=customer_id)
        print(customer.__dict__)
        return