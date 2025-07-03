from app.user.application.ports.user_repository import IUserRepository
from app.user.entities.user import User
from app.user.interface_adapters.dtos.user_profile_update_dto import (
    UserProfileUpdateDTO,
)


class UpdateUserProfileUseCase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    async def execute(self, current_user: User, dto: UserProfileUpdateDTO):
        # Validación opcional de reglas
        if not current_user.is_active:
            raise ValueError("Inactive users cannot update profile.")

        return await self.repo.update_profile(current_user.id, dto)
