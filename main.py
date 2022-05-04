""" Main Script """
# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from random import randrange
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


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


# Path Operations:
@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Hello World"}  # JSON


@app.get("/posts/{post_id}")  # Path parameter
def get_post(post_id: int):
    """GET method endpoint that points to provided post ID"""
    post = find_post(post_id)
    return {"post_detail": post}


@app.get("/posts")
def get_posts():
    """GET method endpoint that points to our posts"""
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    """POST method endpoint that creates our posts"""
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 100_000)
    my_posts.append(post_dict)
    return {"data": post_dict}
