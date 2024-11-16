from pydantic import BaseModel, Field


class DatabaseConfig(BaseModel):
    engine_url: str = Field(
        default="sqlite:///:memory:",
        description="URL used by SQLAlchemy engine to connect database.",
    )
