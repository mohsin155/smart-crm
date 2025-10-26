
from datetime import date, datetime
from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True, index=True  , nullable=False, unique=True)
    first_name: str
    last_name: str
    email: str
    password: str
    dob: date
    city: str
    state : str
    country: str
    pincode: str
    phone: int
    created_at: datetime | None = Field(default=None)
    updated_at: datetime | None = Field(default=None)