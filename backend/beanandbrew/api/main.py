from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from .routes import(
    auth
)
from ..log import uvicorn_logger

api_routes = APIRouter(prefix='/api')
api_routes.include_router(auth.router)

@api_routes.get('/foobar')
def get_foobar(request: Request):
    """
    Test route which returns a JSON Response of {'foo': 'bar'}
    """
    uvicorn_logger.debug(request.headers)
    return JSONResponse(content={'foo': 'bar'})