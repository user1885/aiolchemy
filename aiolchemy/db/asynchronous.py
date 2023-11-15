"""
Async database part
"""
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from os import getenv
import asyncio

# async base for models
class AsyncBase(AsyncAttrs, DeclarativeBase):
    pass

# shortcut to get all tables from async engine's database
async def get_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(AsyncBase.metadata.reflect)
        return AsyncBase.metadata.tables

async_engine = create_async_engine(getenv("ASYNC_DATABASE_URL"))
async_session = async_sessionmaker(bind=async_engine)

# get existing tables from async engine
tables = asyncio.run(get_tables())