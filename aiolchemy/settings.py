from pathlib import Path


AIOLCHEMY_DIR = Path(__file__).resolve().parent

WORKSPACE_DIR = AIOLCHEMY_DIR.parent

TEMPLATES_DIR = AIOLCHEMY_DIR / "templates"

RECIPE_TEMPLATE_DIR = TEMPLATES_DIR / "recipe"
