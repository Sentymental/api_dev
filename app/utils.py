"""
Utils file will contain our utilities
"""

from passlib.context import CryptContext

# BCrypt:
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_pw(password: str) -> str:
    """Function that will hash our password"""
    return pwd_context.hash(password)


def verify(password: str, hashed_password: str) -> bool:
    """Verify if hashed passwords match"""
    return pwd_context.verify(password, hashed_password)
