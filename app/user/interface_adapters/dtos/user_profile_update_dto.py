from pydantic import BaseModel, Field
from typing import Optional


class UserProfileUpdateDTO(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    last_name: Optional[str] = Field(None, min_length=2, max_length=50)
    phone: Optional[str]
    region: Optional[int] = Field(None, ge=1, le=16)
