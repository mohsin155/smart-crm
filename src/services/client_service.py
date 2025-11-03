from ..domain.entities.client_entity import ClientEntity

from ..infrastructure.database.postgresdb import get_db
from ..infrastructure.respositories.client_repository import ClientRepository
from sqlalchemy.orm import Session

class ClientService:

    def __init__(self, db):
        self.db = db

    async def register_client(self, client: ClientEntity):
        client_repo = ClientRepository(self.db)
        await client_repo.create(client=client)
        return client