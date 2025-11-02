from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
	name: str
	email: str
	password: str


class UserLogin(BaseModel):
	email: str
	password: str


class UserRead(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: int
	name: str
	email: str
	is_active: bool
	last_login_at: datetime | None


class LoginResponse(BaseModel):
	access_token: str
	token_type: str = "bearer"
	user: UserRead



