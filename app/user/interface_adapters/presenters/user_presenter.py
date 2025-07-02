from app.user.entities.user import User
from app.user.interface_adapters.dtos.user_response_dto import (
    TokenResponseDTO,
    UserResponseDTO,
)


class UserPresenter:
    @staticmethod
    def present_token(token: str) -> TokenResponseDTO:
        return TokenResponseDTO(access_token=token)

    @staticmethod
    def present_user(user: User) -> UserResponseDTO:
        return UserResponseDTO(
            name=user.name,
            last_name=user.last_name,
            email=user.email,
            role=user.role.value,
        )
