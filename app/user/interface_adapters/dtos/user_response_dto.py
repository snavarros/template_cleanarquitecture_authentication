from pydantic import BaseModel

from app.user.entities.user import RoleEnum


class UserResponseDTO(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    phone: str
    region: int
    role: RoleEnum
    is_active: bool


class TokenResponseDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"
