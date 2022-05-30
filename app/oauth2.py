"""
OAUTH2 implementiation of the login system
"""

from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import JWTError, jwt
from passwords import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict):
    """Create access token"""
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    """Verify provided access token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_id = payload.get("users_id")

        if user_id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=user_id)

    except JWTError:
        raise credentials_exception


def get_current_user(token: str = Depends(oauth2_scheme)):
    """Get current user token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not valid credentials!",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_access_token(
        token=token, credentials_exception=credentials_exception
    )
