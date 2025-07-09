from fastapi import APIRouter, Depends

from app.auth.interface_adapters.dependencies.auth import get_current_user
from app.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.user.application.use_cases.change_user_role import ChangeUserRoleUseCase
from app.user.application.use_cases.update_user_profile import UpdateUserProfileUseCase
from app.user.entities.user import User
from app.user.infrastructure.repositories.user_repository import UserRepository
from app.user.interface_adapters.dtos.role_updated_dto import RoleUpdateDTO
from app.user.interface_adapters.dtos.user_profile_update_dto import (
    UserProfileUpdateDTO,
)
from app.user.interface_adapters.dtos.user_response_dto import UserResponseDTO
from app.user.interface_adapters.presenters.user_presenter import UserPresenter


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserResponseDTO)
async def get_user_me(current_user: User = Depends(get_current_user)):
    return UserPresenter.present_user(current_user)


@router.patch("/me")
async def update_my_profile(
    dto: UserProfileUpdateDTO,
    current_user=Depends(get_current_user),
    db=Depends(get_db),
):
    repo = UserRepository(db)
    use_case = UpdateUserProfileUseCase(repo)
    await use_case.execute(current_user, dto)
    return {"message": "Profile updated successfully"}


@router.patch("/{user_email}/role")
async def update_user_role(
    user_email: str,
    dto: RoleUpdateDTO,
    current_user=Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    repo = UserRepository(db)
    use_case = ChangeUserRoleUseCase(repo)
    await use_case.execute(current_user, user_email, dto.new_role)
    return {"message": f"Role changed to {dto.new_role.value}"}
