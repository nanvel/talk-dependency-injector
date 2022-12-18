import os.path
from pathlib import Path

from pydantic import BaseSettings, Field, validator
from pydantic.color import Color


class Settings(BaseSettings):
    db_path: Path = Field(default="tasks.db")
    text_color: Color = Field(default="blue")

    @validator("db_path")
    def validate_db_path(cls, db_path):
        """Convert to absolute path."""
        return os.path.realpath(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", db_path)
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
