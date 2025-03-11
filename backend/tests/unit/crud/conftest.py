import pytest
from app.database import Database

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