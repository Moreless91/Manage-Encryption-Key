import os
import inquirer
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from Modules.settings import Settings
from Modules.clear_terminal import clear_screen
from Modules.base_logger import logger


class EncryptToFile:
    """This class is used to encrypt data to a binary file"""

    def __init__(self):
        """Load config file"""
        config_file = Settings()
        config_file.verify_config_exists()
        config_file: dict[str, str] = config_file.settings()
        self.data_path: str = config_file["path_dir"]["data"]
        self.dotenv_path: str = config_file["path_dir"]["key"]

    def create_binary_file_workflow(self) -> None:
        """Load key from .env"""
        key: str = EncryptToFile.load_key(self)

        while True:
            """Ask user for data to be encrypted and a filename"""
            answers_list: tuple[str, str] | None = EncryptToFile.ask_user_for_data(self)

            """If the user is trying to exit, the list will be None"""
            if answers_list == None:
                return  # Return to main menu

            """Create a file using key"""
            EncryptToFile.create_file(self, key, answers_list)

            """Clear terminal screen"""
            clear_screen()

            """Ask user if they have another file to encryt"""
            user_action: bool = EncryptToFile.multiple_files_prompt(self)

            """Clear terminal screen"""
            clear_screen()

            if user_action == False:
                return  # Return to main menu

    def load_key(self) -> str:
        """Load .env environment variables"""
        try:
            load_dotenv(self.dotenv_path)
            key = os.environ["DECRYPTION_KEY"]
            logger.info("Encryption key loaded")
            return key

        except Exception as e:
            print(f"There was an issue loading {e}! \nExiting...")
            logger.critical(f"There was an issue loading {e}!")
            logger.critical(f"Exiting...")
            exit()

    def ask_user_for_data(self) -> tuple[str, str] | None:
        """Ask user for data to be encrypted and a filename"""
        print("\n\tCreate Binary File:\n")
        print(f"NOTE: Binary files are saved in {self.data_path}\n")
        print('Type data and press "ENTER"\n')
        print("\nTo cancel, type: back\n")

        """Get user response"""
        logger.info(f"User prompted to enter data to encrypt...")
        data = input("Enter the text you'd like to encrypt: ")
        logger.info(f"Response recorded")

        """Check if user tried to cancel"""
        user_cancelled = EncryptToFile.check_cancel_list(self, data)
        if user_cancelled == True:
            return None  # Return to main menu

        logger.info(f"User prompted to enter a filename to save to...")
        filename = input("Enter a new filename to save data to: ")
        logger.info(f"Response recorded")

        """Check if user tried to cancel"""
        user_cancelled = EncryptToFile.check_cancel_list(self, filename)
        if user_cancelled == True:
            return None  # Return to main menu

        return data, filename

    def check_cancel_list(self, user_input: str) -> bool | None:
        cancel_list = ["e", "exit", "quit", "exit()", "quit()", "cancel", "back"]
        if user_input.lower() in cancel_list:
            logger.info(f"User canceled action")
            logger.info(f"Returning to Main Menu")
            return True

    def create_file(self, key: str, answers_list: tuple[str, str]) -> None:
        """Create a file using key"""

        """Encode data answer to binary"""
        binary_data = answers_list[0].encode("ascii")
        logger.debug(f"Encoded data")

        """Remove last 4 char if they are .bin"""
        filename = EncryptToFile.remove_extension(self, answers_list)

        cipher_suite = Fernet(key)
        ciphered_text = cipher_suite.encrypt(binary_data)
        logger.info(f"Encrypted data")

        with open(f"{self.data_path}{filename}.bin", "wb") as file_object:
            file_object.write(ciphered_text)
        logger.info(f"Data saved to '{self.data_path}{filename}.bin'")

    def remove_extension(self, answers_list: tuple[str, str]) -> str:
        filename = answers_list[1]
        if filename[-4:] == ".bin":
            filename = filename[:-4]

        return filename

    def multiple_files_prompt(self) -> bool:
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
            logger.info(f"User chose to create another file...")
            return True
        else:
            logger.info(f"User chose NOT create another file")
            logger.info(f"Returning to Main Menu")
            return False
