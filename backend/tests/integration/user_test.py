import pytest

from fastapi import status



def test_get_info(client, valid_email, valid_password, token, record_data, logger):
    """
    Test API endpoint for getting user information using a valid JWT token
    Endpoint: /user/
    """
    # # Get JWT token from login endpoint
    # login = client.post('/auth/login/', data={'username': valid_email, 'password': valid_password})
    # token = login.json().get('access_token')
    # logger(f'Login response code: {login.status_code}')

    # Test user endpoint with valid token
    response = client.get('/user/', headers={'Authorization': token})

    record_data(
        expected='HTTP 200',
        actual=f'HTTP {response.status_code}',
        test_data=[valid_email, valid_password, token]
    )

    assert response.status_code == status.HTTP_200_OK   

def test_get_info_no_token(client, record_data):
    """
    Test API endpoint for getting user information with no token
    Endpoint: /user/
    """
    response = client.get('/user/')
    record_data(
        expected='HTTP 401',
        actual=f'HTTP {response.status_code}'
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_get_info_invalid_token(client, record_data):
    """
    Test API endpoint for getting user information with an invalid token
    Endpoint: /user/
    """
    response = client.get('/user/', headers={'Authorization': 'Bearer roigjr34553oigh'})
    record_data(
        expected='HTTP 401',
        actual=f'HTTP {response.status_code}',
        test_data=['Bearer roigjr34553oigh']
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED