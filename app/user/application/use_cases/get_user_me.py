from app.user.application.ports.user_repository import IUserRepository
from app.user.entities.user import User


class GetUserMe:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    async def execute(self, email: str) -> User:
        return await self.repo.find_by_email(email)
