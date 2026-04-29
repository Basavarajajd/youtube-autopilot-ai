"""
Central logging system for YouTube Autopilot AI
"""

import sys
from loguru import logger
from core.config import settings


LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)


def setup_logger():
    """Configure global logger"""

    # Remove default logger
    logger.remove()

    # Console logger
    logger.add(
        sys.stdout,
        format=LOG_FORMAT,
        level="DEBUG" if settings.DEBUG else "INFO",
        colorize=True,
    )

    # File logger
    logger.add(
        "logs/app.log",
        rotation="5 MB",
        retention="10 days",
        compression="zip",
        level="INFO",
        format=LOG_FORMAT,
    )


# Setup logger immediately on import
setup_logger()
