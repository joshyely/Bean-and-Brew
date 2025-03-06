import pytest
from datetime import date
from app.crud import user as userCrud
from app.schemas.user import UserRegister, UserLogin
from app.database import db