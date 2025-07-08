from typing import Annotated
from pydantic import BaseModel, StringConstraints


class ResetPasswordWithTokenDTO(BaseModel):
    token: str
    new_password: Annotated[str, StringConstraints(min_length=8)]
