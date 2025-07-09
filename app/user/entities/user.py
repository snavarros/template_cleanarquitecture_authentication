from enum import Enum


class RoleEnum(str, Enum):
    GUEST = "guest"
    ADMIN = "admin"
    GOD = "god"


class User:
    def __init__(
        self,
        id: int | None,
        name: str,
        last_name: str,
        email: str,
        hashed_password: str,
        phone: str,
        region: int,
        role: RoleEnum,
        is_active: bool,
        provider: str,
    ):
        self.id = id
        if "@" not in email:
            raise ValueError("Invalid email")

        self.name = name
        self.last_name = last_name
        self.email = email
        self.hashed_password = hashed_password
        self.phone = phone
        self.region = region
        self.role = role
        self.is_active = is_active
        self.provider = provider


class GuestUser(User):
    pass


class AdminUser(User):
    pass
