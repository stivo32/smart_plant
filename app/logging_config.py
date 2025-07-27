import logging
import logging.config
import yaml


def setup_logging(config_path="./app/logging.yaml"):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    logging.config.dictConfig(config)

    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.pool").setLevel(logging.WARNING)