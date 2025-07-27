import pathlib

STORAGE_PATH = pathlib.Path("smart_plant") / "storage"
PHOTO_STORAGE_PATH = pathlib.Path("smart_plant") / "storage" / "photos"
DB_STORAGE_PATH = pathlib.Path("smart_plant") / "storage" / "db"
MIGRATIONS_STORAGE_PATH = pathlib.Path("smart_plant") / "storage" / "migrations"
DB_FILE = DB_STORAGE_PATH / "smart_plant.sqlite3"
SCHEDULER_CONFIG_FILE = pathlib.Path("smart_plant") / "tasks.json"
LOGGING_CONFIG_FILE = pathlib.Path("smart_plant") / "logging.yaml"