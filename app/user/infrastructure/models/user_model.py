from sqlalchemy import Boolean, Column, Integer, String
from app.config.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    phone = Column(String)
    region = Column(Integer)
    role = Column(String)
    is_active = Column(Boolean, default=True)
    provider = Column(String)
