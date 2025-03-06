from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..dependancies import (
    TokenDep, 
    SessionDep
)
from ...crud import user as userCrud


router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.get('/')
def get_info(db: SessionDep, payload: TokenDep):
    user = userCrud.get_user_by_id(db, payload.sub)
    return JSONResponse(
        status_code=200, content={'user': {
            'firstName': user.first_name,
            'lastName': user.last_name,
            'email': user.email,
            'dob': user.dob,
            'dateCreated': user.date_created,
        }
    })
