import os

from snippet.config import AppConfig
from snippet.database import Database
from snippet.logging import setup_logging
from snippet.tracing import setup_tracing

CONFIG_FILE = os.getenv("APP_CONFIG_FILE", "app.config.yaml")

try:
    # load app config from file
    config = AppConfig.from_file(CONFIG_FILE)
except FileNotFoundError:
    # if file does not exists, create it with default config
    config = AppConfig()
    config.write_default_config("app.config.yaml")

# pass module specific config to each module's entry point
setup_logging(config.logging)
setup_tracing(config.tracing)

database = Database(config.database)
