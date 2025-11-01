from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.room_repository import RoomRepository
from app.schemas.room import RoomCreate, RoomRead, RoomUpdate

router = APIRouter(prefix="/rooms", tags=["Rooms"])

_room_repository = RoomRepository()


@router.post("", response_model=RoomRead, status_code=status.HTTP_201_CREATED)
def create_room(payload: RoomCreate, db: Session = Depends(get_db)) -> RoomRead:
    if payload.capacity <= 0:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Capacidade deve ser maior que zero")
    if payload.daily_rate < 0:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Valor da diária inválido")
    existing = _room_repository.get_by_name(db, payload.name)
    if existing:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Quarto com esse nome já existe")
    room = _room_repository.create(db, payload)
    return RoomRead.model_validate(room)


@router.get("", response_model=list[RoomRead])
def list_rooms(db: Session = Depends(get_db), limit: int = 50, offset: int = 0) -> list[RoomRead]:
    rooms = _room_repository.list(db, limit=limit, offset=offset)
    return [RoomRead.model_validate(room) for room in rooms]


@router.get("/{room_id}", response_model=RoomRead)
def retrieve_room(room_id: int, db: Session = Depends(get_db)) -> RoomRead:
    room = _room_repository.get(db, room_id)
    if room is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Quarto não encontrado")
    return RoomRead.model_validate(room)


@router.patch("/{room_id}", response_model=RoomRead)
def update_room(room_id: int, payload: RoomUpdate, db: Session = Depends(get_db)) -> RoomRead:
    room = _room_repository.get(db, room_id)
    if room is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Quarto não encontrado")
    if payload.capacity is not None and payload.capacity <= 0:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Capacidade deve ser maior que zero")
    if payload.daily_rate is not None and payload.daily_rate < 0:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Valor da diária inválido")
    room = _room_repository.update(db, room, payload)
    return RoomRead.model_validate(room)
