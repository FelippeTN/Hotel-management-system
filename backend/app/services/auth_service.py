import hashlib
import secrets

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import User
from app.repositories.auth_repository import AuthRepository
from app.schemas.auth import UserCreate, UserLogin


class AuthService:
    def __init__(self, repository: AuthRepository) -> None:
        self._repository = repository

    def register(self, db: Session, payload: UserCreate) -> User:
        existing = self._repository.get_by_email(db, payload.email)
        if existing is not None:
            raise HTTPException(status.HTTP_409_CONFLICT, detail="E-mail já cadastrado")

        if "@" not in payload.email:
            raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, detail="E-mail inválido")

        hashed_password = self._hash_password(payload.password)
        return self._repository.create(
            db,
            name=payload.name,
            email=payload.email,
            hashed_password=hashed_password,
        )

    def login(self, db: Session, credentials: UserLogin) -> tuple[str, User]:
        user = self._repository.get_by_email(db, credentials.email)
        if user is None or not self._verify_password(credentials.password, user.hashed_password):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

        updated_user = self._repository.update_last_login(db, user)
        token = secrets.token_urlsafe(32)
        return token, updated_user

    @staticmethod
    def _hash_password(password: str) -> str:
        # Simple SHA256 hashing keeps dependencies minimal; replace with a stronger algorithm when needed.
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    @classmethod
    def _verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls._hash_password(plain_password) == hashed_password
