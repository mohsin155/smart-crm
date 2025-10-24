from fastapi import FastAPI

app = FastAPI(title="Smart CRM", 
              description=" AI Enabled CRM",
              version="1.0.0")

@app.get("/health")
def health():
    return "I am healthy and running"