from app.repositories.auth_repository import AuthRepository
from app.repositories.booking_repository import BookingRepository
from app.repositories.guest_repository import GuestRepository
from app.repositories.room_repository import RoomRepository
from app.services.auth_service import AuthService
from app.services.booking_service import BookingService


_booking_repository = BookingRepository()
_room_repository = RoomRepository()
_guest_repository = GuestRepository()
_booking_service = BookingService(
    booking_repository=_booking_repository,
    room_repository=_room_repository,
    guest_repository=_guest_repository,
)
_auth_repository = AuthRepository()
_auth_service = AuthService(repository=_auth_repository)


def get_booking_service() -> BookingService:
    return _booking_service


def get_auth_service() -> AuthService:
    return _auth_service
