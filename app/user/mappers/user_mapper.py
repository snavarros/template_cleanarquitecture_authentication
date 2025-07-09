from datetime import datetime, timezone
from app.user.entities.user import RoleEnum, User
from app.user.infrastructure.models.user_model import UserModel
from app.user.interface_adapters.dtos.user_profile_update_dto import (
    UserProfileUpdateDTO,
)


class UserMapper:
    @staticmethod
    def to_domain(model: UserModel) -> User:
        return User(
            id=model.id,
            name=model.name,
            last_name=model.last_name,
            email=model.email,
            hashed_password=model.hashed_password,
            phone=model.phone,
            region=model.region,
            role=RoleEnum(model.role),
            is_active=model.is_active,
            provider=model.provider,
        )

    @staticmethod
    def to_orm(entity: User) -> UserModel:
        return UserModel(
            id=entity.id,
            name=entity.name,
            last_name=entity.last_name,
            email=entity.email,
            hashed_password=entity.hashed_password,
            phone=entity.phone,
            region=entity.region,
            role=entity.role.value,
            is_active=entity.is_active,
            provider=entity.provider,
        )

    @staticmethod
    def apply_profile_update(model: UserModel, dto: UserProfileUpdateDTO):
        if dto.name is not None:
            model.name = dto.name
        if dto.last_name is not None:
            model.last_name = dto.last_name
        if dto.phone is not None:
            model.phone = dto.phone

        model.updated_at = datetime.now(timezone.utc)
