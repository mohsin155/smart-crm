from ..domain.entities.client_entity import ClientEntity
from ..infrastructure.database.postgresdb import get_db
from ..infrastructure.repositories.client_repository import ClientRepository
from ..utils.jwt_utils import verify_password, get_password_hash
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

class ClientService:

    def __init__(self, db):
        self.db = db

    async def register_client(self, client: ClientEntity):
        client_repo = ClientRepository(self.db)
        
        # Check if email already exists
        existing_client = await client_repo.get_client_by_email(client.email)
        if existing_client:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists"
            )
        
        client.password = get_password_hash(client.password)
        await client_repo.create(client=client)
        return client
    async def login_client(self, email: str, password: str) -> ClientEntity:
        client_repo = ClientRepository(self.db)
        client = await client_repo.get_client_by_email(email)
        
        if not client or not verify_password(password, client.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        return client