import jwt
from app.models.user import User
from passlib.context import CryptContext
from app.schemas.user import UserCreate, UserResponse
from app.repositories.user_repository import UserRepository
from app.core.settings import settings
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm

class AuthService:
    def __init__(self, db):
        self.user_repository = UserRepository(db)

    def register_user(self, user_data: UserCreate) -> UserResponse:
        existing_user = self.user_repository.get_by_email(user_data.email)
        if existing_user:
            raise ValueError(
                "User with email {user_data.email} already exists")

        hashed_password = pwd_context.hash(user_data.password)
        user_data_with_hashed_password = user_data.copy(update={"password": hashed_password})
        
        user: User = self.user_repository.create(user_data_with_hashed_password)
        
        return UserResponse(id=user.id, email=user.email, first_name=user.first_name, last_name=user.last_name)

    def authenticate_user(self, email: str, password: str) -> User | None:
        user = self.user_repository.get_by_email(email)
        if not user:
            raise ValueError("The user with email {email} does not exist.")

        if not pwd_context.verify(password, user.password_hash):
            raise ValueError("Wrong password.")

        return user

    def create_access_token(self, user_id: str) -> str:
        if user_id is None:
            raise ValueError("User is None. Cannot create access token.")

        expire = datetime.utcnow() + timedelta(hours=1)
        to_encode = {"sub": str(user_id), "exp": expire}
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
