from ...domain.entities.client_entity import ClientEntity
from ...models.client_model import ClientModel

def create_model(client_entity: ClientEntity) -> ClientModel:
    client_model = ClientModel(
        first_name=client_entity.first_name,
        last_name=client_entity.last_name,
        email=client_entity.email,
        password=client_entity.password,
        dob=client_entity.dob,
        gender=client_entity.gender,
        state=client_entity.state,
        city=client_entity.city,
        country=client_entity.country,
        pincode=client_entity.pincode,
        created_at=client_entity.created_at,
        updated_at=client_entity.updated_at
    )
    return client_model


def get_entity(client_model: ClientModel) -> ClientEntity:
    client_entity = ClientEntity(
        
    )
