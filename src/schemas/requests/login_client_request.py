from pydantic_core import PydanticCustomError
from pydantic import BaseModel, EmailStr, constr, Field, field_validator, model_validator
from datetime import date
from ...domain.enums.gender import Gender
from typing import TypeAlias

PinConstraint: TypeAlias = constr(min_length=3, max_length=6) # type:ignore

class LoginClientRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=20)

