from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Optional
from datetime import date

TEXT_FIELD = Annotated[str, Field(max_length=50)]
EMAIL_FIELD = Annotated[EmailStr, Field(max_length=50)]
DOB_FIELD = Optional[date]
PROMOTIONS_FIELD = Annotated[bool, Field(default=False)]

class UserBase(BaseModel):
    email: EMAIL_FIELD

class UserLogin(UserBase):
    password: TEXT_FIELD

class UserRegister(UserBase):
    password: TEXT_FIELD
    first_name: TEXT_FIELD
    last_name: TEXT_FIELD
    dob: DOB_FIELD
    receive_promotions: PROMOTIONS_FIELD

class UserInDB(UserBase):
    hased_password:str
    first_name: TEXT_FIELD
    last_name: TEXT_FIELD
    dob: DOB_FIELD
    receive_promotions: PROMOTIONS_FIELD

class UserOut(UserBase):
    first_name: TEXT_FIELD
    last_name: TEXT_FIELD
    dob: DOB_FIELD
    receive_promotions: PROMOTIONS_FIELD