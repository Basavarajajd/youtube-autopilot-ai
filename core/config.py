"""
Global configuration manager for YouTube Autopilot AI
Loads environment variables and exposes a single settings object.
"""

import os
from pathlib import Path
from dotenv import load_dotenv


# Root project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env file if present
env_path = BASE_DIR / ".env"
if env_path.exists():
    load_dotenv(env_path)


class Settings:
    """Central config used across the entire project"""

    # -------------------------
    # APP INFO
    # -------------------------
    APP_NAME: str = "YouTube Autopilot AI"
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "True") == "True"

    # -------------------------
    # PATHS
    # -------------------------
    DATA_DIR: Path = BASE_DIR / "data"
    GENERATED_DIR: Path = BASE_DIR / "generated"
    ASSETS_DIR: Path = BASE_DIR / "assets"

    VIDEO_DIR: Path = GENERATED_DIR / "videos"
    IMAGE_DIR: Path = GENERATED_DIR / "images"
    THUMBNAIL_DIR: Path = GENERATED_DIR / "thumbnails"
    SHORTS_DIR: Path = GENERATED_DIR / "shorts"
    VOICE_DIR: Path = GENERATED_DIR / "voice"

    # -------------------------
    # DATABASE
    # -------------------------
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{BASE_DIR}/data/app.db"
    )

    # -------------------------
    # REDIS / CELERY
    # -------------------------
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    # -------------------------
    # AI API KEYS
    # -------------------------
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    STABILITY_API_KEY: str | None = os.getenv("STABILITY_API_KEY")
    ELEVENLABS_API_KEY: str | None = os.getenv("ELEVENLABS_API_KEY")

    # -------------------------
    # YOUTUBE
    # -------------------------
    YOUTUBE_CLIENT_ID: str | None = os.getenv("YOUTUBE_CLIENT_ID")
    YOUTUBE_CLIENT_SECRET: str | None = os.getenv("YOUTUBE_CLIENT_SECRET")

    # -------------------------
    # RUNTIME LIMITS
    # -------------------------
    MAX_DAILY_VIDEOS: int = int(os.getenv("MAX_DAILY_VIDEOS", 5))
    MAX_DAILY_SHORTS: int = int(os.getenv("MAX_DAILY_SHORTS", 10))

    # -------------------------
    # CREATE DIRECTORIES
    # -------------------------
    @staticmethod
    def create_required_dirs():
        dirs = [
            Settings.DATA_DIR,
            Settings.GENERATED_DIR,
            Settings.VIDEO_DIR,
            Settings.IMAGE_DIR,
            Settings.THUMBNAIL_DIR,
            Settings.SHORTS_DIR,
            Settings.VOICE_DIR,
        ]
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)


# Create global settings instance
settings = Settings()

# Ensure required folders exist on import
settings.create_required_dirs()
