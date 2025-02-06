from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.orm import relationship
import datetime
from .base import Base
class User(Base):
    __tablename__ = "users"
    id = Column(String(255), primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password_hash = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)

    # Importação da classe Vault na hora do relacionamento
    def __init__(self, *args, **kwargs):
        from app.models.vault import Vault  # Importação tardia
        self.vaults = relationship("Vault", back_populates="user", cascade="all, delete-orphan")
        super().__init__(*args, **kwargs)
