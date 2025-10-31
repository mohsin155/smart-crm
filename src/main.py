from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from .infrastructure.integrations.aws_client import AWSClient
from .infrastructure.database.postgresdb import check_database

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    #response = AWSClient.get_parameter_store("smart-crm-local")
    #print(f"Parameter {response}")
    await check_database()
    yield

def get_env_from_args():
    if "--env" in sys.argv:
        index = sys.argv.index("--env")
        if index + 1 < len(sys.argv):
            return sys.argv[index + 1]
    return None

env = get_env_from_args()
settings = get_settings(env)
print(settings)
app = FastAPI(title="Smart CRM", 
              description=" AI Enabled CRM",
              version="1.0.0",
              lifespan=lifespan)

@app.get("/health")
def health():
    return "I am healthy and running"