from . import db
from cauldron import chatbot
from .settings import WORKSPACE_DIR
import cauldron.settings
import importlib.util
import asyncio
import os


def _settings_to_env():
    is_const = lambda x: x.upper() == x
    for name, attr in vars(cauldron.settings).items():
        if is_const(name):
            os.environ.setdefault(name, str(attr))

def setup_settings():
    _settings_to_env()

def setup_recipes():
    recipe_names = cauldron.settings.RECIPES
    for recipe_name in recipe_names:
        spec = importlib.util.spec_from_file_location(
            recipe_name,
            WORKSPACE_DIR / recipe_name / "__init__.py")
        recipe = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(recipe)
        recipe.setup(recipe_name)

def setup():
    setup_settings()
    db.setup()
    chatbot.setup()
    setup_recipes()
    db.post_setup()

def run():
    asyncio.run(chatbot.dp.start_polling(chatbot.bot))
    