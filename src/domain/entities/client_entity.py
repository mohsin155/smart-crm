from datetime import datetime, date, timezone
from ..enums.gender import Gender

class ClientEntity:

    def __init__(self, first_name, last_name, email, dob, gender, password, city, state, country, pincode):
        self.id: int | None = None
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email
        self.dob: date = dob
        self.gender: Gender = gender
        self.password: str = password
        self.city: str = city
        self.state: str = state
        self.country: str = country
        self.pincode: str = pincode  
        self.is_verified: bool = False 
        self.created_at: datetime = datetime.now(timezone.utc)
        self.updated_at: datetime = datetime.now(timezone.utc)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"    