""" Main Script """
# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session
from database import engine, get_db

# from schemas import CreatePost, UpdatePost # change when we add folder for that
import schemas
import models


app = FastAPI()

# Create our database Table
models.Post.metadata.create_all(bind=engine)


# Path Operations:
@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Hello World"}  # JSON


# Get Single Post Endpoint:
@app.get("/posts/{post_id}")  # Path parameter
def get_post(post_id: int, db_session: Session = Depends(get_db)):
    """GET method endpoint that points to provided post ID"""
    post = (
        db_session.query(models.Post).filter(models.Post.id == post_id).first()
    )
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found!"
        )
    return post


# Get All Posts Endpoint:
@app.get("/posts")
def get_posts(db_session: Session = Depends(get_db)):
    """GET method endpoint that points to our posts"""
    posts = db_session.query(models.Post).all()
    return posts


# Post Creation Endpoint:
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(
    post: schemas.CreatePost, db_session: Session = Depends(get_db)
):
    """POST method endpoint that creates our posts"""
    post = models.Post(**post.dict())
    db_session.add(post)
    db_session.commit()
    db_session.refresh(post)
    return post


@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db_session: Session = Depends(get_db)):
    """Delete a post"""
    post = db_session.query(models.Post).filter(models.Post.id == post_id)
    if post.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found!"
        )

    post.delete()
    db_session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{post_id}")
def update_post(
    post_id: int,
    post: schemas.UpdatePost,
    db_session: Session = Depends(get_db),
):
    """Update post"""
    post_query = db_session.query(models.Post).filter(
        models.Post.id == post_id
    )
    if post_query.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found!"
        )

    post_query.update(post.dict())
    db_session.commit()
    return {"data": post_query.first()}
