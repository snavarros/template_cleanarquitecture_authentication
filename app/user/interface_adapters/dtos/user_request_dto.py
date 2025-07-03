from typing import Annotated
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    StringConstraints,
    field_validator,
)
import re


class UserRegisterDTO(BaseModel):
    name: Annotated[str, StringConstraints(min_length=2, max_length=50)]
    last_name: Annotated[str, StringConstraints(min_length=2, max_length=50)]
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8)]
    phone: Annotated[str, StringConstraints(min_length=9, max_length=20)]
    region: Annotated[int, Field(ge=1, le=16)]

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v):
        pattern = r"^\+\d{1,3}\d{7,14}$"
        if not re.match(pattern, v):
            raise ValueError("Invalid phone number format")
        return v


class UserLoginDTO(BaseModel):
    email: EmailStr
    password: str
