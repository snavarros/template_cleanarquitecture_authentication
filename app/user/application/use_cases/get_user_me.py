from app.user.domain.user import User


class GetUserMe:
    def __init__(self, repo):
        self.repo = repo

    async def execute(self, email: str) -> User:
        return await self.repo.find_by_email(email)
