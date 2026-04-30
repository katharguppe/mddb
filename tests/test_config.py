import os
import tempfile
from pathlib import Path

def test_load_production_flag_from_env():
    """Test that PRODUCTION flag is loaded correctly."""
    # Create a temp .env file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.env', delete=False) as f:
        f.write("PRODUCTION=1\n")
        temp_env_file = f.name

    try:
        # Test loading with custom .env path
        from app.config import Settings
        settings = Settings(_env_file=temp_env_file)
        assert settings.PRODUCTION == "1"
    finally:
        os.unlink(temp_env_file)

def test_load_production_zero_from_env():
    """Test PRODUCTION=0 for Phase 1."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.env', delete=False) as f:
        f.write("PRODUCTION=0\n")
        temp_env_file = f.name

    try:
        from app.config import Settings
        settings = Settings(_env_file=temp_env_file)
        assert settings.PRODUCTION == "0"
    finally:
        os.unlink(temp_env_file)
