from datetime import datetime, date
from ..enums.gender import Gender

class ClientEntity:

    def __init__(self, first_name, last_name, dob, gender, city, state, country, pincode):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.dob: date = dob
        self.gender: Gender = gender
        self.city: str = city
        self.state: str = state
        self.country: str = country
        self.pincode: str = pincode  
        self.is_verified: bool = False 
        self.created_at: datetime = datetime.now(datetime.timezone.utc)
        self.updated_at: datetime = datetime.unow(datetime.timezone.utc)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"    