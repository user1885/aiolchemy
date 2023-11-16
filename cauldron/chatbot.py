"""
Aiogram root file
"""
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from os import getenv


storage: MemoryError
bot: Bot
dp: Dispatcher

def setup():
    global storage, bot, dp
    storage = MemoryStorage()
    bot = Bot(token=getenv("BOT_API_TOKEN"))
    dp = Dispatcher(storage=storage)