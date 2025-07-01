from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.auth.infrastructure.api import auth_routes
from app.config.database import Base, get_engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Crear una conexión con el engine
    engine = get_engine()
    async with engine.connect() as conn:  # Usamos `connect()` para obtener la conexión
        # Usar el contexto para ejecutar la creación de tablas
        await conn.run_sync(Base.metadata.create_all)
        yield


app = FastAPI(lifespan=lifespan)


app.include_router(auth_routes.router)
