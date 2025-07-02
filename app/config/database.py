from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime, timezone
from app.config.settings import settings  # 👈 importa tu instancia de configuración


# Declarative base moderna (para usar Mapped y mapped_column)
class Base(DeclarativeBase):
    __abstract__ = True  # Evita que se cree una tabla "base"

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now(tz=timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(tz=timezone.utc),
        onupdate=datetime.now(tz=timezone.utc),
    )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id})>"


def get_database_url() -> str:
    # Reemplaza el driver sync por async
    return settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")


def get_engine():
    return create_async_engine(get_database_url(), echo=True)


def get_session_maker(engine=None):
    if engine is None:
        engine = get_engine()
    return async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db() -> AsyncSession:  # type: ignore
    SessionLocal = get_session_maker()
    async with SessionLocal() as session:
        yield session
