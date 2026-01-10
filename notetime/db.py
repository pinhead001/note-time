from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# SQLite database path
DATABASE_URL = "sqlite:///notetime.db"

# Engine
engine = create_engine(DATABASE_URL, echo=False)

# Session factory
SessionLocal = sessionmaker(bind=engine)

# Base class for ORM models
class Base(DeclarativeBase):
    pass
