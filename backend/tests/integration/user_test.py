import pytest

from fastapi import status



def test_get_info(client):
    login = client.post('/auth/login/', data={'username': 'johndoe@example.com', 'password': 'Password$123'})
    token = login.json().get('access_token')
    response = client.get('/user/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == status.HTTP_200_OK   

def test_get_info_no_token(client):
    response = client.get('/user/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_get_info_invalid_token(client):
    response = client.get('/user/', headers={'Authorization': f'Bearer roigjr34553oigh'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED