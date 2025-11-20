from pydantic import BaseModel, EmailStr

class CreateCustomerRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    
    