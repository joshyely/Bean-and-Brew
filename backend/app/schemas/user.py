from pydantic import BaseModel, Field, EmailStr, field_validator
import re 
from typing import Annotated, Optional
from datetime import date

TEXT_FIELD = Annotated[str, Field(max_length=50)]
NAME_FIELD = Annotated[str, Field(max_length=50, pattern='^[a-zA-Z]+$')]
EMAIL_FIELD = Annotated[EmailStr, Field(max_length=50)]
PASSWORD_FIELD = Annotated[str, Field(min_length=8, max_length=50)]
DOB_FIELD = Optional[date]
PROMOTIONS_FIELD = Annotated[bool, Field(default=False)]

class UserBase(BaseModel):
    email: EMAIL_FIELD

class UserLogin(UserBase):
    password: TEXT_FIELD

class UserRegister(UserBase):
    password: PASSWORD_FIELD
    @field_validator("password")
    @classmethod
    def validate_password(cls, value:str) -> str:
        """Custom password validation to ensure it meets security criteria."""
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"[0-9]", value):
            raise ValueError("Password must contain at least one number.")
        if not re.search(r"[@&£$%^&()\-]", value):
            raise ValueError("Password must contain at least one special character (@&£$%^&()-).")
        return value
    
    first_name: NAME_FIELD
    last_name: NAME_FIELD
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