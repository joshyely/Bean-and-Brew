from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

from .schemas.token import Payload
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_token(payload:Payload) -> str:
    """_Creates a JWT token on a verfified login._

    Args:
        payload (Payload): Token payload containing data to be encoded.

    Returns:
        str: Token String
    """
    payload_json = vars(payload)
    token = jwt.encode(payload_json, settings.JWT_KEY, settings.JWT_ALGORITHM)
    return token

def create_password_hash(password:str) -> str:
    """
    Hashes a plain text password input to be stored in the database
    
    Args:
        password (str): Plain text password

    Returns:
        str: Password hash
    """
    return pwd_context.hash(password)

def verify_password(password:str, hash:str) -> bool:
    """Compares a plain text password to the hashed password

    Args:
        password (str): Plain text password
        hash (str): Password hash

    Returns:
        bool: Do values match?
    """
    return pwd_context.verify(password, hash)

def create_expiry(minutes:int) -> datetime:
    """
    Args:
        minutes (int): How many minutes until the token expires

    Returns:
        datetime: Token expiry date
    """
    return datetime.now(timezone.utc) + timedelta(minutes=minutes)

