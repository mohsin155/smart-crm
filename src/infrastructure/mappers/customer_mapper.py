from src.models.customer_model import CustomerModel
from src.domain.entities.customer_entity import CustomerEntity

def create_model(customer_entity: CustomerEntity) -> CustomerModel :
    customer_model = CustomerModel(
        first_name=customer_entity.first_name,
        last_name=customer_entity.last_name,
        email=customer_entity.email,
        created_at=customer_entity.created_at,
        updated_at=customer_entity.updated_at
    )
    return customer_model

def create_entity(customer_model: CustomerModel) -> CustomerEntity:
    customer = CustomerEntity(
        id=customer_model.id,
        first_name=customer_model.first_name,
        last_name=customer_model.last_name,
        email=customer_model.email
    )

    return customer