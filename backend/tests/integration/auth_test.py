import pytest
from pytest import param
from fastapi import status
from fastapi.testclient import TestClient
from dataclasses import dataclass

@dataclass
class ValidUser:
    first_name='John'
    last_name='Doe'
    dob='2003-12-21'
    email='johndoe@example.com'
    password='Password$123'
    receive_promotions=False



@pytest.mark.parametrize(
    'first_name,last_name,dob,email,password,receive_promotions,expected',
    [
        param(
            None,
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='First name is empty'
        ),
        param(
            'John32',
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Invalid first name with numerical characters'
        ),
        param(
            'John$',
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Invalid first name with symbols'
        ),
        param(
            ValidUser.first_name,
            None,
            ValidUser.dob,
            ValidUser.email,
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Last name is empty'
        ),
        param(
            ValidUser.first_name,
            'Doe49',
            ValidUser.dob,
            ValidUser.email,
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Invalid last name with numerical characters'
        ),
        param(
            ValidUser.first_name,
            'Doe£',
            ValidUser.dob,
            ValidUser.email,
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Invalid last name with symbols'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            'odihwioh125',
            ValidUser.email,
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Invalid dob as random string'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            None,
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Email is empty'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            'johndoe@example',
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Invalid email without dot'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            'johndoeexample.com',
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Invalid email without @'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            '.johndoe@example.com',
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Invalid email starting with a dot'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            'johndoe@@example.com',
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Invalid email with more than one @'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            'johndoe@example..com',
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Invalid email with two dots next to each other'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            None,
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Password is empty'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            'Pa$12',
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Password is too short'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            'password$123',
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Password has no uppercase'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            'PASSWORD$123',
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Password has no lowercase'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            'password123',
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Password has no symbol'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            'password$',
            ValidUser.receive_promotions,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Password has no number'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            ValidUser.password,
            'foihwf',
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Receieve promotions is not a boolean'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            ValidUser.password,
            None,
            [status.HTTP_422_UNPROCESSABLE_ENTITY],
            id='Receieve promotions is empty'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_201_CREATED, ValidUser.email],
            id='Valid Registration'
        ),
        param(
            ValidUser.first_name,
            ValidUser.last_name,
            ValidUser.dob,
            ValidUser.email,
            ValidUser.password,
            ValidUser.receive_promotions,
            [status.HTTP_226_IM_USED],
            id='User with email already exists'
        ),
    ]
)
def test_register(
    client:TestClient, 
    first_name:str, 
    last_name:str, 
    dob:str, 
    email:str, 
    password:str, 
    receive_promotions:bool,
    expected:list
):
    """
    Registering a user
    """
    response = client.post(
        '/auth/register',
        json={
            'first_name': first_name,
            'last_name': last_name,
            'dob': dob,
            'email': email,
            'password': password,
            'receieve_promotions': receive_promotions,
        }
    )
    assert response.status_code == expected[0]
    if len(expected) > 1:
        assert response.json()['email'] == expected[1]
    