from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import JSONResponse

from contextlib import asynccontextmanager

from fastapi.staticfiles import StaticFiles

from .config import settings
from . import database
from .api import api_routes
from .log import uvicorn_logger



app = FastAPI(name=settings.PROJECT_NAME)
app.include_router(api_routes)
app.mount('/', StaticFiles(directory='app/static', html=True), name='static')


origins = ['http://localhost:8080/']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/')
def test_page():
    """
    API Home page which provides links to documentation and tests a fetch request.
    Route already linked to static files so return value is not needed.
    """
    return











