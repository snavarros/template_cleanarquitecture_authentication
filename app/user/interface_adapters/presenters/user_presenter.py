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
            id=user.id,
            name=user.name,
            last_name=user.last_name,
            email=user.email,
            phone=user.phone,
            region=user.region,
            role=user.role,
            is_active=user.is_active,
        )
