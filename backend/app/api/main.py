from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from .routes import(
    auth
)
from ..log import uvicorn_logger

api_routes = APIRouter()
api_routes.include_router(auth.router)

@api_routes.get('/foo')
def get_test(request: Request):
    """
    Test GET route for frontend which returns a JSON Response of {'foo': 'bar'}
    """
    return JSONResponse(content={'message': 'bar'})
