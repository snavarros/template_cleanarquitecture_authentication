from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.user.application.ports.user_repository import IUserRepository
from app.user.domain.factories.user_factory import create_user_by_role
from app.user.entities.user import RoleEnum, User
from app.user.infrastructure.models.user_model import UserModel


class UserRepository(IUserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, user: User):
        model = UserModel(**user.__dict__)
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)
        return model

    async def update(self, user: User) -> UserModel:
        result = await self.db.execute(select(UserModel).where(UserModel.id == user.id))
        model = result.scalar_one_or_none()
        if not model:
            raise Exception("User not found")

        # Campos permitidos para modificar
        model.name = user.name
        model.last_name = user.last_name
        model.role = user.role.value
        model.updated_at = datetime.now(datetime.timezone.utc)

        await self.db.commit()
        await self.db.refresh(model)
        return model

    async def find_by_email(self, email: str) -> User:
        result = await self.db.execute(
            select(UserModel).where(UserModel.email == email.lower())
        )

        model = result.scalar_one_or_none()

        if not model:
            return None

        role_enum = RoleEnum(model.role)

        return create_user_by_role(
            name=model.name,
            last_name=model.last_name,
            email=model.email,
            hashed_password=model.hashed_password,
            role=role_enum,
        )

    async def exists_by_email(self, email: str) -> bool:
        result = await self.db.execute(
            select(UserModel.id).where(UserModel.email == email)
        )
        user_id = result.scalar_one_or_none()

        return user_id is not None
