"""
SqlAlchemmy models
"""
from aiolchemy.db.core import AsyncBase
from sqlalchemy import *

# create your models here

class User(AsyncBase):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(32))