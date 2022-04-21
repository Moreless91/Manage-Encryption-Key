from Modules.generate_key import GenerateKey
from Modules.encrypt_data import EncryptToFile
from Modules.decrypt_data import DecryptFile
from Modules.settings import Settings


class MainMenu:
    """This class is used setup the main menu options when launching the program"""

    def __init__(self, user_input=None):
        self.user_input = None

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
        key_check = GenerateKey()
        key_check.create_key_workflow()

    def option_b(self):
        """Decrypt Binary File"""
        decrypt_file = DecryptFile()
        decrypt_file.decrypt_binary_file_workflow()

    def option_c(self):
        """Encrypt Data to File"""
        create_binary = EncryptToFile()
        create_binary.create_binary_file_workflow()

    def option_d(self):
        """Adjust Settings"""
        update_settings = Settings()
        update_settings.update_settings()
