from sqlalchemy import Column, String

from .base import Base



class Cafe(Base):
    __tablename__ = 'products'

    name = Column(String(50))
    address = Column(String(100))
    postcode = Column(String(10))

class Restaurant(Base):
    __tablename__ = 'restaurants'

    name = Column(String(50))
    address = Column(String(100))
    postcode = Column(String(10))
    
class BakingLesson(Base):
    __tablename__ = 'baking_lessons'
    
    name = Column(String(50))
    address = Column(String(100))
    postcode = Column(String(10))
    
    