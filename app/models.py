"""
Create our database models
"""

from database import Base
from sqlalchemy import Boolean, Column, Integer, String


class Post(Base):
    """Create our Post table"""

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, default=True)
