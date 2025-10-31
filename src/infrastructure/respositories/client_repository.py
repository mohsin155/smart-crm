from sqlalchemy.orm import Session
from fastapi import Depends
from ..database.postgresdb import get_db
from ...domain.entities.client_entity import ClientEntity
from ..mappers.client_mapper import create_model

class ClientRepository():

    db: Session
    def __init__(self, db:Session=Depends(get_db())):
        self.db = db

    async def create_client(self, client: ClientEntity):
        client_model = create_model(client_entity=client)
        self.db.add(client_model)
        self.db.refresh(client_model)
        return 

    async def update_client():
        pass