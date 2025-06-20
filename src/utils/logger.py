import logging

from google.cloud.logging import Client as CloudLoggingClient
from google.cloud.logging.handlers import CloudLoggingHandler

from src.core.config import settings


def setup_logger(name: str, level: int = logging.DEBUG, cloud_logging: bool = False) -> logging.Logger:
    """Setup logger

    Args:
        name (str): logger name
        level (int): logger level
        cloud_logging (bool): whether to use cloud logging

    Returns:
        logging.Logger: logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler: logging.Handler | CloudLoggingHandler

    if not logger.hasHandlers():
        if cloud_logging:
            cloud_logging_client = CloudLoggingClient()
            handler = CloudLoggingHandler(cloud_logging_client, name=name)
        else:
            handler = logging.StreamHandler()

        formatter = logging.Formatter(datefmt="%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


logger = setup_logger(
    name=settings.APP_NAME,
    cloud_logging=settings.CLOUD_LOGGING
)