from decimal import Decimal

from pydantic import BaseModel

from app.models.room import RoomStatus


class RoomBase(BaseModel):
    name: str
    description: str | None = None
    capacity: int
    daily_rate: Decimal
    status: RoomStatus = RoomStatus.AVAILABLE


class RoomCreate(RoomBase):
    pass


class RoomUpdate(BaseModel):
    description: str | None = None
    capacity: int | None = None
    daily_rate: Decimal | None = None
    status: RoomStatus | None = None


class RoomRead(RoomBase):
    id: int

    class Config:
        from_attributes = True
