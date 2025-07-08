from datetime import datetime, timezone
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.user.application.ports.user_repository import IUserRepository
from app.user.domain.factories.user_factory import create_user_by_role
from app.user.entities.user import User
from app.user.infrastructure.models.user_model import UserModel
from app.user.interface_adapters.dtos.user_profile_update_dto import (
    UserProfileUpdateDTO,
)
from app.user.mappers.user_mapper import UserMapper


class UserRepository(IUserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, user: User):
        model = UserMapper.to_orm(user)
        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)
        return UserMapper.to_domain(model)

    async def update_role(self, user: User) -> UserModel:
        result = await self.db.execute(select(UserModel).where(UserModel.id == user.id))
        model = result.scalar_one_or_none()
        if not model:
            raise Exception("User not found")

        # Campos permitidos para modificar
        model.name = user.name
        model.last_name = user.last_name
        model.role = user.role.value
        model.updated_at = datetime.now(timezone.utc)

        await self.db.commit()
        await self.db.refresh(model)
        return model

    async def update_profile(
        self, user_id: int, dto: UserProfileUpdateDTO
    ) -> UserModel:
        result = await self.db.execute(select(UserModel).where(UserModel.id == user_id))
        model = result.scalar_one_or_none()

        if not model:
            raise Exception("User not found")

        # Aquí aplicas los cambios usando el mapper
        UserMapper.apply_profile_update(model, dto)

        self.db.add(
            model
        )  # opcional, a veces no necesario si el objeto ya está en sesión
        await self.db.commit()
        await self.db.refresh(model)
        return model

    async def update_password_by_email(
        self, email: str, new_hashed_password: str
    ) -> None:
        stmt = (
            update(UserModel)
            .where(UserModel.email == email)
            .values(
                hashed_password=new_hashed_password,
                updated_at=datetime.now(timezone.utc),
            )
            .execution_options(synchronize_session="fetch")
        )
        await self.db.execute(stmt)
        await self.db.commit()

    async def find_by_email(self, email: str) -> User:
        result = await self.db.execute(
            select(UserModel).where(UserModel.email == email.lower())
        )

        model = result.scalar_one_or_none()

        if not model:
            return None

        domain_user = UserMapper.to_domain(model)

        return create_user_by_role(domain_user)

    async def exists_by_email(self, email: str) -> bool:
        result = await self.db.execute(
            select(UserModel.id).where(UserModel.email == email)
        )
        user_id = result.scalar_one_or_none()

        return user_id is not None
