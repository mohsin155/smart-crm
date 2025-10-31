from pydantic import BaseModel, constr
from datetime import date
from ...domain.enums.gender import Gender
from typing import TypeAlias

PinConstraint: TypeAlias = constr(min_length=3, max_length=6) # type:ignore

class RegisterClientRequest(BaseModel):
    first_name: str
    last_name: str
    dob: date
    gender: Gender
    city: str
    state: str
    country: str
    pincode: PinConstraint

