from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_auth_service
from app.core.database import get_db
from app.schemas.auth import LoginResponse, UserCreate, UserLogin, UserRead
from app.services.auth_service import AuthService


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register_user(
	payload: UserCreate,
	db: Session = Depends(get_db),
	service: AuthService = Depends(get_auth_service),
) -> UserRead:
	user = service.register(db, payload)
	return UserRead.model_validate(user)


@router.post("/login", response_model=LoginResponse)
def login_user(
	credentials: UserLogin,
	db: Session = Depends(get_db),
	service: AuthService = Depends(get_auth_service),
) -> LoginResponse:
	token, user = service.login(db, credentials)
	return LoginResponse(access_token=token, user=UserRead.model_validate(user))

