from sqlalchemy import Column, String, Boolean, Integer, Date, DateTime, Enum
from sqlalchemy.orm import DeclarativeBase
from ..domain.enums.gender import Gender

class Base(DeclarativeBase):
    pass    

class ClientModel(Base):

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    dob = Column(Date)
    gender = Column(Enum(Gender), nullable=False)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    pincode = Column(String)
    is_verified = Column(Boolean, default=False) 
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

