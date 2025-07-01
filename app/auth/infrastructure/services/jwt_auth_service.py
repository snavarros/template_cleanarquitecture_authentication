from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt

from app.config import settings


class AuthServiceJWT:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain: str, hashed: str) -> bool:
        return self.pwd_context.verify(plain, hashed)

    def create_token(self, email: str) -> str:
        payload = {
            "sub": email,
            "exp": datetime.utcnow() + timedelta(minutes=30),
        }

        return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
