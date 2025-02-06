from pydantic import BaseModel, field_validator, EmailStr
from typing import Optional
from validators.user_validator import validate_email, validate_password


class VaultBase(BaseModel):
    application_title: str
    email: EmailStr
    encrypted_password: str

    @field_validator('email')
    def validate_email(cls, value):
        return validate_email(value)

    @field_validator('password')
    def validate_password(cls, value):
        return validate_password(value)


class VaultCreate(VaultBase):
    application_title: Optional[str] = None
    email: Optional[EmailStr] = None
    encrypted_password: Optional[str] = None

    @field_validator('email')
    def validate_email(cls, value):
        return validate_email(value)

    @field_validator('password')
    def validate_password(cls, value):
        return validate_password(value)


class VaultResponse(VaultBase):
    id: str
    application_title: str
    email: str
    encrypted_password: str
    user_id: str

    @field_validator('email')
    def validate_email(cls, value):
        return validate_email(value)

    @field_validator('password')
    def validate_password(cls, value):
        return validate_password(value)

    class Config:
        orm_mode = True
