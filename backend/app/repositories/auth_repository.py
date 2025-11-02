from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import User


class AuthRepository:
    def get_by_email(self, db: Session, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return db.scalar(stmt)

    def create(self, db: Session, *, name: str, email: str, hashed_password: str) -> User:
        user = User(name=name, email=email, hashed_password=hashed_password)
        db.add(user)
        db.flush()
        db.refresh(user)
        return user

    def update_last_login(self, db: Session, user: User) -> User:
        user.last_login_at = datetime.utcnow()
        db.add(user)
        db.flush()
        db.refresh(user)
        return user