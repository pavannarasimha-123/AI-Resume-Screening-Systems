from pydantic import BaseModel, EmailStr, Field


# -------------------------
# Register Request
# -------------------------
class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)


# -------------------------
# Register Response
# -------------------------
class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: str
    is_active: bool

    class Config:
        from_attributes = True


# -------------------------
# Login Request
# -------------------------
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# -------------------------
# Login Response
# -------------------------
class Token(BaseModel):
    access_token: str
    token_type: str