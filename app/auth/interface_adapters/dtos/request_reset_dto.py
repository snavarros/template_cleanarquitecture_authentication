from pydantic import BaseModel, EmailStr


class RequestResetDTO(BaseModel):
    email: EmailStr
