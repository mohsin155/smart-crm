from pydantic import BaseModel
from datetime import date

class RegisterClientRequest(BaseModel):
    first_name: str
    last_name: str
    dob: date
