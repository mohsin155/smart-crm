from pydantic_core import PydanticCustomError
from pydantic import BaseModel, EmailStr, constr, Field, field_validator, model_validator
from datetime import date
from ...domain.enums.gender import Gender
from typing import TypeAlias

PinConstraint: TypeAlias = constr(min_length=3, max_length=6) # type:ignore

class RegisterClientRequest(BaseModel):
    first_name: str 
    last_name: str
    dob: date = Field(..., format="date"),
    email: EmailStr
    gender: Gender
    password: str = Field(..., min_length=6, max_length=20)
    confirm_password: str = Field(..., min_length=6, max_length=20)
    city: str = Field(..., min_length=2, max_length=20)
    state: str = Field(..., min_length=2, max_length=20)
    country: str = Field(..., min_length=2, max_length=20)
    pincode: PinConstraint 

    @field_validator("first_name")
    @classmethod
    def validate_firstName(cls, v):
        if (len(v) < 3 or len(v) > 20):
            # raise ValueError('First name must be between 3 and 20 characters')
            raise PydanticCustomError(
                "first_name",  # custom error code
                "First name must be between 3 and 20 characters."
            )
        return v
    
    @field_validator("last_name")
    @classmethod
    def validate_lastName(cls, v):
        if (len(v) < 3 or len(v) > 20):
            raise PydanticCustomError(
                "last_name",
                "Last name must be between 3 and 20 characters."
            )
        return v
    
    @model_validator(mode="after")
    def validate_passwords(self):
        if self.password != self.confirm_password:
            raise PydanticCustomError(
                "password_mismatch",
                "Password and Confirm Password do not match."
            )
        return self

