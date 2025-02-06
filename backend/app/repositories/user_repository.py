from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.gen_usr_id import generate_user_id
from app.core.security import hash_password
from datetime import datetime


def get_current_utc_time():
    return datetime.utcnow()

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[User]:
        return self.db.query(User).all()

    def get_by_id(self, user_id: str) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user_data: UserCreate) -> User:
        try:
            new_user = User(
                id=generate_user_id(),
                email=user_data.email,
                password_hash=hash_password(user_data.password),
                first_name=user_data.first_name,
                last_name=user_data.last_name,
                created_at=get_current_utc_time()
            )
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return new_user
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"There was an error creating the user: {str(e)}")

    def update(self, user_id: str, updated_data: UserUpdate) -> User:
        user = self.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found. Cannot update.")

        for key, value in updated_data.dict(exclude_unset=True).items():
            setattr(user, key, value)

        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()
