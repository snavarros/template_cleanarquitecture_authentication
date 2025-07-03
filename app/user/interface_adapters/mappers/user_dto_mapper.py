from app.user.entities.user import RoleEnum, User
from app.user.interface_adapters.dtos.user_request_dto import UserRegisterDTO


class UserDTOMapper:
    @staticmethod
    def from_create_dto(dto: UserRegisterDTO, hashed_password: str) -> User:
        return User(
            id=None,
            name=dto.name,
            last_name=dto.last_name,
            email=dto.email,
            hashed_password=hashed_password,
            phone=dto.phone,
            region=dto.region,
            role=RoleEnum.GUEST,  # Forzado
        )
