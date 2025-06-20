import logging


def get_logger(name: str) -> logging.Logger:
    """Setup logger

    Args:
        name (str): logger name

    Returns:
        logging.Logger: logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger