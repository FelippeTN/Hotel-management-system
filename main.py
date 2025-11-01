from fastapi import FastAPI
import uvicorn

from app.api.routes import bookings, guests, rooms
from app.core.config import get_settings
from app.core.database import init_db


def create_app() -> FastAPI:
    settings = get_settings()
    application = FastAPI(title=settings.app_name, debug=settings.debug)

    application.include_router(guests.router, prefix=settings.api_v1_prefix)
    application.include_router(rooms.router, prefix=settings.api_v1_prefix)
    application.include_router(bookings.router, prefix=settings.api_v1_prefix)

    @application.on_event("startup") # refactor: Criar lifespam pois esse modo esta depreciado
    def _startup() -> None:
        init_db()

    @application.get("/")
    def read_root():
        return {"message": "Hotel Management System API", "status": "online"}

    @application.get("/health", tags=["Health"])
    def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return application


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000)
