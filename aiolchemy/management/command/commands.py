"""
Your own commands for command manager
"""
from pathlib import Path
from .base import BaseCommand
from ...core.assembly import Assembly
from os import getenv
import shutil


class MakeRecipeCommand(BaseCommand):
    """
    Make new recipe by template schema
    """
    name = "makerecipe"

    def execute(self):
        assembly = Assembly()
        assembly.setup_settings()
        recipe_name = self.args[2]
        this_file = Path(__file__).resolve()
        templates_dir = this_file.parent.parent.parent / "templates"
        recipe_template = templates_dir / "recipe"
        recipes_dir = Path(getenv("RECIPES_DIR")).resolve()
        shutil.copytree(recipe_template, recipes_dir / recipe_name)


class BrewCommand(BaseCommand):
    """
    Start "brew" the cauldron to run project
    """
    name = "brew"

    def execute(self):
        assembly = Assembly()
        assembly.assemble()
        assembly.run()
