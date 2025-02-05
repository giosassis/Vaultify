from app.database import SessionLocal
from app.models.user import User
from app.models.vault import Vault
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def seed_data(db: Session):
    existing_user = db.query(User).filter(User.email == "test@example.com").first()
    if not existing_user:
        user = User(
        email="test@example.com",
        password_hash=pwd_context.hash("password123"),
        first_name="John",
        last_name="Doe"
    )
        db.add(user)
        db.commit()
        db.refresh(user)

    passwords = [
        Vault(user_id=user.id, application_title="Amazon", encrypted_password="encrypted_pwd1", email="test@example.com"),
        Vault(user_id=user.id, application_title="Gmail", encrypted_password="encrypted_pwd2", email="test@example.com"),
    ]

    db.add_all(passwords)
    db.commit()
    print("✅ Seed concluído!")

if __name__ == "__main__":
    db = SessionLocal()
    seed_data(db)
    db.close()
