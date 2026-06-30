from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password, verify_password
from app.core.security import create_access_token


class UserService:

    @staticmethod
    def create_user(db: Session, user: UserCreate):

        existing_user = db.scalar(
            select(User).where(User.email == user.email)
        )

        if existing_user:
            raise ValueError("Email already registered")

        new_user = User(
            full_name=user.full_name,
            email=user.email,
            password_hash=hash_password(user.password)
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def login_user(db: Session, email: str, password: str):

        user = db.scalar(
            select(User).where(User.email == email)
        )

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(password, user.password_hash):
            raise ValueError("Invalid email or password")

        token = create_access_token(
            {
                "sub": user.email,
                "role": user.role
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }