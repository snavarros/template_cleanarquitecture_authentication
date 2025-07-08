from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt

from app.config.settings import settings


class AuthServiceJWT:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain: str, hashed: str) -> bool:
        return self.pwd_context.verify(plain, hashed)

    def create_access_token(
        self, data: dict, expires_delta: timedelta | None = None
    ) -> str:
        to_encode = data.copy()
        expire = datetime.now(tz=timezone.utc) + (
            expires_delta or timedelta(minutes=30)
        )
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    def generate_password_reset_token(self, email: str, expires_minutes: int = 15):
        expire = datetime.now(tz=timezone.utc) + timedelta(minutes=int(expires_minutes))
        return jwt.encode(
            {"sub": email, "exp": expire}, settings.SECRET_KEY, algorithm="HS256"
        )

    def verify_token(self, token: str):
        from jose.exceptions import JWTError, ExpiredSignatureError

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return payload["sub"]
        except ExpiredSignatureError:
            raise ValueError("Token expired")
        except JWTError:
            raise ValueError("Invalid token")
