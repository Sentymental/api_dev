""" Main Script """
# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument


from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    """Pydantic model for validation our Posts"""

    title: str
    content: str
    published: bool = True


# Path Operations:
@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Hello World"}  # JSON


@app.get("/posts")
def get_posts():
    """GET method endpoint that points to our posts"""
    return {"data": "This is your posts"}


@app.post("/createpost")
def create_posts(post: Post):
    """POST method endpoint that creates our posts"""
    return {"title": post.title, "content": post.content, "published": post.published}
