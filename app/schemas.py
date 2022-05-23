"""
File contain all schemas used by application
"""

from datetime import datetime
from pydantic import BaseModel, EmailStr


class BasePost(BaseModel):
    """
    Pydantic model for validation our Posts.
    - title: title of the post -> str
    - content: content of the post -> str
    - published: True/False (default True) -> bool
    """

    title: str
    content: str
    published: bool | None = True


class CreatePost(BasePost):
    """
    Pydantic model for validation our CreatePosts.
    It inherits from BasePost class:
    - title: title of the post -> str
    - content: content of the post -> str
    - published: True/False (default True) -> bool
    """

    pass


class UpdatePost(BasePost):
    """
    Pydantic model for validation our UpadePosts.
    It inherits from BasePost class:
    - title: title of the post -> str
    - content: content of the post -> str
    - published: True/False (default True) -> bool
    """

    pass


class Post(BasePost):
    """Class that will be responsible for our response model"""

    id: int
    created_at: datetime

    class Config:
        """Class that will help us to receive dict like response"""

        orm_mode = True


# Schemas for user:
class UserBase(BaseModel):
    """Pydantic model for validation our Users"""

    email: EmailStr
    password: str

    class Config:
        """Class that will help us to receive dict like response"""

        orm_mode = True


class UserCreate(UserBase):
    """Pydantic model for validation our Users"""

    pass


class UserOutput(BaseModel):
    """Class that will be responsible for our response model"""

    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        """Class that will help us to receive dict like response"""

        orm_mode = True


class User(UserBase):
    """Class that will be responsible for our response model"""

    id: int
    created_at: datetime
