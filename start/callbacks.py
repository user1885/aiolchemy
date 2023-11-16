"""
Callbacks for future handling by dispatcher or router
"""
from aiolchemy.db.context.session import asessional
from aiogram.types import Message
from aiogram.filters import CommandObject
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User

# create your callbacks here

@asessional
async def start(message: Message,
                command: CommandObject,
                session: AsyncSession):
    await message.answer("start")