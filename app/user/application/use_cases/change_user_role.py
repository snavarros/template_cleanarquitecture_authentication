from app.user.application.ports.user_repository import IUserRepository
from app.user.entities.user import AdminUser, RoleEnum, User


class ChangeUserRoleUseCase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    async def execute(
        self, current_user: User, target_user_email: str, new_role: str
    ) -> User:
        if not isinstance(current_user, AdminUser):
            raise PermissionError("Only admins can change user roles.")

        if current_user.email == target_user_email:
            raise ValueError("You cannot change your own role.")

        user = await self.repo.find_by_email(target_user_email)
        if not user:
            raise ValueError(f"User with EMAIL: {target_user_email} does not exist.")

        try:
            validated_role = RoleEnum(new_role)
        except ValueError:
            raise ValueError(f"Invalid role: {new_role}")

        user.role = validated_role
        await self.repo.update_role(user)
        return user
