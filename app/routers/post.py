"""
Router file for our post path operations and endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter(prefix="/posts", tags=["Posts"])


# Get Single Post Endpoint:
@router.get("/{post_id}", response_model=schemas.Post)
async def get_post(post_id: int, db_session: Session = Depends(get_db)):
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
@router.get("/", response_model=list[schemas.Post])
async def get_posts(db_session: Session = Depends(get_db)):
    """GET method endpoint that points to our posts"""
    posts = db_session.query(models.Post).all()
    return posts


# Post Creation Endpoint:
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.Post,
)
async def create_posts(
    post: schemas.CreatePost, db_session: Session = Depends(get_db)
):
    """POST method endpoint that creates our posts"""
    post = models.Post(**post.dict())
    db_session.add(post)
    db_session.commit()
    db_session.refresh(post)
    return post


# Post Deletion Endpoint:
@router.delete("/{post_id}")
async def delete_post(post_id: int, db_session: Session = Depends(get_db)):
    """Delete a post"""
    post = db_session.query(models.Post).filter(models.Post.id == post_id)
    if post.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found!"
        )

    post.delete()
    db_session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Post Update Endpoint:
@router.put("/{post_id}", response_model=schemas.Post)
async def update_post(
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
    return post_query.first()
