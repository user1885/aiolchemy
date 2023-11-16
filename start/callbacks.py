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
    user = await session.get(User, message.chat.id)
    if user is None:
        user = User(id=message.chat.id,
                    name=message.chat.full_name)
        session.add(user)
        await session.commit()
        await message.answer("You are newbie!")
    else:
        await message.answer(str(user) + " nice to see you")