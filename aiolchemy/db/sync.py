"""
Sync database part
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from os import getenv


class SyncBase(DeclarativeBase):
    pass


engine = create_engine(getenv("SYNC_DATABASE_URL"))
session = sessionmaker(bind=engine)

metadata = MetaData()
metadata.reflect(bind=engine)

tables = metadata.tables