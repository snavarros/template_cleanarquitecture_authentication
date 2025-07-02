from datetime import timedelta
from app.config.settings import settings
from app.user.application.ports.user_repository import IUserRepository
from app.user.domain.exceptions.exceptions import (
    EmailAlreadyExistsError,
    WeakPasswordError,
)
from app.user.entities.user import RoleEnum, User
from app.user.domain.validators.password_validator import validate_password_strength


class RegisterUser:
    def __init__(self, repo: IUserRepository, auth_service):
        self.repo = repo
        self.auth = auth_service

    async def execute(self, dto):
        if await self.repo.exists_by_email(dto.email):
            raise EmailAlreadyExistsError(dto.email)

        errors = validate_password_strength(dto.password)

        if errors:
            raise WeakPasswordError(errors)

        hashed = self.auth.hash_password(dto.password)

        # Forzar rol viewer sin importar entrada
        role_enum = RoleEnum.GUEST

        user = User(
            name=dto.name,
            last_name=dto.last_name,
            email=dto.email,
            hashed_password=hashed,
            role=role_enum,
        )
        await self.repo.save(user)
        return self.auth.create_access_token(
            data={"sub": str(user.email)},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        )
