"""
Module to assemble project parts in right order
"""
from os import getenv
import importlib
import asyncio
import os


class Assembly:
    def setup_settings(self):
        settings = importlib.import_module(".settings", "cauldron")
        is_constant = lambda x: x.upper() == x
        for name, attr in vars(settings).items():
            if is_constant(name):
                os.environ.setdefault(name, str(attr))
        return settings

    def _setup_recipe_handlers(self, recipe_dir):
        handlers = importlib.import_module(
            f".{recipe_dir}.handlers", 
            "recipes")
        return handlers

    def setup_recipies(self):
        recipe_dirs = os.listdir(getenv("RECIPES_DIR"))
        for recipe_dir in recipe_dirs:
            self._setup_recipe_handlers(recipe_dir)

    def setup_chatbot(self):
        chatbot = importlib.import_module(".chatbot", "cauldron")
        return chatbot

    def assemble(self):
        self.setup_settings()
        self.setup_recipies()
        self.chatbot = self.setup_chatbot()

    def run(self):
        dp = self.chatbot.dp
        bot = self.chatbot.bot
        asyncio.run(dp.start_polling(bot))