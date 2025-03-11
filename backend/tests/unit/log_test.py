import pytest, logging
from pytest import param
from app.log import get_logger



@pytest.mark.parametrize('name,level,expected', [
    param(None, None, '<RootLogger root (DEBUG)>', id='Creating a root logger with no name or level set'),
    param('test', None, '<Logger test (DEBUG)>', id='Creating a logger named "test"'),
    param('test', 'INFO', '<Logger test (INFO)>', id='Creating a logger named "test" with the level set to INFO'),
    param('test', 'WARNING', '<Logger test (WARNING)>', id='Creating a logger named "test" with the level set to WARNING'),
    param('test', 'ERROR', '<Logger test (ERROR)>', id='Creating a logger named "test" with the level set to ERROR'),
])
def test_create_logger(name:str, level:str, expected:str, record_data):
    """
    Test creating a new logger.
    """

    logger = get_logger(name) if not level else get_logger(name, level)
    actual = str(logger)
    
    record_data(
        expected,
        actual,
        test_data=[name, level]
    )
    assert actual == expected
