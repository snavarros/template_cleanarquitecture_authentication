from sqlalchemy import Column, Integer, String
from app.config.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)
    role = Column(String)
