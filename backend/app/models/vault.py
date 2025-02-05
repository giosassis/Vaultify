from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from app.utils.gen_pass_id import generate_pass_id
from app.database import Base
import datetime

class Vault(Base):
    __tablename__ = "vaults"
    id = Column(String(255), primary_key=True, index=True, default=generate_pass_id)
    user_id = Column(String(255), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    application_title = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    encrypted_password = Column(Text, nullable=False)
    
    user = relationship("User", back_populates="vaults")