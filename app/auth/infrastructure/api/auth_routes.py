from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.application.use_cases.login_user import LoginUser
from app.auth.infrastructure.services.jwt_auth_service import AuthServiceJWT
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
async def login(dto: UserLoginDTO, db=Depends(get_db)):
    repo = UserRepository(db)
    auth = AuthServiceJWT()
    use_case = LoginUser(repo, auth)
    token = await use_case.execute(dto)
    return UserPresenter.present_token(token)
