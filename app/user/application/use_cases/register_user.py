from app.auth.infrastructure.services.jwt_auth_service import AuthServiceJWT

from app.user.application.ports.user_repository import IUserRepository
from app.user.domain.exceptions.exceptions import (
    EmailAlreadyExistsError,
    WeakPasswordError,
)

from app.user.domain.validators.password_validator import validate_password_strength
from app.user.interface_adapters.dtos.user_request_dto import UserRegisterDTO
from app.user.interface_adapters.mappers.user_dto_mapper import UserDTOMapper


class RegisterUser:
    def __init__(self, repo: IUserRepository, auth_service: AuthServiceJWT):
        self.repo = repo
        self.auth = auth_service

    async def execute(self, dto: UserRegisterDTO):
        if await self.repo.exists_by_email(dto.email):
            raise EmailAlreadyExistsError(dto.email)

        errors = validate_password_strength(dto.password)

        if errors:
            raise WeakPasswordError(errors)

        hashed = self.auth.hash_password(dto.password)
        user = UserDTOMapper.from_create_dto(dto, hashed)
        saved = await self.repo.save(user)
        return saved
