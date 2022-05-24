"""
Router file for our authenthication path operations and endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
import utils


router = APIRouter(tags=["Authentication"])


@router.post("/login")
async def login(
    user_credentials: schemas.UserLogin, db_session: Session = Depends(get_db)
):
    """Login Endpoint"""
    user = (
        db_session.query(models.User)
        .filter(models.User.email == user_credentials.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials"
        )

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials"
        )

    return user
