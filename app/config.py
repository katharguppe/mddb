from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from pathlib import Path

class Settings(BaseSettings):
    """Application configuration loaded from .env file."""

    model_config = ConfigDict(
        env_file=str(Path(__file__).parent.parent / ".env"),
        case_sensitive=True,
        extra="ignore"
    )

    PRODUCTION: str = "1"  # "1" for mockup (Phase 0), "0" for live (Phase 1)
