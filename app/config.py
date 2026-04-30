from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    """Application configuration loaded from .env file."""

    PRODUCTION: str = "1"  # "1" for mockup (Phase 0), "0" for live (Phase 1)

    class Config:
        env_file = str(Path(__file__).parent.parent / ".env")
        case_sensitive = True
