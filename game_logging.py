from loguru import logger
from sys import stderr

logger.remove()
logger.add(
    stderr,
    colorize=True,
    format="<level>{message}</level>",
    level="INFO",
)
