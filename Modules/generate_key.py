import inquirer
from pathlib import Path
from cryptography.fernet import Fernet
from Modules.settings import Settings


class GenerateKey:
    """This class is used to generate a new encryption key and save it to file"""

    def __init__(self):
        """Load config file"""
        config_file = Settings()
        config_file = config_file.settings()
        self.data_path = config_file["path_dir"]["data"]

    def check_for_existing_key(self):
        """Check the Key folder for an existing key"""
        key = Path(".env")
        if key.is_file():
            print(f" Key found in: .env")
            print(f" .bin save to: {self.data_path}")
            return True

    def create_key_workflow(self):
        """Workflow for creating a new a key"""
        if GenerateKey.check_for_existing_key(self) == True:
            print("\nAre you sure you want to overwrite your key?")

            """Launch inquirer for user action"""
            user_action = GenerateKey.overwrite_file_prompt(self)

            if user_action == False:
                print("Returning to Main Menu")
                return

        """Get amount of times user wants to generate a number"""
        user_input = GenerateKey.get_iteration_amount(self)

        """Use random number to generate a new key XX amount of times"""
        new_key = GenerateKey.generate_new_key(self, user_input)

        """Write key to file"""
        GenerateKey.write_key_to_file(self, new_key)

    def get_iteration_amount(self):
        """Get amount of times user wants to generate a number"""

        """Get user response"""
        user_input = None
        while user_input == None:
            try:
                print("Type the number of times a key will be randomly generated")
                print("NOTE: Only the last key randomly generated will be used!")
                user_input = int(input("Type number: "))  # Verify input is a whole number only
                if user_input > 0:  # Verify number is greater than '0'
                    return user_input
                else:
                    user_input = None
                    print("Integer must be greater than '0'")
            except ValueError:
                print("This is not a whole number.")

    def generate_new_key(self, user_input):
        """Generate new key"""
        for i in range(user_input):
            new_key = Fernet.generate_key()
            cipher_suite = Fernet(new_key)

        """Return the last key generated"""
        return new_key

    def write_key_to_file(self, new_key):
        """Write new key to file"""

        """Decode Binary to String"""
        new_key = new_key.decode("ascii")

        contents = f"DECRYPTION_KEY={new_key}"

        with open(".env", "w") as file:
            file.write(contents)
            print(f"Contents saved to: .env")

    def overwrite_file_prompt(self):
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
