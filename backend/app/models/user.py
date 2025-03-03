from sqlalchemy import Column, String, Date, Boolean
from datetime import date

from .base import Base

class User(Base):
    __tablename__ = 'users'

    email = Column(String(50), unique=True)
    password_hash = Column(String)
    first_name = Column(String(50))
    last_name = Column(String(50))
    dob = Column(Date)
    receive_promotions = Column(Boolean)
    date_created = Column(Date)

    def __init__(
        self,
        *,
        email:str,
        password_hash:str,
        first_name:str,
        last_name:str,
        dob:date,
        receive_promotions:bool,
        date_created:date
    ):
        self.email = email
        self.password_hash = password_hash
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.receive_promotions = receive_promotions
        self.date_created = date_created