from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.user.domain.exceptions.exceptions import (
    EmailAlreadyExistsError,
    WeakPasswordError,
)


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except EmailAlreadyExistsError as e:
            return JSONResponse(
                status_code=400,
                content={"detail": f"Email already registered: {e.email}"},
            )
        except WeakPasswordError as e:
            return JSONResponse(
                status_code=422, content={"detail": {"password_errors": e.errors}}
            )
        except Exception as e:
            # Fallback: loggear, enviar a Sentry, etc.
            return JSONResponse(
                status_code=500,
                content={
                    "detail": "Internal server error",
                    "error": str(e),
                },
            )
