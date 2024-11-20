from enum import Enum


class Color(Enum):
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[00m"


class Weight(Enum):
    BOLD = "\033[01m"
    ITALIC = "\033[03m"
    NORMAL = "\033[00m"


LEVEL_COLOR = {
    "TRACE": Color.BLUE,
    "DEBUG": Color.BLUE,
    "INFO": Color.GREEN,
    "WARNING": Color.YELLOW,
    "ERROR": Color.RED,
    "RESET": Color.RED,
}
