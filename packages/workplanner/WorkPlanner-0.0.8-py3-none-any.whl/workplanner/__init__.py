import sys

from loguru import logger

logger.add(sys.stdout, colorize=True, backtrace=True, diagnose=True)
