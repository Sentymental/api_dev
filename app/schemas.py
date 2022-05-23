"""
File contain all schemas used by application
"""

from datetime import datetime
from pydantic import BaseModel


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
