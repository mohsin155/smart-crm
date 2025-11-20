from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pydantic import BaseModel
from ..infrastructure.integrations.aws_client import AWSClient
from functools import lru_cache

class PostgresConfig(BaseModel):
    host: str
    port: str
    username: str
    password: str
    database: str

class Settings(BaseSettings):
    app_name: str 
    debug: bool = True
    parameter_store: str
    postgres_config: PostgresConfig | None = None
    
    model_config = SettingsConfigDict(extra="ignore")

@lru_cache
def get_settings(env: str | None = None) -> Settings:
    env_folder = "src/env"
    env = env or os.environ.get("ENV", "dev")  # Default to 'dev' if ENV is not set
    env_file = os.path.join(env_folder, f".env.{env}")
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Env file does not exist: {env_file}")
    settings = Settings(_env_file=env_file)
    paramValues = AWSClient.get_parameter_store(settings.parameter_store)
    print(f"Successfully fetched Parameter Store value")
    merged_settings = settings.model_dump() | paramValues
    
    # Map postgres_db from parameter store to postgres_config
    if 'postgres_db' in merged_settings:
        postgres_data = merged_settings['postgres_db'].copy()
        postgres_data['database'] = postgres_data.get('database', 'smartcrm')
        merged_settings['postgres_config'] = PostgresConfig(**postgres_data)
        del merged_settings['postgres_db']
    return Settings(**merged_settings)