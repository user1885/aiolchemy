"""
Aiogram root file
"""
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from os import getenv


storage = MemoryStorage()
bot = Bot(token=getenv("BOT_API_TOKEN"))
dp = dispatcher = Dispatcher(storage=storage)