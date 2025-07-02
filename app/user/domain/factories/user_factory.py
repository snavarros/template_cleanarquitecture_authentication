from app.user.entities.user import RoleEnum, User


def create_user_by_role(
    name: str, last_name: str, email: str, hashed_password: str, role: RoleEnum
) -> User:
    if role == RoleEnum.GUEST:
        from app.user.entities.user import GuestUser

        return GuestUser(name, last_name, email, hashed_password, role)
    if role == RoleEnum.ADMIN:
        from app.user.entities.user import AdminUser

        return AdminUser(name, last_name, email, hashed_password, role)

    else:
        raise ValueError(f"Invalid role: {role}")
