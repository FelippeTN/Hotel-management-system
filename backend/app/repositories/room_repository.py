from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Room
from app.schemas.room import RoomCreate, RoomUpdate


class RoomRepository:
    def create(self, db: Session, data: RoomCreate) -> Room:
        room = Room(**data.model_dump())
        db.add(room)
        db.flush()
        db.refresh(room)
        return room

    def get(self, db: Session, room_id: int) -> Room | None:
        return db.get(Room, room_id)

    def get_by_name(self, db: Session, name: str) -> Room | None:
        stmt = select(Room).where(Room.name == name)
        return db.scalars(stmt).first()

    def list(self, db: Session, limit: int = 50, offset: int = 0) -> Sequence[Room]:
        stmt = select(Room).offset(offset).limit(limit)
        return db.scalars(stmt).all()

    def update(self, db: Session, room: Room, data: RoomUpdate) -> Room:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(room, key, value)
        db.add(room)
        db.flush()
        db.refresh(room)
        return room
