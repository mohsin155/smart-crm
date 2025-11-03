from sqlalchemy.orm import Session
from fastapi import Depends

from ...domain.entities.client_entity import ClientEntity
from ..mappers.client_mapper import create_model

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