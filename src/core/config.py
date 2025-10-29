from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    app_name: str
    debug: bool
    database_url: str
    
    model_config = SettingsConfigDict(env_file=None, extra="ignore")

def get_settings(env: str = None) -> Settings:
    env = env or os.environ.get("ENV", "dev")  # Default to 'dev' if ENV is not set
    env_file_map = {
        "dev": "env/.env.dev",
        "uat": "env/.env.uat",
        "prod": "env/.env.prod"
    }
    env_file = env_file_map.get(env, None)
    if not env_file:
        raise ValueError(f"Invalid environment: {env}")
    return Settings(_env_file=env_file) 