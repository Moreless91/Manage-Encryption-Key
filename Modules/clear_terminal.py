import os
import platform
from Modules.base_logger import logger


def clear_screen():
    # This function is used to clear the terminal console's text

    # Get OS Platform
    platform_os: str = platform.system()

    if platform_os == "Windows":
        logger.debug(f"Clearing terminal's text")
        return os.system("cls")
    else:
        logger.debug(f"Clearing terminal's text")
        return os.system("clear")
