import sys
from typing import Literal, Optional
import logging


def get_logger(
    name:Optional[str] = None,
    level:Literal['DEBUG', 'INFO', 'WARNING', 'ERROR'] = 'DEBUG',
    format:Optional[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
) -> logging.Logger:
    """
    Creates a new logger, setting it to the global format for this project.

    Args:
        name (Optional[str]): 
            Name of logger. Defaults to None.
        level (Literal[str]): 
            Level of logs being displayed.  
            Accepted values: 'DEBUG', 'INFO', 'WARNING', 'ERROR'

    Returns:
        logging.Logger: 
            The created logger object.
    """
    
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if format:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(
            logging.Formatter(format)
        )
        logger.addHandler(handler)
        
    return logger


uvicorn_logger = get_logger('uvicorn.error', format=None)
