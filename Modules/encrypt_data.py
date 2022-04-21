import os
import inquirer
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from Modules.clear_terminal import ClearTerminalText
from Modules.settings import Settings


class EncryptToFile:
    """This class is used to encrypt data to a binary file"""

    def __init__(self):
        """Load config file"""
        config_file = Settings()
        config_file = config_file.settings()
        self.data_path = config_file["path_dir"]["data"]

    def create_binary_file_workflow(self):
        """Load key from .env"""
        key = EncryptToFile.load_key(self)

        while True:
            """Ask user for data to be encrypted and a filename"""
            answers_list = EncryptToFile.ask_user_for_data(self)

            """If the user is trying to exit, the list will be None"""
            if answers_list == None:
                return  # Return to main menu

            """Create a file using key"""
            EncryptToFile.create_file(self, key, answers_list)

            """Clear terminal screen"""
            clear_text = ClearTerminalText()
            clear_text.clear_screen()

            """Ask user if they have another file to encryt"""
            user_action = EncryptToFile.multiple_files_prompt(self)

            """Clear terminal screen"""
            clear_text.clear_screen()

            if user_action == False:
                return  # Return to main menu

    def load_key(self):
        """Load .env environment variables"""
        try:
            load_dotenv()
            key = os.environ["DECRYPTION_KEY"]
            return key

        except Exception as e:
            print(f"There was an issue loading {e}! \nExiting...")
            exit()

    def ask_user_for_data(self):
        """Ask user for data to be encrypted and a filename"""
        print("\n\tCreate Binary File:\n")
        print(f"NOTE: Binary files are saved in {self.data_path}\n")
        print('Type data and press "ENTER"\n')
        print("\nTo cancel, type: back\n")

        cancel_list = ["e", "exit", "quit", "exit()", "quit()", "cancel", "back"]

        """Get user response"""
        data = input("Enter the text you'd like to encrypt: ")

        """Check if user tried to cancel"""
        if data.lower() in cancel_list:
            return  # Return to main menu

        filename = input("Enter a new filename to save data to: ")
        """Check if user tried to cancel"""

        if filename.lower() in cancel_list:
            return  # Return to main menu

        return data, filename

    def create_file(self, key, answers_list):
        """Create a file using key"""

        """Encode data answer to binary"""
        binary_data = answers_list[0].encode("ascii")

        """Remove last 4 char if they are .bin"""
        filename = answers_list[1]
        if filename[-4:] == ".bin":
            filename = filename[:-4]

        cipher_suite = Fernet(key)
        ciphered_text = cipher_suite.encrypt(binary_data)
        with open(self.data_path + filename + ".bin", "wb") as file_object:
            file_object.write(ciphered_text)

    def multiple_files_prompt(self):
        """Setup menu to ask user if they would like to create an additional file"""
        print("\n\tCreate another encrypted file?:\n")
        questions = [
            inquirer.List(
                "multiple_files_options",
                message="Option Select",
                choices=["Yes", "No"],
                carousel=True,
            ),
        ]
        answer = inquirer.prompt(
            questions,
        )

        if answer["multiple_files_options"] == "Yes":
            return True
        else:
            return False
