from sqlalchemy.orm import Session
from app.database import get_db_connection
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService
from app.schemas.login_schemas import UserLogin
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserCreate, db: Session = Depends(get_db_connection)):
    
    auth_service = AuthService(db)
    try:
        return auth_service.register_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.exception("There was an error registering the user: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR0, detail="Internal server error")


@router.post("/login", status_code=status.HTTP_200_OK)
def login_user(user_data: UserLogin, db: Session = Depends(get_db_connection)):
    auth_service = AuthService(db)

    try:
        user = auth_service.authenticate_user(user_data.email, user_data.password)
        if not user:
            logger.warning(f"Your login attempt failed. Please check your credentials and try again.")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        token = auth_service.create_access_token(user.id)
        return {"access_token": token, "token_type": "bearer"}

    except ValueError as e:
        logging.exception("There was an error to authenticate the user: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logging.exception("There was an error to authenticate the user: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")