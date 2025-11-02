from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings


_SETTINGS = get_settings()

_CONNECT_ARGS: dict[str, object] = {}
if _SETTINGS.database_url.startswith("sqlite"):
    _CONNECT_ARGS["check_same_thread"] = False

engine: Engine = create_engine(
    _SETTINGS.database_url,
    echo=_SETTINGS.debug,
    future=True,
    connect_args=_CONNECT_ARGS,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise
    finally:
        db.close()


def init_db() -> None:
    from app.models.base import Base

    Base.metadata.create_all(bind=engine)
