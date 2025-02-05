import pytest, logging
from ...beanandbrew.log import get_logger



@pytest.mark.parametrize('name,level,expected', [
    (None, None, '<RootLogger root (DEBUG)>'),
    ('test', None, '<Logger test (DEBUG)>'),
    ('test', 'INFO', '<Logger test (INFO)>'),
    ('test', 'WARNING', '<Logger test (WARNING)>'),
    ('test', 'ERROR', '<Logger test (ERROR)>'),
])
def test_create_logger(name:str, level:str, expected):
    logger = get_logger(name) if not level else get_logger(name, level)
    assert str(logger) == expected
