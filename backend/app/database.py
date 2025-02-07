from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from app.core.settings import settings
from dotenv import load_dotenv
import os

DATABASE_URL = settings.database_url

if not DATABASE_URL:
    raise ValueError("DATABASE_URL was not specified in configfile.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db_connection():
    db = SessionLocal()
    try:
        db.execute(text("SELECT 1")).fetchone()
        yield db 
    except SQLAlchemyError as e:
        raise ValueError("Error to connect to database" + str(e)) 
    finally:
        db.close()
    