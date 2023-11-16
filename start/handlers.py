"""
Register callbacks as handlers
"""
from cauldron.chatbot import dp
from .callbacks import *
from aiogram.filters import CommandStart
from aiogram import F

# create your handlers here

dp.message.register(start,
                    CommandStart())
