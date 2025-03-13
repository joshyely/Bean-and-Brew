import pytest
import logging
from typing import Literal
from typing import Generator
from fastapi.testclient import TestClient
from datetime import date
from app.security import create_token, create_expiry
from app.schemas.token import Payload
from app.main import app




@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c

@pytest.fixture
def token(valid_id):
    tok = create_token(
        Payload(sub=str(valid_id), exp=create_expiry(minutes=30))
    )
    return f'Bearer {tok}'

@pytest.fixture
def valid_email():
    return 'johndoe@example.com'

@pytest.fixture
def valid_password():
    return 'Password$123'

@pytest.fixture
def valid_first_name():
    return 'John'

@pytest.fixture
def valid_last_name():
    return 'Doe'

@pytest.fixture
def valid_id():
    return 1

@pytest.fixture
def valid_dob_object():
    return date(year=2003, month=12, day=21)

@pytest.fixture
def valid_dob_string():
    return '2003-12-21'

@pytest.fixture
def valid_receive_promotions_false():
    return False

@pytest.fixture
def valid_user(
    valid_email, 
    valid_password, 
    valid_first_name, 
    valid_last_name, 
    valid_dob_object,
    valid_receive_promotions_false,
    valid_id,
):
    return {
        'email': valid_email,
        'password': valid_password,
        'first_name': valid_first_name,
        'last_name': valid_last_name,
        'dob': valid_dob_object,
        'receieve_promotions': valid_receive_promotions_false,
        'id': valid_id
    }


@pytest.hookimpl
def pytest_runtest_setup(item: pytest.Item):
    # Create stashes for debug and info logs before test is ran so they can be appended to later
    item.stash['debug_logs'] = ''
    item.stash['info_logs'] = ''

@pytest.fixture
def logger(request: pytest.FixtureRequest):
    logger = logging.getLogger(request.node.name)
    logger.setLevel('DEBUG')
    def func(msg, level: Literal['DEBUG', 'INFO'] = 'DEBUG'):
        level = level.upper()
        if level == 'DEBUG':
            logger.debug(msg)
            request.node.stash['debug_logs'] += f'\n{msg}'
        elif level == 'INFO':
            logger.info(msg)
            request.node.stash['info_logs'] += f'\n{msg}'

    return func


@pytest.fixture
def record_data(request: pytest.FixtureRequest):
    def func(expected:any, actual:any, test_data:str|list=''):
        if type(test_data) != str:
            test_data = ', '.join([str(data) for data in test_data])

        request.node.stash['test_data'] = test_data
        request.node.stash['expected'] = expected
        request.node.stash['actual'] = actual
    return func

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    return report


def pytest_csv_register_columns(columns):
    columns['description'] = lambda item, report: {'Description of test': f'{item.name}\n\nLocation: {report.fspath}\n{item.obj.__doc__}'}
    columns['test_data'] = lambda item, report: {'Test data to be used (if required)': item.stash.get('test_data', '')}
    columns['expected'] = lambda item, report: {'Expected result': item.stash.get('expected', '')}
    columns['actual'] = lambda item, report: {'Actual result': item.stash.get('actual', '')}

    def comments(item: pytest.Item, report:pytest.TestReport):
        comments_str = f'{report.outcome}'
        # If a test has failed append any debug logs to assist developer
        if report.failed:
            logs = item.stash['debug_logs']
            if logs != '':
                comments_str += f'DEBUG LOGS:\n{logs}\n'
        
        # Get info logs and check to see if there are any
        logs = item.stash['info_logs']
        if logs != '':
            comments_str += f'INFO LOGS:\n{logs}\n'

        
        # Check for error messages and appends them. Ignores assertion errors.
        if report.longreprtext and not 'AssertionError' in report.longreprtext:
            comments_str += f'\nErrors:\n{report.longrepr}'

        yield 'Comments', f'{comments_str}'

    columns['comments'] = comments