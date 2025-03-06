import pytest
from typing import Generator
from fastapi.testclient import TestClient

from app.security import create_token, create_expiry

from app.schemas.token import Payload
from app.api.dependancies import get_db
from app.main import app



@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture
def token():
    return create_token(
        Payload(sub='1', exp=create_expiry(minutes=30))
    )



def user_id():
    return '1'



