from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass    

class Client(Base):

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)

