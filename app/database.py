"""
Database configuration file:
- engine: engine (async version)
- SessionLocal: sessionmaker
- Base: declarative base 
"""

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Engine:
engine = create_async_engine("postgresql+asyncpg://user:password@localhost/tmp")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
