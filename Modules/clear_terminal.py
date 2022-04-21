import os
import platform


class ClearTerminalText:
    """This class is used to clear the terminal window of text"""

    def clear_screen(self):
        """Get OS Platform"""
        platform_os = platform.system()

        if platform_os == "Windows":
            """Windows"""
            return os.system("cls")
        else:
            """Linux"""
            return os.system("clear")
