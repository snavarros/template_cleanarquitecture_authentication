from abc import ABC, abstractmethod


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
