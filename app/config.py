import pathlib

STORAGE_PATH = pathlib.Path("app") / "storage"
PHOTO_STORAGE_PATH = pathlib.Path("app") / "storage" / "photos"
DB_STORAGE_PATH = pathlib.Path("app") / "storage" / "db"
MIGRATIONS_STORAGE_PATH = pathlib.Path("app") / "storage" / "migrations"
DB_FILE = DB_STORAGE_PATH / "smart_plant.sqlite3"
SCHEDULER_CONFIG_FILE = pathlib.Path("app") / "tasks.json"