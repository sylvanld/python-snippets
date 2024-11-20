import json
import logging
import socket

from snippet.logs.utils import get_record_extras

GELF_LEVEL_MAPPING = {
    "TRACE": 7,
    "DEBUG": 7,
    "INFO": 6,
    "WARNING": 4,
    "ERROR": 3,
    "CRITICAL": 2,
}


class GELFFormatter(logging.Formatter):
    def __init__(self, log_trace: bool = False, indent: int = None):
        super().__init__()
        self.log_trace = log_trace
        self.indent = indent
        self.hostname = socket.gethostname()

    def format(self, record):
        record_extra = get_record_extras(record)
        gelf_record = {
            "host": self.hostname,
            "level": GELF_LEVEL_MAPPING[record.levelname],
            "short_message": record.msg % record_extra,
            "timestamp": record.created,
            "version": "1.1",
            "_log_type": record.name,
        }
        if self.log_trace:
            record_extra.update(
                {
                    "log_module": record.module,
                    "log_lineno": record.lineno,
                    "log_function": record.funcName,
                }
            )
        for field, value in record_extra.items():
            gelf_record["_" + field.lower()] = value
        return json.dumps(gelf_record, indent=self.indent)
