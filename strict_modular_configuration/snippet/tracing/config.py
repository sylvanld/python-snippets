from enum import Enum

from pydantic import BaseModel, Field


class TracingConfig(BaseModel):
    enabled: bool = Field(default=False)
    otlp_endpoint: str = Field(default="localhost:4318")
    otlp_protocol: str = Field(default="http")
