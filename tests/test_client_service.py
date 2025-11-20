from src.services.client_service import ClientService
from unittest.mock import patch, MagicMock, AsyncMock
import pytest
from src.domain.entities.client_entity import ClientEntity
from src.infrastructure.repositories.client_repository import ClientRepository

@pytest.mark.asyncio
@patch('src.infrastructure.repositories.client_repository.ClientRepository')
async def test_create_register_success(mock_repo):
    repo_mock = MagicMock()
    client = ClientEntity(
        first_name="Mohsin",
        last_name="Hassan",
        dob="12-02-2000",
        gender="male",
        city="bengaluru",
        state="karnataka",
        pincode="560029",
        country='india'
    )
    repo_mock.create = AsyncMock(return_value=client)
    mock_repo.return_value = repo_mock
    service = ClientService(db=MagicMock())
    result = await service.register_client(client=client)

    assert result == client
