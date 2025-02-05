from pydantic import BaseModel, Field, EmailStr
from typing import Annotated
from datetime import date

TEXT_FIELD = Annotated[str, Field(max_length=50)]
EMAIL_FIELD = Annotated[EmailStr, Field(max_length=50)]

class UserBase(BaseModel):
    email: EMAIL_FIELD

class UserLogin(UserBase):
    password: TEXT_FIELD

class UserRegister(UserBase):
    password: TEXT_FIELD
    first_name: TEXT_FIELD
    last_name: TEXT_FIELD
    dob: date
    receive_promotions: Annotated[bool, Field(default=False)]

class UserInDB(UserBase):
    hased_password:str
    first_name: TEXT_FIELD
    last_name: TEXT_FIELD
    dob: date
    receive_promotions: Annotated[bool, Field(default=False)]

class UserOut(UserBase):
    first_name: TEXT_FIELD
    last_name: TEXT_FIELD
    dob: date
    receive_promotions: Annotated[bool, Field(default=False)]