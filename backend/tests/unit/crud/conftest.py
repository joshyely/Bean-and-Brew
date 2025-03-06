import pytest
from app.database import Database

test_db = Database('sqlite+pysqlite:///:memory:')

@pytest.fixture
def temp_db():
    with test_db.Session.begin() as session:
        yield session