from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from typing import Annotated
from ..dependancies import SessionDep, OAuth2FormDep, TokenDep
from ...models import User
from ...schemas.user import (
    UserLogin,
    UserRegister
)
from ...schemas.token import Payload, Token
from ...crud.user import (
    get_user_by_email,
    create_user,
    authenticate_user
)
from ...security import (
    create_token,
    create_expiry
)

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/register')
def register_user(db:SessionDep, user: UserRegister):
    user_db = get_user_by_email(db, user.email)
    if user_db:
        raise HTTPException(status_code=status.HTTP_226_IM_USED, detail='User exists.')
    create_user(db, user)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content='User Registered'
    )

@router.post('/token')
def login_token(db:SessionDep, form_data: OAuth2FormDep):
    print('logging in user..')
    user_db = authenticate_user(db, form_data)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Credentials')
    
    payload = Payload(sub=str(user_db.id), exp=create_expiry(minutes=30))
    return Token(
        access_token=create_token(payload),
        token_type='bearer'
    )
    
@router.get('/dummy/')
def dummy_route(token: TokenDep):
    return {'Foo', 'Bar'}