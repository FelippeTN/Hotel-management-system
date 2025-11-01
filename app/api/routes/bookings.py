from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_booking_service
from app.core.database import get_db
from app.repositories.booking_repository import BookingRepository
from app.schemas.booking import (
    BookingCreate,
    BookingRead,
    BookingTransitionResponse,
)
from app.services.booking_service import BookingService

router = APIRouter(prefix="/bookings", tags=["Bookings"])

_booking_repository = BookingRepository()


@router.post("", response_model=BookingRead, status_code=status.HTTP_201_CREATED)
def create_booking(
    payload: BookingCreate,
    db: Session = Depends(get_db),
    service: BookingService = Depends(get_booking_service),
) -> BookingRead:
    booking = service.create(db, payload)
    return BookingRead.model_validate(booking)


@router.get("", response_model=list[BookingRead])
def list_bookings(
    db: Session = Depends(get_db), limit: int = 50, offset: int = 0
) -> list[BookingRead]:
    bookings = _booking_repository.list(db, limit=limit, offset=offset)
    return [BookingRead.model_validate(booking) for booking in bookings]


@router.get("/{booking_id}", response_model=BookingRead)
def retrieve_booking(booking_id: int, db: Session = Depends(get_db)) -> BookingRead:
    booking = _booking_repository.get(db, booking_id)
    if booking is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Reserva não encontrada")
    return BookingRead.model_validate(booking)


@router.post("/{booking_id}/confirm", response_model=BookingTransitionResponse)
def confirm_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    service: BookingService = Depends(get_booking_service),
) -> BookingTransitionResponse:
    return service.confirm(db, booking_id)


@router.post("/{booking_id}/cancel", response_model=BookingTransitionResponse)
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    service: BookingService = Depends(get_booking_service),
) -> BookingTransitionResponse:
    return service.cancel(db, booking_id)


@router.post("/{booking_id}/check-in", response_model=BookingTransitionResponse)
def check_in_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    service: BookingService = Depends(get_booking_service),
) -> BookingTransitionResponse:
    return service.check_in(db, booking_id)


@router.post("/{booking_id}/check-out", response_model=BookingTransitionResponse)
def check_out_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    service: BookingService = Depends(get_booking_service),
) -> BookingTransitionResponse:
    return service.check_out(db, booking_id)
