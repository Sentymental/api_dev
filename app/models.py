"""
Create our database models
"""

from database import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String
from sqlalchemy.sql.expression import text


class Post(Base):
    """
    Create our Post table
    Columns:
    - id: primary_key, unique, nullable=False
    - title: str, nullable=False
    - content: str, nullable=False
    - published: bool, nullable=False, default=True
    - created_at: timestamp, nullable=False, default=now()
    """

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class User(Base):
    """
    Create our User table in our database
    Columns:
    - id: primary_key, unique, nullable=False
    - email: str, unique, nullable=False
    - password: str, nullable=False -> hashed
    - created_at: timestamp, nullable=False, default=now()
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
