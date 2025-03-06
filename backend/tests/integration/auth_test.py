import pytest
from fastapi import status

@pytest.fixture
def register_data():
    return {
        'email': 'johndoe@example.com',
        'password': 'Password$123',
        'first_name': 'John',
        'last_name': 'Doe',
        'dob': '2002-03-06',
        'receive_promotions': False
    }

@pytest.fixture
def register_data_2():
    return {
        'email': 'lisa@example.com',
        'password': 'aPassword£123',
        'first_name': 'Lisa',
        'last_name': 'Smith',
        'dob': '1998-02-05',
        'receive_promotions': False
    }


@pytest.mark.first
def test_register(client, register_data):
    response = client.post('/auth/register/', json=register_data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.second
def test_register_existing_user(client, register_data):
    response = client.post('/auth/register/', json=register_data)
    assert response.status_code == status.HTTP_226_IM_USED


def test_register_empty_data(client):
    response = client.post('/auth/register/', json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

@pytest.mark.parametrize(
    'email',
    [
        None,
        24972,
        False,
        True,
        'lisa@example',
        'lisaexample.com',
        'lisa@@example.com',
        'lisa@example..com',
        'lisa@example.',
        '@lisa.com',
        '.lisa@example.com',
    ]
)
def test_register_invalid_email(client, register_data_2, email):
    register_data_2['email'] = email
    response = client.post('/auth/register/', json=register_data_2)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

@pytest.mark.parametrize(
    'password',
    [
        None,
        24972,
        False,
        True,
        'apassword£123',
        'APASSWORD£123',
        'aPassword123',
        'aPassword£',
        'aP£123',
    ]
)
def test_register_invalid_password(client, register_data_2, password):
    register_data_2['password'] = password
    response = client.post('/auth/register/', json=register_data_2)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

@pytest.mark.parametrize(
    'first_name,last_name',
    [
        (None, 'Smith02'),
        (12, 'Smith'),
        ('Lisa22', 'Smith'),
        ('Lisa$', 'Smith'),
        ('Lisa', None),
        ('Lisa', 24),
        ('Lisa', 'Smith02'),
        ('Lisa', 'Smith£'),
    ]
)
def test_register_invalid_names(client, register_data_2, first_name, last_name):
    register_data_2['first_name'] = first_name
    register_data_2['last_name'] = last_name
    response = client.post('/auth/register/', json=register_data_2)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

@pytest.mark.parametrize(
    'dob',
    [
        210401,
        False,
        '391kdpsk',
    ]
)
def test_register_invalid_dob(client, register_data_2, dob):
    register_data_2['dob'] = dob
    response = client.post('/auth/register/', json=register_data_2)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

@pytest.mark.parametrize(
    'receive_promotions',
    [
        'ioefheofh',
        131
    ]
)
def test_register_invalid_receive_promotions(client, register_data_2, receive_promotions):
    register_data_2['receive_promotions'] = receive_promotions
    response = client.post('/auth/register/', json=register_data_2)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY






def test_login(client):
    response = client.post('/auth/login/', json={
        'username': 'johndoe@example.com',
        'password': 'Password$123'
    })
    assert response.status_code == status.HTTP_200_OK
    res_json: dict = response.json()
    assert list(res_json.keys()) == ['access_token', 'token_type']

@pytest.mark.parametrize('username,password', [
    pytest.param('johndoe@example.com', 'Wrongpassword£124', id='Correct Email, Incorrect Password'),
    pytest.param('wrongemail@example.com', 'Password$123', id='Correct Password, Incorrect Email'),
    pytest.param('wrongemail@example.com', 'Wrongpassword£124', id='Incorrect Email and Password'),
    pytest.param(None, None, id='Fields empty'),
])
def test_login_invalid(client, username, password):
    response = client.post('/auth/login/', json={
        'username': username,
        'password': password
    })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

