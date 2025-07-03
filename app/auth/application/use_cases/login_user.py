from datetime import timedelta
from app.auth.infrastructure.services.jwt_auth_service import AuthServiceJWT
from app.config.settings import settings
from app.user.application.ports.user_repository import IUserRepository
from app.user.interface_adapters.dtos.user_request_dto import UserLoginDTO


class LoginUser:
    def __init__(self, repo: IUserRepository, auth_service: AuthServiceJWT):
        self.repo = repo
        self.auth = auth_service

    async def execute(self, dto: UserLoginDTO):
        db_user = await self.repo.find_by_email(dto.email)
        if not db_user or not self.auth.verify_password(
            dto.password, db_user.hashed_password
        ):
            raise Exception("Invalid credentials")
        return self.auth.create_access_token(
            data={"sub": str(db_user.email)},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        )
