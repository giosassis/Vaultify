from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService
from app.database import get_db_connection
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user_data: UserCreate, db: Session = Depends(get_db_connection)):
    auth_service = AuthService(db)
    try:
        return auth_service.register_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
