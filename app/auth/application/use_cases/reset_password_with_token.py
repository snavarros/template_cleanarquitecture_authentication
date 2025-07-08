from app.auth.infrastructure.services.jwt_auth_service import AuthServiceJWT
from app.user.application.ports.user_repository import IUserRepository
from app.user.domain.exceptions.exceptions import WeakPasswordError
from app.user.domain.validators.password_validator import validate_password_strength


class ResetPasswordWithTokenUseCase:
    def __init__(
        self, repo: IUserRepository, auth_service, token_service: AuthServiceJWT
    ):
        self.repo = repo
        self.auth_service = auth_service
        self.token_service = token_service

    async def execute(self, token: str, new_password: str):
        email = self.token_service.verify_token(token)
        user = await self.repo.find_by_email(email)
        if not user:
            raise ValueError(f"User with EMAIL: {user.email} does not exist.")

        errors = validate_password_strength(new_password)
        if errors:
            raise WeakPasswordError(errors)

        hashed_password = self.auth_service.hash_password(new_password)
        await self.repo.update_password_by_email(user.email, hashed_password)
