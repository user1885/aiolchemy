"""
Async database part
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.util import FacadeDict
from sqlalchemy import Table
from os import getenv
import asyncio


async_engine: AsyncEngine
async_session: async_sessionmaker[AsyncSession]
tables: FacadeDict[str, Table]

# async base for models
class AsyncBase(AsyncAttrs, DeclarativeBase):
    pass

# shortcut to get all tables from async engine's database
async def get_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(AsyncBase.metadata.reflect)
        return AsyncBase.metadata.tables

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(AsyncBase.metadata.create_all)

def setup_tables_to_db():
    asyncio.run(create_tables())

def setup_tables_from_db():
    global tables
    tables = asyncio.run(get_tables())

def setup():
    global async_engine, async_session
    async_engine = create_async_engine(getenv("ASYNC_DATABASE_URL"))
    async_session = async_sessionmaker(bind=async_engine)

def post_setup():
    setup_tables_to_db()
