from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel

from app.models.booking import BookingStatus


class BookingBase(BaseModel):
    guest_id: int
    room_id: int
    check_in: date
    check_out: date
    guests_count: int
    notes: str | None = None


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BaseModel):
    notes: str | None = None


class BookingRead(BookingBase):
    id: int
    reference_code: str
    status: BookingStatus
    total_amount: Decimal
    created_at: datetime
    updated_at: datetime
    confirmed_at: datetime | None
    checked_in_at: datetime | None
    checked_out_at: datetime | None

    class Config:
        from_attributes = True


class BookingTransitionResponse(BaseModel):
    id: int
    status: BookingStatus
    reference_code: str
    message: str

    class Config:
        from_attributes = True
