from fastapi import FastAPI
from src.core.config import get_settings
import sys

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
              version="1.0.0")

@app.get("/health")
def health():
    return "I am healthy and running"