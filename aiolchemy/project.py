from . import db
from cauldron import settings
from cauldron import chatbot
import importlib.util
import asyncio
import os


def _settings_to_env():
    is_const = lambda x: x.upper() == x
    for name, attr in vars(settings).items():
        if is_const(name):
            os.environ.setdefault(name, str(attr))

def setup_settings():
    _settings_to_env()

def setup_recipes():
    recipe_names = settings.RECIPES
    for recipe_name in recipe_names:
        recipe = importlib.import_module(recipe_name)
        recipe.setup(recipe_name)

def setup():
    setup_settings()
    db.setup()
    chatbot.setup()
    setup_recipes()
    db.post_setup()

def run():
    asyncio.run(chatbot.dp.start_polling(chatbot.bot))
    