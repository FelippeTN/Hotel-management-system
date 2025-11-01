from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import Booking, BookingStatus, RoomStatus
from app.repositories.booking_repository import BookingRepository
from app.repositories.guest_repository import GuestRepository
from app.repositories.room_repository import RoomRepository
from app.schemas.booking import BookingCreate, BookingTransitionResponse


class BookingService:
    def __init__(
        self,
        booking_repository: BookingRepository,
        room_repository: RoomRepository,
        guest_repository: GuestRepository,
    ) -> None:
        self._booking_repository = booking_repository
        self._room_repository = room_repository
        self._guest_repository = guest_repository

    def create(self, db: Session, payload: BookingCreate) -> Booking:
        room = self._room_repository.get(db, payload.room_id)
        if room is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Quarto não encontrado")

        guest = self._guest_repository.get(db, payload.guest_id)
        if guest is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Hóspede não encontrado")

        if payload.guests_count <= 0:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Quantidade de hóspedes inválida")

        if room.capacity < payload.guests_count:
            raise HTTPException(
                status.HTTP_409_CONFLICT,
                detail="Capacidade do quarto excedida",
            )

        if room.status != RoomStatus.AVAILABLE:
            raise HTTPException(
                status.HTTP_409_CONFLICT,
                detail="Quarto indisponível para novas reservas",
            )

        if payload.check_in >= payload.check_out:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail="Data de check-out deve ser posterior ao check-in",
            )

        overlap_count = self._booking_repository.count_active_overlaps(
            db=db,
            room_id=room.id,
            check_in=payload.check_in,
            check_out=payload.check_out,
        )
        if overlap_count:
            raise HTTPException(
                status.HTTP_409_CONFLICT,
                detail="Já existe uma reserva ativa no período selecionado",
            )

        total_amount = self._calculate_total_amount(room.daily_rate, payload.check_in, payload.check_out)
        return self._booking_repository.create(db, payload, total_amount=total_amount)

    def confirm(self, db: Session, booking_id: int) -> BookingTransitionResponse:
        booking = self._require_booking(db, booking_id)

        if booking.status == BookingStatus.CANCELLED:
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Reserva cancelada não pode ser confirmada")
        if booking.status == BookingStatus.CONFIRMED:
            return BookingTransitionResponse(
                id=booking.id,
                status=booking.status,
                reference_code=booking.reference_code,
                message="Reserva já confirmada",
            )
        if booking.status != BookingStatus.CREATED:
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Reserva já processada")

        now = datetime.utcnow()
        booking.status = BookingStatus.CONFIRMED
        booking.confirmed_at = now
        self._booking_repository.save(db, booking)
        return BookingTransitionResponse(
            id=booking.id,
            status=booking.status,
            reference_code=booking.reference_code,
            message="Reserva confirmada com sucesso",
        )

    def cancel(self, db: Session, booking_id: int) -> BookingTransitionResponse:
        booking = self._require_booking(db, booking_id)

        if booking.status == BookingStatus.CANCELLED:
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Reserva já cancelada")
        if booking.status == BookingStatus.CHECKED_OUT:
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Reserva já finalizada")

        booking.status = BookingStatus.CANCELLED
        booking.confirmed_at = None
        booking.checked_in_at = None
        booking.checked_out_at = None
        self._booking_repository.save(db, booking)
        return BookingTransitionResponse(
            id=booking.id,
            status=booking.status,
            reference_code=booking.reference_code,
            message="Reserva cancelada",
        )

    def check_in(self, db: Session, booking_id: int, today: date | None = None) -> BookingTransitionResponse:
        booking = self._require_booking(db, booking_id)

        if booking.status != BookingStatus.CONFIRMED:
            if booking.status == BookingStatus.CHECKED_IN:
                return BookingTransitionResponse(
                    id=booking.id,
                    status=booking.status,
                    reference_code=booking.reference_code,
                    message="Check-in já realizado",
                )
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Check-in disponível apenas para reservas confirmadas")

        today = today or date.today()
        if today < booking.check_in:
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Check-in não permitido antes da data prevista")
        if today > booking.check_out:
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Check-in não permitido após a data de check-out")

        booking.status = BookingStatus.CHECKED_IN
        booking.checked_in_at = datetime.utcnow()
        self._booking_repository.save(db, booking)
        return BookingTransitionResponse(
            id=booking.id,
            status=booking.status,
            reference_code=booking.reference_code,
            message="Check-in realizado",
        )

    def check_out(self, db: Session, booking_id: int, today: date | None = None) -> BookingTransitionResponse:
        booking = self._require_booking(db, booking_id)

        if booking.status != BookingStatus.CHECKED_IN:
            if booking.status == BookingStatus.CHECKED_OUT:
                return BookingTransitionResponse(
                    id=booking.id,
                    status=booking.status,
                    reference_code=booking.reference_code,
                    message="Check-out já finalizado",
                )
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Check-out permitido apenas após check-in")

        today = today or date.today()
        if today < booking.check_in:
            raise HTTPException(status.HTTP_409_CONFLICT, detail="Check-out não permitido antes do período de estadia")

        booking.status = BookingStatus.CHECKED_OUT
        booking.checked_out_at = datetime.utcnow()
        self._booking_repository.save(db, booking)
        return BookingTransitionResponse(
            id=booking.id,
            status=booking.status,
            reference_code=booking.reference_code,
            message="Check-out finalizado",
        )

    def _require_booking(self, db: Session, booking_id: int) -> Booking:
        booking = self._booking_repository.get(db, booking_id)
        if booking is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Reserva não encontrada")
        return booking

    @staticmethod
    def _calculate_total_amount(
        daily_rate: Decimal | float | int,
        check_in: date,
        check_out: date,
    ) -> Decimal:
        nights = (check_out - check_in).days
        if nights <= 0:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Período de estadia inválido")
        rate = daily_rate if isinstance(daily_rate, Decimal) else Decimal(str(daily_rate))
        return (rate * Decimal(nights)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
