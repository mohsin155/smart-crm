from datetime import datetime, timezone

class CustomerEntity:

    def __init__(self, id: int | None, first_name: str, last_name: str, email: str):
        self.id = id 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at: datetime = datetime.now(timezone.utc)
        self.updated_at: datetime = datetime.now(timezone.utc)
