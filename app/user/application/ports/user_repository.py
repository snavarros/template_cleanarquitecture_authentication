from abc import ABC, abstractmethod

from app.user.entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    async def save(self, user, roles):
        pass

    @abstractmethod
    async def find_by_email(self, email: str):
        pass

    @abstractmethod
    async def exists_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    async def update_profile(self, user_id: int, dto) -> User:
        pass

    @abstractmethod
    async def update_role(self, user_id: int, dto) -> User:
        pass
