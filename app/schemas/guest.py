from datetime import datetime

from pydantic import BaseModel, EmailStr


class GuestBase(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str | None = None
    document_id: str | None = None


class GuestCreate(GuestBase):
    pass


class GuestUpdate(BaseModel):
    full_name: str | None = None
    phone_number: str | None = None
    document_id: str | None = None


class GuestRead(GuestBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
