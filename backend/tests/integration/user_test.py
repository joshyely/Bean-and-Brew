import pytest

from fastapi import status

@pytest.fixture()
def valid_info(valid_first_name, valid_last_name, valid_email, valid_dob_string):
    return {
        'firstName': valid_first_name,
        'lastName': valid_last_name,
        'email': valid_email,
        'dob': valid_dob_string,
        'dateCreated': user.date_created,
    }

def test_get_info(client, valid_email, valid_password, token, record_data):
    """
    Test API endpoint for getting user information using a valid JWT token
    Endpoint: /user/
    """
    response = client.get('/user/', headers={'Authorization': token})
    res_json = response.json()
    record_data(
        expected={
            'status': 'HTTP 200',
            'returned email': valid_email
        },
        actual={
            'status': f'HTTP {response.status_code}',
            'returned email': returned_email 
        },
        test_data=[valid_email, valid_password, token]
    )

    assert response.status_code == status.HTTP_200_OK
    assert returned_email == valid_email  

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