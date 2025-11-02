import os
from dataclasses import dataclass
from functools import lru_cache


@dataclass
class Settings:
    app_name: str = "Pousada Manager API"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://postgres:1234@localhost:5432/pousada_db",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
