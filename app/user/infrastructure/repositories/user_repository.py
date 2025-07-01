from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.user.domain.user import User
from app.user.infrastructure.models.user_model import UserModel


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, user: User):
        model = UserModel(**user.__dict__)
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)
        return model

    async def find_by_email(self, email: str):
        result = await self.db.execute(
            select(UserModel).where(UserModel.email == email)
        )
        return result.scalar_one_or_none()
