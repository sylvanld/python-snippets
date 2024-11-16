from enum import Enum

from pydantic import BaseModel, Field


class LogFormat(Enum):
    GELF = "GELF"
    DEBUG = "debug"


class LogLevel(Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class RotationFrequency(Enum):
    DAY = "day"
    HOUR = "hour"


class DebugLogsConfig(BaseModel):
    enabled: bool = Field(default=False)
    logger: str = Field(default="")
    file: str = Field(default="debug.log")
    backup_frequency: RotationFrequency = Field(default=RotationFrequency.DAY)
    backup_count: int = Field(default=3)


class LoggingConfig(BaseModel):
    level: LogLevel = Field(
        default=LogLevel.INFO,
        description="Level used by log handler to filter log records.",
    )
    format: LogFormat = Field(
        default=LogFormat.GELF,
        description="Name of formatter used to format log records.",
    )
    audit: DebugLogsConfig = Field(default_factory=lambda: [DebugLogsConfig()])
