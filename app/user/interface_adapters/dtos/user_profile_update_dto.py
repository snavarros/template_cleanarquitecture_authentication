import re
from pydantic import BaseModel, StringConstraints, field_validator
from typing import Annotated


class UserProfileUpdateDTO(BaseModel):
    name: Annotated[str, StringConstraints(min_length=2, max_length=50)]
    last_name: Annotated[str, StringConstraints(min_length=2, max_length=50)]
    phone: Annotated[str, StringConstraints(min_length=9, max_length=20)]

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v):
        pattern = r"^\+\d{1,3}\d{7,14}$"
        if not re.match(pattern, v):
            raise ValueError("Invalid phone number format")
        return v
