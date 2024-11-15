import os

from snippet.config import Config


class EnvConfig(Config):
    def get(self, key: str):
        return os.environ.get(key.replace(".", "_").upper())
