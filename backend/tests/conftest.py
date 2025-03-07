import pytest

from pytest_csv.column import _utils as pytest_csv_utils
from typing import Generator
from fastapi.testclient import TestClient
from datetime import date

import pytest_csv.column

from app.crud import user as userCrud
from app.schemas.user import UserRegister, UserLogin
from app.database import db
from app.security import create_token, create_expiry
from app.schemas.token import Payload
from app.main import app

pytest_csv.column

@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c

@pytest.fixture
def token():
    return create_token(
        Payload(sub='1', exp=create_expiry(minutes=30))
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    report = outcome.get_result()
    return report

def pytest_csv_register_columns(columns):
    def pearson_columns(item: pytest.Item, report: pytest.TestReport):
        
        doc = item.obj.__doc__ or ''
        yield 'Description of test', f'{item.name} \n{item.obj.__module__} \n{doc} \n'
        yield 'Test data to be used (if required)', f'{item.keywords}\n{item.listextrakeywords()}\n{item.from_parent()}\n{item.own_markers}'
    
    columns['pearson_columns'] = pearson_columns