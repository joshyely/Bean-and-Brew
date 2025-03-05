from sqlalchemy.orm import Session
from datetime import date
from ..models import User
from ..schemas.user import UserLogin, UserRegister, UserInDB
from ..security import create_password_hash, verify_password
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
def create_user(db: Session, user: UserRegister) -> User:
    """
    Creates a new user in the database.

    Args:
        db (Session): The current database session
        user (UserRegister): Schema for registering a user
    
    Returns:
        User: User added
    """

    db_object = User(
        email=user.email,
        password_hash=create_password_hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        dob=user.dob,
        receive_promotions=user.receive_promotions,
        date_created=date.today()
    )
    db.add(db_object)
    return db_object

def get_user_by_id(db: Session, id:int) -> User|None:
    """
    Gets a user by their id.

    Args:
        db (Session): The current database session
        id (int): User's id

    Returns:
        User
    """
    return db.query(User).filter_by(id=id).first()

def get_user_by_email(db: Session, email:str) -> User|None:
    """
    Gets a user by their email.

    Args:
        db (Session): The current database session
        email (str): User's email

    Returns:
        User
    """
    return db.query(User).filter_by(email=email).first()

def authenticate_user(db: Session, user: OAuth2PasswordRequestForm) -> User|None:
    """
    Authenticates a user by checking if the given email exists and verifying the password against the password hash.

    Args:
        db (Session): The current database session
        user (UserLogin): The schema for logging in a user
    
    Returns:
        User
    """

    user_db: User = get_user_by_email(db, email=user.username)
    if not user_db:
        return None
    elif not verify_password(user.password, user_db.password_hash):
        return None
    return user_db


