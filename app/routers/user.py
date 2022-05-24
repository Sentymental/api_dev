"""
Router file for our user path operations and endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
import utils

router = APIRouter(prefix="/users", tags=["User"])


# Get User by ID:
@router.get("/{user_id}", response_model=schemas.UserOutput)
async def get_user(user_id: int, db_session: Session = Depends(get_db)):
    """GET method endpoint that points to our user by ID"""
    user = (
        db_session.query(models.User).filter(models.User.id == user_id).first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"UserID: {user_id} not found!",
        )
    return user


# Get All Users Endpoint:
@router.get("/", response_model=list[schemas.UserOutput])
async def get_users(db_session: Session = Depends(get_db)):
    """GET method endpoint that points to our users"""

    users = db_session.query(models.User).all()
    return users


# Create User Endpoint:
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserOutput,
)
async def create_user(
    user: schemas.UserCreate, db_session: Session = Depends(get_db)
):
    """POST method endpoint that creates our users"""

    hashed_password = utils.hash_pw(user.password)
    user.password = hashed_password

    user = models.User(**user.dict())
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    return user
