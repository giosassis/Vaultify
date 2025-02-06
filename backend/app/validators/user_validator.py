import re
from pydantic import EmailStr, ValidationError

def validate_email(email: EmailStr):
    try:
        EmailStr._validate(email)
        return email
    except ValidationError:
        raise ValueError("Invalid email format")

def validate_password(password: str):
    if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
        raise ValueError("Password must be at least 12 characters long, contain at least one uppercase letter, one lowercase letter, one number, and one special character")
    return password