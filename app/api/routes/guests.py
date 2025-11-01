from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.guest_repository import GuestRepository
from app.schemas.guest import GuestCreate, GuestRead, GuestUpdate

router = APIRouter(prefix="/guests", tags=["Guests"])

_guest_repository = GuestRepository()


@router.post("", response_model=GuestRead, status_code=status.HTTP_201_CREATED)
def create_guest(payload: GuestCreate, db: Session = Depends(get_db)) -> GuestRead:
    existing = _guest_repository.get_by_email(db, payload.email)
    if existing:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="E-mail já cadastrado")
    guest = _guest_repository.create(db, payload)
    return GuestRead.model_validate(guest)


@router.get("", response_model=list[GuestRead])
def list_guests(db: Session = Depends(get_db), limit: int = 50, offset: int = 0) -> list[GuestRead]:
    guests = _guest_repository.list(db, limit=limit, offset=offset)
    return [GuestRead.model_validate(guest) for guest in guests]


@router.patch("/{guest_id}", response_model=GuestRead)
def update_guest(guest_id: int, payload: GuestUpdate, db: Session = Depends(get_db)) -> GuestRead:
    guest = _guest_repository.get(db, guest_id)
    if guest is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Hóspede não encontrado")
    guest = _guest_repository.update(db, guest, payload)
    return GuestRead.model_validate(guest)
