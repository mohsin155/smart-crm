from sqlalchemy.orm import Session
from fastapi import Depends

from ...domain.entities.client_entity import ClientEntity
from ...models.client_model import ClientModel
from ..mappers.client_mapper import create_model, get_entity

class ClientRepository():

    db: Session
    def __init__(self, db:Session):
        self.db = db

    async def create(self, client: ClientEntity):
        client_model = create_model(client_entity=client)
        self.db.add(client_model)
        self.db.commit() 
        self.db.refresh(client_model)
        client.id = client_model.id
        return client

    async def update_client():
        pass
    async def get_client_by_email(self, email: str) -> ClientEntity | None:
        client_model = self.db.query(ClientModel).filter(ClientModel.email == email).first()
        if client_model:
            return get_entity(client_model)
        return None