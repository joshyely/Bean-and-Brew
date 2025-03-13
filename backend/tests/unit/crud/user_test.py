import pytest
from datetime import date
from fastapi.security import OAuth2PasswordRequestForm
from app.crud import user as userCrud
from app.models.user import User
from app.schemas.user import UserLogin, UserRegister
from app.database import db
from sqlalchemy.exc import IntegrityError
import sqlite3


def test_create_user(temp_db, valid_user:dict, record_data, logger):
    """
    Test creating a new user through the crud.
    """
    valid_user.pop('id')
    user = UserRegister(
        **valid_user
    )
    logger(f'User class: {user}')

    result = userCrud.create_user(
        temp_db, 
        user
    )
    actual = f'type(result) == {type(result)} ' 
    if result != None:
        actual += f'\nAND\n result.email == {result.email}'

    record_data(
        expected=f'type(result) == User \nAND\n result.email == {valid_user["email"]}',
        actual=actual,
        test_data=['memory db session', valid_user]
    )

    assert type(result) == User
    assert result.email == valid_user['email']

def test_create_user_exists(temp_db, valid_user:dict, record_data):
    """
    Test attemping to create a new user with an email that already exists.
    """
    valid_user.pop('id')
    result = userCrud.create_user(
        temp_db, 
        UserRegister(
            **valid_user
        )
    )
    
    record_data(
        expected='None',
        actual=f'{result}',
        test_data=['memory db session', valid_user]
    )
    assert result == None

def test_get_user_by_id(temp_db, valid_id:int, valid_email:str, record_data):
    """
    Test getting a user from the crud using their id.
    """
    result = userCrud.get_user_by_id(temp_db, valid_id)
    
    actual = f'type(result) == {type(result)} ' 
    if result != None:
        actual += f'\nAND\n result.email == {result.email}'

    record_data(
        expected=f'type(result) == User \nAND\n result.email == {valid_email}',
        actual=actual,
        test_data=[f'memory db session', f'user id: {valid_id}']
    )
    assert type(result) == User
    assert result.email == valid_email


@pytest.mark.parametrize('invalid_id', [
    pytest.param(32, id='User with ID does not exist'),
    pytest.param('string', id='String is passed instead of integer'),
])
def test_get_user_by_id_invalid(temp_db, invalid_id, record_data):
    """
    Test to ensure the crud returns None when an invalid user id is entered when trying to retrieve a user.
    """
    result = userCrud.get_user_by_id(temp_db, invalid_id)
    record_data(
        expected='None',
        actual=f'{result}',
        test_data=[f'memory db session', f'invalid user id: {invalid_id}']
    )
    assert result == None


def test_get_user_by_email(temp_db, valid_email:str, record_data):
    """
    Test getting a user from the crud using their email.
    """
    result = userCrud.get_user_by_email(temp_db, valid_email)

    actual = f'type(result) == {type(result)} ' 
    if result != None:
        actual += f'\nAND\n result.email == {result.email}'

    record_data(
        expected=f'type(result) == User \nAND\n result.email == {valid_email}',
        actual=actual,
        test_data=[f'memory db session', f'email: {valid_email}']
    )

    assert type(result) == User
    assert result.email == valid_email


@pytest.mark.parametrize('invalid_email', [
    pytest.param('random_email@hotmail.com', id='User with email does not exist'),
    pytest.param(12, id='Wrong variable type for email is passed.'),
])
def test_get_user_by_email_invalid(temp_db, invalid_email, record_data):
    """
    Test to ensure the crud returns None when an invalid user email is entered when trying to retrieve a user.
    """
    result = userCrud.get_user_by_email(temp_db, invalid_email)
    record_data(
        expected='None',
        actual=f'{result}',
        test_data=[f'memory db session', f'invalid email: {invalid_email}']
    )
    assert result == None


def test_authenticate_user(temp_db, valid_email:str, valid_password:str, record_data):
    """
    Test authenticating a user with the correct credentials.
    """
    result = userCrud.authenticate_user(
        temp_db,
        OAuth2PasswordRequestForm(username=valid_email, password=valid_password)
    )

    actual = f'type(result) == {type(result)} ' 
    if result != None:
        actual += f'\nAND\n result.email == {result.email}'

    record_data(
        expected=f'type(result) == User \nAND\n result.email == {valid_email}',
        actual=actual,
        test_data=[f'memory db session', f'email: {valid_email}', f'password: {valid_password}']
    )

    assert type(result) == User
    assert result.email == valid_email


@pytest.mark.parametrize('email,password', [
    pytest.param('johndoe@example.com', 'Wrongpassword£124', id='Correct Email, Incorrect Password'),
    pytest.param('wrongemail@example.com', 'Password$123', id='Correct Password, Incorrect Email'),
    pytest.param('wrongemail@example.com', 'Wrongpassword£124', id='Incorrect Email and Password'),
])
def test_authenticate_invalid(temp_db, email:str, password:str, record_data):
    """
    Test the user authentication function with invalid credentials.
    """
    result = userCrud.authenticate_user(
        temp_db,
        OAuth2PasswordRequestForm(username=email, password=password)
    )
    record_data(
        expected=None,
        actual=result,
        test_data=[f'memory db session', f'email: {email}', f'password: {password}']
    )
    assert result == None

