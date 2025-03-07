import pytest
from datetime import date
from fastapi.security import OAuth2PasswordRequestForm
from app.crud import user
from app.models.user import User
from app.schemas.user import UserLogin, UserRegister
from app.database import db

from sqlalchemy.exc import IntegrityError


def test_create_user(temp_db):
    result = user.create_user(
        temp_db, 
        UserRegister(
            email='johndoe@example.com',
            password='Password$123',
            first_name='John',
            last_name='Doe',
            dob=date(year=2003, month=12, day=21),
            receive_promotions=False
        )
    )
    assert type(result) == User
    assert result.email == 'johndoe@example.com'

def test_create_user_exists(temp_db):
    with pytest.raises(Exception):
        user.create_user(
            temp_db, 
            UserRegister(
                email='johndoe@example.com',
                password='Password$123',
                first_name='John',
                last_name='Doe',
                dob=date(year=2003, month=12, day=21),
                receive_promotions=False
            )
        )

def test_get_user_by_id(temp_db):
    result = user.get_user_by_id(temp_db, 1)
    assert type(result) == User
    assert result.email == 'johndoe@example.com'


@pytest.mark.parametrize('invalid_id', [
    pytest.param(32, id='User with ID does not exist'),
    pytest.param('string', id='String is passed instead of integer'),
])
def test_get_user_by_id_invalid(temp_db, invalid_id):
    result = user.get_user_by_id(temp_db, invalid_id)
    assert result == None


def test_get_user_by_email(temp_db):
    result = user.get_user_by_email(temp_db, 'johndoe@example.com')
    assert type(result) == User
    assert result.first_name == 'John'


@pytest.mark.parametrize('invalid_email', [
    pytest.param('random_email@hotmail.com', id='User with email does not exist'),
    pytest.param(12, id='Wrong variable type for email is passed.'),
])
def test_get_user_by_email_invalid(temp_db, invalid_email):
    result = user.get_user_by_email(temp_db, invalid_email)
    assert result == None

def test_authenticate_user(temp_db):
    result = user.authenticate_user(
        temp_db,
        OAuth2PasswordRequestForm(username='johndoe@example.com', password='Password$123')
    )
    assert type(result) == User
    assert result.email == 'johndoe@example.com'

@pytest.mark.parametrize('email,password', [
    pytest.param('johndoe@example.com', 'Wrongpassword£124', id='Correct Email, Incorrect Password'),
    pytest.param('wrongemail@example.com', 'Password$123', id='Correct Password, Incorrect Email'),
    pytest.param('wrongemail@example.com', 'Wrongpassword£124', id='Incorrect Email and Password'),
])
def test_authenticate_invalid(temp_db, email, password):
    result = user.authenticate_user(
        temp_db,
        OAuth2PasswordRequestForm(username=email, password=password)
    )
    assert result == None

