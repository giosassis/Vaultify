from sqlalchemy import Column, Integer, String, DateTime, Text 
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base 
from app.utils.gen_usr_id import generate_user_id
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(String(255), primary_key=True, index=True, default=generate_user_id)
    email = Column(String(255), unique=True, index=True)
    password_hash = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    
    vaults = relationship("Vault", back_populates="user")
    