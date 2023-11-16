import importlib


def setup(recipe_name):
    importlib.import_module(".models", recipe_name)
    importlib.import_module(".handlers", recipe_name)