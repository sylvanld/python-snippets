import yaml
from pydantic import BaseModel, Field

from snippet.database.config import DatabaseConfig
from snippet.logging.config import LoggingConfig
from snippet.tracing.config import TracingConfig


class YamlDumper(yaml.SafeDumper):
    def write_line_break(self, data=None):
        super().write_line_break(data)
        if len(self.indents) == 1:
            super().write_line_break()


class BaseConfig(BaseModel):
    def write_default_config(self, file_path: str):
        default_config = self.model_dump(mode="json")
        with open(file_path, "w") as app_config_file:
            yaml.dump(
                default_config, app_config_file, Dumper=YamlDumper, sort_keys=False
            )

    @classmethod
    def from_file(cls, file_path: str):
        with open(file_path) as app_config_file:
            data = yaml.safe_load(app_config_file)
        return cls.model_validate(data)


class AppConfig(BaseConfig):
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    tracing: TracingConfig = Field(default_factory=TracingConfig)
