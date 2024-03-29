import json
import inquirer
from pathlib import Path
from Modules.base_logger import logger
from Modules.clear_terminal import clear_screen


class Settings:
    """This class is used to load and update the config file"""

    def __init__(self):
        self.config_file: str = "Settings/config.json"

    def update_settings_workflow(self) -> None:
        Settings.verify_config_exists(self)
        answer = Settings.update_settings_inquirer_prompt(self)
        if answer == "--Main Menu--":
            logger.info(f"Returning to Main Menu")
            print("Going to Main Menu")
            return
        else:
            # Get new path from user
            clear_screen()
            new_binary_path = Settings.get_new_binary_path(self)

            # Format string
            formatted_binary_path = Settings.format_binary_path(self, new_binary_path)

            # Write changes to config file
            Settings.update_binary_path(self, formatted_binary_path)
            logger.info(f"Returning to Main Menu")
            print("Going to Main Menu")

    def verify_config_exists(self) -> bool:
        """Verify config file exists"""
        logger.debug(f"Verifying '{self.config_file}' exists...")
        config_path_check = Path(self.config_file)
        if config_path_check.is_file():
            logger.debug(f"Found '{self.config_file}'")
            return True
        else:
            logger.critical(f"Cannot find '{self.config_file}'")
            logger.critical("Exiting...")
            exit()

    def settings(self) -> dict[str, str]:
        """Load config file into dictionary"""
        with open(self.config_file) as json_data_file:
            config_file = json.load(json_data_file)

        logger.debug(f"'{self.config_file}' loaded")

        return config_file

    def update_settings_inquirer_prompt(self) -> str:
        """Update config.json settings prompt"""

        print("\n\tUpdate Settings:\n")
        questions = [
            inquirer.List(
                "settings_options",
                message="Setting Select",
                choices=["--Main Menu--", "Binary Save Location"],
                carousel=True,
            ),
        ]
        answer = inquirer.prompt(
            questions,
        )

        """Outcome from option chosen"""
        answer = answer["settings_options"]

        return answer

    def get_new_binary_path(self) -> str:
        """Update binary path save location"""

        """Load config.json"""
        config_file: dict[str, str] = Settings.settings(self)
        binary_path: str = config_file["path_dir"]["data"]

        print("\n\tUpdate Binary Save Location:\n")
        print(f"Current Setting: {binary_path}\n")
        print(f"EXAMPLE: Absolute path: C:/Users/username/Documents/")
        print(f"EXAMPLE: Relative path: Data/\n")
        print("\nTo cancel, type: back\n")

        new_binary_path = input("Enter new path: ")

        return new_binary_path

    def format_binary_path(self, new_binary_path: str) -> str | None:
        """Check if user tried to cancel"""
        cancel_list = ["e", "exit", "quit", "exit()", "quit()", "cancel", "back"]
        if new_binary_path.lower() in cancel_list:
            return  # return to Main Menu

        """Add slash if not present"""
        if new_binary_path[-1] != "/":
            new_binary_path = new_binary_path + "/"

        """Replace all back slashes with forward slashes"""
        # This really shouldn't matter, but it looks better imo
        new_binary_path = new_binary_path.replace("\\", "/")
        new_binary_path = new_binary_path.replace("//", "/")  # Data\ becomes Data/ and NOT Data//

        return new_binary_path

    def update_binary_path(self, formatted_binary_path: str) -> None:
        """Write answer to config.json"""
        with open(self.config_file, "r+") as jsonFile:
            config_file = json.load(jsonFile)

            """Update config file item"""
            config_file["path_dir"]["data"] = formatted_binary_path

            """Close file and maintain human readability"""
            jsonFile.seek(0)  # <--- should reset file position to the beginning
            json.dump(config_file, jsonFile, indent=4)  # <--- should make human readable
            jsonFile.truncate()

        logger.info(f"New path '{formatted_binary_path}' has been saved to '{self.config_file}'")
