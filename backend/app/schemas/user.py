from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
from app.validators.user_validator import validate_email, validate_password


class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str

    @field_validator('email')
    def validate_email(cls, value):
        return validate_email(value)


class UserCreate(UserBase):
    password: str

    @field_validator('password')
    def validate_password(cls, value):
        return validate_password(value)


class UserUpdate(UserBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    @field_validator('email')
    def validate_email(cls, value):
        return validate_email(value)

    @field_validator('password')
    def validate_password(cls, value):
        return validate_password(value)


class UserResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
