import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture(autouse=True)
def patch_db_modules():
    with patch("src.infrastructure.database.postgresdb.create_engine"), \
         patch("src.infrastructure.database.postgresdb.get_db"), \
         patch("src.infrastructure.database.postgresdb.settings") as mock_settings:

        mock_settings.postgres_config = MagicMock(
            username="fake",
            password="fake",
            host="localhost",
            port="5432",
            database="fake"
        )
        print(">>> conftest loaded for every test <<<")
        yield
