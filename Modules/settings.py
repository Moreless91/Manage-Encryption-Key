import json
import inquirer
from pathlib import Path
from Modules.clear_terminal import clear_screen


class Settings:
    """This class is used to load and update the config file"""

    def __init__(self):
        self.config_file: str = "Settings/config.json"

        def verify_config_exists():
            """Verify config file exists"""
            config_path_check = Path(self.config_file)
            if config_path_check.is_file():
                return True
            else:
                print("Cannot find config.json in Settings/")
                print("Exiting...")
                exit()

        # Verify config file exists
        verify_config_exists()

    def settings(self) -> dict[str, str]:
        """Load config file"""
        with open(self.config_file) as json_data_file:
            config_file = json.load(json_data_file)

        return config_file

    def update_settings(self):
        """Update config.json settings"""

        """Load config.json"""
        config_file: dict[str, str] = Settings.settings(self)
        binary_path: str = config_file["path_dir"]["data"]

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
        if answer["settings_options"] == "--Main Menu--":
            print("Going to Main Menu")
            return

        else:
            """Get new path from user"""
            new_binary_path = Settings.get_new_binary_path(self, binary_path)

            """Write changes to config file"""
            Settings.update_binary_path(self, new_binary_path)

    def get_new_binary_path(self, binary_path: str) -> str:
        """Update binary path save location"""

        """Clear terminal screen"""
        clear_screen()

        print("\n\tUpdate Binary Save Location:\n")
        print(f"Current Setting: {binary_path}\n")
        print(f"EXAMPLE: Absolute path: C:/Users/username/Documents/")
        print(f"EXAMPLE: Relative path: Data/\n")
        print("\nTo cancel, type: back\n")

        new_binary_path = input("Enter new path: ")

        return new_binary_path

    def update_binary_path(self, new_binary_path: str) -> None:
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

        """Write answer to config.json"""
        with open(self.config_file, "r+") as jsonFile:
            config_file = json.load(jsonFile)

            """Update config file item"""
            config_file["path_dir"]["data"] = new_binary_path

            """Close file and maintain human readability"""
            jsonFile.seek(0)  # <--- should reset file position to the beginning
            json.dump(config_file, jsonFile, indent=4)  # <--- should make human readoble
            jsonFile.truncate()
