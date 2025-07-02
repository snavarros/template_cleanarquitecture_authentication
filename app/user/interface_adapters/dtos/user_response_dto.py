from pydantic import BaseModel

from app.user.entities.user import RoleEnum


class UserResponseDTO(BaseModel):
    name: str
    last_name: str
    email: str
    role: RoleEnum


class TokenResponseDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"
