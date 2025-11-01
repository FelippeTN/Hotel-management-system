from collections.abc import Sequence
from datetime import date
from decimal import Decimal

from sqlalchemy import Select, select
from sqlalchemy.orm import Session

from app.models import Booking, BookingStatus
from app.schemas.booking import BookingCreate, BookingUpdate


class BookingRepository:
    def create(self, db: Session, data: BookingCreate, total_amount: Decimal) -> Booking:
        payload = data.model_dump()
        payload["total_amount"] = total_amount
        booking = Booking(**payload)
        db.add(booking)
        db.flush()
        db.refresh(booking)
        return booking

    def get(self, db: Session, booking_id: int) -> Booking | None:
        return db.get(Booking, booking_id)

    def list(self, db: Session, limit: int = 50, offset: int = 0) -> Sequence[Booking]:
        stmt = select(Booking).offset(offset).limit(limit).order_by(Booking.created_at.desc())
        return db.scalars(stmt).all()

    def update(self, db: Session, booking: Booking, data: BookingUpdate) -> Booking:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(booking, key, value)
        db.add(booking)
        db.flush()
        db.refresh(booking)
        return booking

    def save(self, db: Session, booking: Booking) -> Booking:
        db.add(booking)
        db.flush()
        db.refresh(booking)
        return booking

    def _active_overlap_query(
        self,
        room_id: int,
        check_in: date,
        check_out: date,
    ) -> Select[tuple[int]]:
        return (
            select(Booking.id)
            .where(Booking.room_id == room_id)
            .where(Booking.status != BookingStatus.CANCELLED)
            .where(Booking.check_out > check_in)
            .where(Booking.check_in < check_out)
        )

    def count_active_overlaps(
        self,
        db: Session,
        room_id: int,
        check_in: date,
        check_out: date,
    ) -> int:
        stmt = self._active_overlap_query(room_id, check_in, check_out)
        return len(db.scalars(stmt).all())
