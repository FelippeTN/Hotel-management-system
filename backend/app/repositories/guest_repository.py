from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Guest
from app.schemas.guest import GuestCreate, GuestUpdate


class GuestRepository:
    def create(self, db: Session, data: GuestCreate) -> Guest:
        guest = Guest(**data.model_dump())
        db.add(guest)
        db.flush()
        db.refresh(guest)
        return guest

    def get(self, db: Session, guest_id: int) -> Guest | None:
        return db.get(Guest, guest_id)

    def get_by_email(self, db: Session, email: str) -> Guest | None:
        stmt = select(Guest).where(Guest.email == email)
        return db.scalars(stmt).first()

    def list(self, db: Session, limit: int = 50, offset: int = 0) -> Sequence[Guest]:
        stmt = select(Guest).offset(offset).limit(limit)
        return db.scalars(stmt).all()

    def update(self, db: Session, guest: Guest, data: GuestUpdate) -> Guest:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(guest, key, value)
        db.add(guest)
        db.flush()
        db.refresh(guest)
        return guest
