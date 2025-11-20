from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class CustomerModel(Base):

    __tablename__ = "customers"

    id=Column(Integer, primary_key=True, index=True)
    first_name=Column(String)
    last_name=Column(String)
    email=Column(String)
    created_at=Column(DateTime)
    updated_at=Column(DateTime)
