from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.application.use_cases.login_user import LoginUser
from app.auth.application.use_cases.request_reset_password import (
    RequestResetPasswordUseCase,
)
from app.auth.application.use_cases.reset_password_with_token import (
    ResetPasswordWithTokenUseCase,
)
from app.auth.infrastructure.services.email_service import EmailService
from app.auth.infrastructure.services.jwt_auth_service import AuthServiceJWT
from app.auth.interface_adapters.dtos.request_reset_dto import RequestResetDTO
from app.auth.interface_adapters.dtos.reset_with_token_dto import (
    ResetPasswordWithTokenDTO,
)
from app.config.database import get_db
from app.user.application.use_cases.register_user import RegisterUser
from app.user.infrastructure.repositories.user_repository import UserRepository
from app.user.interface_adapters.presenters.user_presenter import UserPresenter
from app.user.interface_adapters.dtos.user_request_dto import (
    UserLoginDTO,
    UserRegisterDTO,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
async def register(dto: UserRegisterDTO, db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    auth = AuthServiceJWT()
    use_case = RegisterUser(repo, auth)
    user = await use_case.execute(dto)
    return {"message": f"User {user.email} created"}


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    repo = UserRepository(db)
    auth = AuthServiceJWT()
    use_case = LoginUser(repo, auth)

    # Crea un DTO a partir del form (email = username en OAuth2)
    dto = UserLoginDTO(
        email=form_data.username,
        password=form_data.password,
    )

    token = await use_case.execute(dto)
    return UserPresenter.present_token(token)


@router.post("/password/request-reset")
async def request_reset_password(dto: RequestResetDTO, db=Depends(get_db)):
    use_case = RequestResetPasswordUseCase(
        UserRepository(db), AuthServiceJWT(), EmailService()
    )
    await use_case.execute(dto.email)
    return {"message": "If the email exists, a reset link was sent"}


@router.post("/password/reset")
async def reset_password(dto: ResetPasswordWithTokenDTO, db=Depends(get_db)):
    use_case = ResetPasswordWithTokenUseCase(
        UserRepository(db), AuthServiceJWT(), AuthServiceJWT()
    )
    await use_case.execute(dto.token, dto.new_password)
    return {"message": "Password reset successfully"}
