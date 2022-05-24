from passlib.context import CryptContext

# BCrypt:
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str) -> str:
    """Function that will hash our password"""
    return pwd_context.hash(password)
