from dataclasses import dataclass


class ConfigurationError(Exception):
    """Exception raised when a configuration error occurs."""


@dataclass
class Config:
    """Simple class holding sample configuration for this demo."""

    database_url: str


CONF = Config(database_url="sqlite:///db.sqlite")
