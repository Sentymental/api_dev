""" Main Script """
# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from random import randrange
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, get_db
import models


app = FastAPI()

# Create our database Table
models.Post.metadata.create_all(bind=engine)


class Post(BaseModel):
    """Pydantic model for validation our Posts"""

    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts: list[dict] = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "Pizza Lover", "content": "I Like pizza", "id": 2},
]


def find_post(post_id: int):
    """Function that will loop over our posts and will look for specific ID"""
    for post in my_posts:
        if post["id"] == post_id:
            return post
        return None


def find_index_post(post_id: int):
    """Find corresponding index"""
    for i, post in enumerate(my_posts):
        if post["id"] == post_id:
            return i


# Path Operations:
@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Hello World"}  # JSON


@app.get("/posts/{post_id}")  # Path parameter
def get_post(post_id: int):
    """GET method endpoint that points to provided post ID"""

    post = find_post(post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not Found"
        )
    return {"post_detail": post}


@app.get("/posts")
def get_posts(db_session: Session = Depends(get_db)):
    """GET method endpoint that points to our posts"""
    posts = db_session.query(models.Post).all()
    return posts


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db_session: Session = Depends(get_db)):
    """POST method endpoint that creates our posts"""
    post = models.Post(**post.dict())
    db_session.add(post)
    db_session.commit()
    db_session.refresh(post)
    return post


@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    """Delete a post"""
    index = find_index_post(post_id)
    if not index:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found!"
        )
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):
    """Update post"""
    index = find_index_post(post_id)
    if not index:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found!"
        )
    post_dict = post.dict()
    post_dict["id"] = post_id
    my_posts[index] = post_dict
    return {"data": post_dict}
