from Modules.generate_key import GenerateKey
from Modules.encrypt_data import EncryptToFile
from Modules.decrypt_data import DecryptFile
from Modules.settings import Settings
from Modules.base_logger import logger
from Modules.clear_terminal import clear_screen


class MainMenu:
    """This class is used setup the main menu options when launching the program"""

    def main_menu_options(self):
        """Main Menu Options"""
        print("\n Manage Encryption Key Menu")
        print(" --------------------------")
        print(" a) Generate Encryption Key")
        print(" b) Decrypt Binary File")
        print(" c) Encrypt Data to Binary File")
        print(" d) Settings")
        print(" e) Exit\n")

    def option_a(self):
        """Generate an Encryption Key"""
        logger.info(f"Generating new decryption key...")
        key_check = GenerateKey()
        key_check.create_key_workflow()

    def option_b(self):
        """Decrypt Binary File"""
        logger.info(f"Decrypting data...")
        decrypt_file = DecryptFile()
        decrypt_file.decrypt_binary_file_workflow()

    def option_c(self):
        """Encrypt Data to File"""
        logger.info(f"Encrypting data...")
        create_binary = EncryptToFile()
        create_binary.create_binary_file_workflow()

    def option_d(self):
        """Adjust Settings"""
        logger.info(f"Updating Settings...")
        update_settings = Settings()
        update_settings.verify_config_exists()
        answer = update_settings.update_settings_inquirer_prompt()
        if answer == "--Main Menu--":
            logger.info(f"Returning to Main Menu")
            print("Going to Main Menu")
            return
        else:
            # Get new path from user
            clear_screen()
            new_binary_path = update_settings.get_new_binary_path()

            # Format string
            formatted_binary_path = update_settings.format_binary_path(new_binary_path)

            # Write changes to config file
            update_settings.update_binary_path(formatted_binary_path)
            logger.info(f"Returning to Main Menu")
            print("Going to Main Menu")
