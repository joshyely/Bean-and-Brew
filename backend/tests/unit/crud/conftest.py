import pytest
from app.database import Database
from app.crud import user as userCrud
from app.schemas.user import UserRegister

test_db = Database('sqlite+pysqlite:///:memory:')

@pytest.fixture
def temp_db():
    """
    Create a new session from an in memory sqlite database to be used for testing the CRUD.

    Yields:
        _Generator[sqlalchemy.orm.Session, None, None]_: _Session Generator Object_
    """
    with test_db.Session.begin() as session:
        yield session

@pytest.fixture
def user_session(temp_db, valid_user:dict):
    valid_user.pop('id')
    userCrud.create_user(temp_db, UserRegister(**valid_user))
    return temp_db