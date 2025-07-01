from pydantic import BaseModel


class UserResponseDTO(BaseModel):
    email: str
    message: str


class TokenResponseDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"
