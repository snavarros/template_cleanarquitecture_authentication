from pydantic import BaseModel

from app.user.entities.user import RoleEnum


class RoleUpdateDTO(BaseModel):
    new_role: RoleEnum
