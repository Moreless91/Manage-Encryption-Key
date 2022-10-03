import os
import platform


def clear_screen():
    # This function is used to clear the terminal console's text

    # Get OS Platform
    platform_os: str = platform.system()

    if platform_os == "Windows":
        return os.system("cls")
    else:
        return os.system("clear")
