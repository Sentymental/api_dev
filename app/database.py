"""
Database configuration file:
- engine: engine (async version)
- SessionLocal: sessionmaker
- Base: declarative base
"""
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# Engine:
SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://postgres:lukas14@127.0.0.1:5433/fastapi"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency:
def get_db() -> Generator[Session, None, None]:
    """Dependency for database connection"""
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
