"""
Project settings
"""
from pathlib import Path

# telergam bot API token
BOT_API_TOKEN = "6087130044:AAFEXBHXjUDCHBIQJakSl6iYyWn3DhNmGbU"

# base directory for project files
BASE_DIR = Path(__file__).resolve().parent.parent

# database path by base directory
DATABASE_PATH = BASE_DIR / "db.sqlite3"

# sqlalchemy url for sync engine 
SYNC_DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# sqlalchemy url for async engine
ASYNC_DATABASE_URL = f"sqlite+aiosqlite:///{DATABASE_PATH}"

# recipes to load order is matter
RECIPES = (
    "start",
)