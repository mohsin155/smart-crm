from ..domain.entities.client_entity import ClientEntity

from ..infrastructure.database.postgresdb import get_db
from ..infrastructure.respositories.client_repository import ClientRepository
from sqlalchemy.orm import Session

class ClientService:

    async def register_client(self, client: ClientEntity):
        client_repos = ClientRepository.create_client(client)
        pass