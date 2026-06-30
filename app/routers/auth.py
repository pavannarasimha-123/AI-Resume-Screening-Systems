from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin, Token
from app.services.user_service import UserService

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


# ----------------------------
# Register API
# ----------------------------
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return UserService.create_user(db, user)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# ----------------------------
# Login API
# ----------------------------
@router.post(
    "/login",
    response_model=Token
)
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):
    try:
        return UserService.login_user(
            db,
            credentials.email,
            credentials.password
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )