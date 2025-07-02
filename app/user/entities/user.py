from enum import Enum


class RoleEnum(str, Enum):
    GUEST = "guest"
    ADMIN = "admin"
    GOD = "god"


class User:
    def __init__(
        self,
        name: str,
        last_name: str,
        email: str,
        hashed_password: str,
        role: RoleEnum,
    ):
        if "@" not in email:
            raise ValueError("Invalid email")

        self.name = name
        self.last_name = last_name
        self.email = email
        self.hashed_password = hashed_password
        self.role = role


class GuestUser(User):
    pass


class AdminUser(User):
    pass
