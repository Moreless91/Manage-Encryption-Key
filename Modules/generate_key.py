import inquirer
from pathlib import Path
from cryptography.fernet import Fernet
from Modules.settings import Settings
from typing import Optional, ByteString


class GenerateKey:
    """This class is used to generate a new encryption key and save it to file"""

    def __init__(self):
        """Load config file"""
        config_file = Settings()
        config_file: dict[str, str] = config_file.settings()
        self.data_path: str = config_file["path_dir"]["data"]

    def check_for_existing_key(self) -> bool:
        """Check the Key folder for an existing key"""
        key = Path(".env")
        if key.is_file():
            print(f" Key found in: .env")
            print(f" .bin save to: {self.data_path}")
            return True

        return False

    def create_key_workflow(self):
        """Workflow for creating a new a key"""
        if GenerateKey.check_for_existing_key(self) == True:
            print("\nAre you sure you want to overwrite your key?")

            """Launch inquirer for user action"""
            user_action: bool = GenerateKey.overwrite_file_prompt(self)

            if user_action == False:
                print("Returning to Main Menu")
                return

        """Get amount of times user wants to generate a number"""
        user_input: int = GenerateKey.get_iteration_amount(self)

        """Use random number to generate a new key XX amount of times"""
        new_key: str = GenerateKey.generate_new_key(self, user_input)

        """Write key to file"""
        GenerateKey.write_key_to_file(self, new_key)

    def get_iteration_amount(self) -> Optional[int]:
        """Get amount of times user wants to generate a number"""

        """Get user response"""
        user_input = None
        while True:
            try:
                print("Type the number of times a key will be randomly generated")
                print("NOTE: Only the last key randomly generated will be used!")
                user_input = int(input("Type number: "))  # Verify input is a whole number only
                if user_input > 0:  # Verify number is greater than '0'
                    break  # Exit While Loop
                else:
                    user_input = None
                    print("Integer must be greater than '0'")
            except ValueError:
                print("This is not a whole number.")

        return user_input

    def generate_new_key(self, user_input: int) -> ByteString:
        """Generate new key"""
        for i in range(user_input):
            new_key = Fernet.generate_key()

        """Return the last key generated"""
        return new_key

    def write_key_to_file(self, new_key: str) -> bool:
        """Write new key to file"""

        """Decode Binary to String"""
        new_key = new_key.decode("ascii")

        contents = f"DECRYPTION_KEY={new_key}"

        with open(".env", "w") as file:
            file.write(contents)
            print(f"Contents saved to: .env")

        return True

    def overwrite_file_prompt(self) -> bool:
        """Setup menu to prompt for overwrite change"""
        print("\n\tOverwrite Options:\n")
        questions = [
            inquirer.List(
                "overwrite_file_options",
                message="Option Select",
                choices=["Yes", "No"],
                carousel=True,
            ),
        ]
        answer = inquirer.prompt(
            questions,
        )

        if answer["overwrite_file_options"] == "Yes":
            return True
        else:
            return False
