import logging
from datetime import datetime
from typing import Any, Mapping, Tuple

from snippet.logs.style import LEVEL_COLOR, Color, Weight
from snippet.logs.utils import get_record_extras, iter_combine_columns


def get_sort_key(entry: Tuple[str, str]):
    return (not entry[0].startswith("log_"), entry[0])


class DebugFormatter(logging.Formatter):
    def __init__(
        self,
        datefmt: str = "%H:%M:%S.%f",
        validate: bool = True,
        colored: bool = True,
        log_date: bool = True,
        log_type: bool = True,
        log_extra: bool = True,
        log_trace: bool = False,
        *,
        defaults: Mapping[str, Any] | None = None,
    ):
        super().__init__(None, datefmt, "%", validate, defaults=defaults)
        self.colored = colored
        self.log_date = log_date
        self.log_type = log_type
        self.log_extra = log_extra
        self.log_trace = log_trace

    def format_text(
        self,
        text: str,
        color: Color = None,
        weight: Weight = Weight.NORMAL,
        ljust: int = None,
    ):
        """Convert raw text (str) to a style text with color, font weight, and eventually fixed length."""
        out = ""
        if self.colored and weight:
            out += weight.value
        if self.colored and color:
            out += color.value
        out += text
        if self.colored:
            out += Weight.NORMAL.value
        if ljust:
            N = ljust - len(text)
            if N > 0:
                out += " " * N
        return out

    def get_logged_attributes(
        self, record: logging.LogRecord, record_extra: dict = None
    ):
        """Compute displayed attributes of a log record based on formatter configuration."""
        log_attributes = {}

        if self.log_type:
            log_attributes["log_type"] = record.name

        if self.log_trace:
            log_attributes.update(
                {
                    "log_module": record.module,
                    "log_lineno": record.lineno,
                    "log_function": record.funcName,
                }
            )

        if self.log_extra and record_extra:
            log_attributes.update(record_extra)

        return log_attributes

    def iterate_first_column(self, record: logging.LogRecord, column_width: int = 22):
        """Given a record, return an iterator for cells of the first column of its representation."""
        # first row is colored log level
        yield self.format_text(
            record.levelname,
            color=LEVEL_COLOR[record.levelname],
            weight=Weight.BOLD,
            ljust=column_width,
        )
        # second row is log creation date
        if self.log_date:
            yield datetime.fromtimestamp(record.created).strftime(self.datefmt).ljust(
                column_width
            )

    def iterate_second_column(self, record: logging.LogRecord):
        """Given a record, return an iterator for cells of the second column of its representation."""
        record_extra = get_record_extras(record)
        # first row is bold log message
        yield self.format_text(record.msg % record_extra, weight=Weight.BOLD)
        # generate log attributes table
        for attr, value in self.get_logged_attributes(record, record_extra).items():
            colored_key = self.format_text(attr, color=Color.CYAN, weight=Weight.ITALIC)
            colored_value = self.format_text(
                str(value), color=Color.MAGENTA, weight=Weight.ITALIC
            )
            yield f"  {colored_key}: {colored_value}"

    def format(self, record):
        log_text = ""

        column1_width = 22
        for row in iter_combine_columns(
            self.iterate_first_column(record, column_width=column1_width),
            self.iterate_second_column(record),
            default="",
        ):
            cell1, cell2 = row
            log_text += cell1.ljust(column1_width) + cell2 + "\n"

        return log_text
