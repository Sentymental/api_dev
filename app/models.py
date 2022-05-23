"""
Create our database models
"""

from database import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String
from sqlalchemy.sql.expression import text


class Post(Base):
    """Create our Post table"""

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
