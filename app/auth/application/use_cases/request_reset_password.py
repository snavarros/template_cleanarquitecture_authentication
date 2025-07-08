from app.auth.infrastructure.services.jwt_auth_service import AuthServiceJWT
from app.user.application.ports.user_repository import IUserRepository


class RequestResetPasswordUseCase:
    def __init__(
        self, repo: IUserRepository, token_service: AuthServiceJWT, email_service
    ):
        self.repo = repo
        self.token_service = token_service
        self.email_service = email_service

    async def execute(self, email: str):
        user = await self.repo.find_by_email(email)
        if not user:
            return  # Por seguridad, no decir que no existe

        token = self.token_service.generate_password_reset_token(
            email, expires_minutes=15
        )
        # 👉 Aquí enviarías el token por correo
        print(f"Reset link: https://tuapp.com/reset-password?token={token}")
        await self.email_service.send_password_reset_email(email, token)
