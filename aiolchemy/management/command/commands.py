"""
Your own commands for command manager
"""
from .base import BaseCommand
from ... import project
from ...settings import RECIPE_TEMPLATE_DIR
import shutil


class MakeRecipeCommand(BaseCommand):
    """
    Make new recipe by template schema
    """
    name = "makerecipe"

    def execute(self):
        project.setup_settings()
        recipe_name = self.args[2]
        shutil.copytree(RECIPE_TEMPLATE_DIR, recipe_name)


class BrewCommand(BaseCommand):
    """
    Start "brew" the cauldron to run project
    """
    name = "brew"

    def execute(self):
        project.setup()
        project.run()