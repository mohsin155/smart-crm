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
    print(f"Settings : {settings}")
    paramValues = AWSClient.get_parameter_store(settings.parameter_store)
    merged_settings = settings.model_dump() | paramValues
    print(f"Merged : {merged_settings}")
    return Settings(**merged_settings)