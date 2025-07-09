from app.user.entities.user import AdminUser, GuestUser, RoleEnum, User


def create_user_by_role(user: User) -> User:
    match user.role:
        case RoleEnum.ADMIN:
            return AdminUser(**user.__dict__)
        case RoleEnum.GUEST:
            return GuestUser(**user.__dict__)
        case _:
            raise ValueError(f"Rol no reconocido: {user.role}")
