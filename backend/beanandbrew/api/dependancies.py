import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import status, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated, Generator
from sqlalchemy.orm import Session

from ..schemas.token import Payload
from ..config import settings
from ..database import db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/auth/token')

def verify_token(token:Annotated[str, Depends(oauth2_scheme)]) -> Payload:
    """_Uses JWT to verfify the token's signature using the a saved jwt key_
    
    Args:
        token (Annotated[str, Depends]): _Token string from request header_
    
    Raises:
        HTTPException: Raises 401 UNAUTHORIZED if the token's signature is invalid.

    Returns:
        `backend.ravenborn.schemas.token.Payload`: _Payload containing token data_
    """
    try:
        payload_dict = jwt.decode(token, key=settings.JWT_KEY, algorithms=[settings.JWT_ALGORITHM])
    except InvalidTokenError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Bad Token', headers={"WWW-Authenticate": "Bearer"},)
    return Payload(**payload_dict)

def get_db() -> Generator[Session, None, None]:
    """
    Creates a new database session for the api endpoint.

    Returns:
        Generator[Session, None, None]
    """
    with db.Session.begin() as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[Session, Depends(verify_token)]
OAuth2FormDep = Annotated[OAuth2PasswordRequestForm, Depends()]