from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.database import Base, get_engine
from app.auth.infrastructure.api import auth_routes
from app.user.infrastructure.api import user_routes
from app.user.infrastructure.middlewares.exception_handler import (
    ExceptionHandlingMiddleware,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    from app.user.infrastructure.models.user_model import UserModel  # noqa: F401

    # 🧪 DEBUG: Verificar que SQLAlchemy registró la tabla
    print("Tablas detectadas por SQLAlchemy:", Base.metadata.tables.keys())
    # Crear una conexión con el engine
    engine = get_engine()
    async with engine.begin() as conn:  # Usamos `connect()` para obtener la conexión
        # Usar el contexto para ejecutar la creación de tablas
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(ExceptionHandlingMiddleware)


app.include_router(auth_routes.router)
app.include_router(user_routes.router)
