from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserResponse
from passlib.context import CryptContext
from app.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self, db):
        self.user_repository = UserRepository(db) 

    def register_user(self, user_data: UserCreate) -> UserResponse:
        existing_user = self.user_repository.get_by_email(user_data.email)
        if existing_user:
            raise ValueError("User with email {user_data.email} already exists")
        
        hashed_password = pwd_context.hash(user_data.password)
        user_data_with_hashed_password = user_data.copy(update={"password": hashed_password})

        user: User = self.user_repository.create(user_data_with_hashed_password)

        return UserResponse(id=user.id, email=user.email, first_name=user.first_name, last_name=user.last_name)
