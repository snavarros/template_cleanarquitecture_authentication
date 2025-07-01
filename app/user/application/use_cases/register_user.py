from app.user.domain.exceptions.exceptions import WeakPasswordError
from app.user.domain.user import User
from app.user.domain.validators.password_validator import validate_password_strength


class RegisterUser:
    def __init__(self, repo, auth_service):
        self.repo = repo
        self.auth = auth_service

    async def execute(self, dto):
        errors = validate_password_strength(dto.password)

        if errors:
            raise WeakPasswordError(errors)

        hashed = self.auth.hash_password(dto.password)
        user = User(
            name=dto.name,
            last_name=dto.last_name,
            email=dto.email,
            hashed_password=hashed,
            role_id=dto.role_id,
        )
        await self.repo.save(user)
        return self.auth.create_token(user.email)
