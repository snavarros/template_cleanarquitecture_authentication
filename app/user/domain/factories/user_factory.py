from app.user.entities.user import AdminUser, GuestUser, RoleEnum, User


def create_user_by_role(user: User) -> User:
    if user.role == RoleEnum.ADMIN:
        return AdminUser(**user.__dict__)
    elif user.role == RoleEnum.GUEST:
        return GuestUser(**user.__dict__)
    else:
        raise ValueError(f"Invalid role: {user.role}")
