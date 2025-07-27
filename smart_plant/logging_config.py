import logging
import logging.config
from pathlib import Path
import yaml

from smart_plant.config import LOGGING_CONFIG_FILE


def setup_logging(config_path: Path =LOGGING_CONFIG_FILE):
    if not config_path.is_file():
        raise FileNotFoundError(f"Logging configuration file not found: {config_path}")
    with config_path.open() as f:
        config = yaml.safe_load(f)
    logging.config.dictConfig(config)

    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.pool").setLevel(logging.WARNING)