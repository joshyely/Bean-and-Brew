from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

from .config import settings
from .models import Base

class Database:
    def __init__(self, db_url):
        self.engine = create_engine(url=db_url)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine) 

db = Database(db_url=settings.DB_URL)
    