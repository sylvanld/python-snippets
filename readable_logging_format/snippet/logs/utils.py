import logging
from typing import Iterable, Tuple

RECORD_NON_EXTRA_FIELDS = {
    "args",
    "msg",
    "levelname",
    "levelno",
    "pathname",
    "filename",
    "name",
    "module",
    "exc_info",
    "exc_text",
    "stack_info",
    "lineno",
    "funcName",
    "created",
    "msecs",
    "relativeCreated",
    "thread",
    "threadName",
    "processName",
    "process",
}


def iter_combine_columns(
    *columns: Iterable[str], default=None
) -> Iterable[Tuple[str, ...]]:
    while True:
        row = tuple(next(column, default) for column in columns)
        if not any(row):
            break
        yield row


def get_record_extras(record: logging.LogRecord):
    extra = vars(record).copy()
    for field in RECORD_NON_EXTRA_FIELDS:
        extra.pop(field, None)
    return extra
