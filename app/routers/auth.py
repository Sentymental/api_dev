"""
Router file for our authenthication path operations and endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
import models
import utils
import oauth2


router = APIRouter(tags=["Authentication"])


@router.post("/login")
async def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db_session: Session = Depends(get_db),
):
    """Login Endpoint"""
    user = (
        db_session.query(models.User)
        .filter(models.User.email == user_credentials.username)
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

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
