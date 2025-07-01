from pydantic import BaseModel, EmailStr


class UserRegisterDTO(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str
    role_id: int


class UserLoginDTO(BaseModel):
    email: EmailStr
    password: str
