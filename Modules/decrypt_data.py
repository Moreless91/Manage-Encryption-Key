import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from Modules.settings import Settings


class DecryptFile:
    """This class is used to decrypt data from a binary file"""

    def __init__(self):
        """Load config file"""
        config_file = Settings()
        config_file = config_file.settings()
        self.data_path = config_file["path_dir"]["data"]

    def decrypt_binary_file_workflow(self):
        """Load key from .env"""
        key = DecryptFile.load_key(self)

        """Find all files in data directory"""
        file_list = DecryptFile.get_files(self)

        """Decrypt File"""
        DecryptFile.decrypt_files(self, key, file_list)

        """Confirm to go back to main menu"""
        DecryptFile.user_done(self)

    def load_key(self):
        """Load .env environment variables"""
        try:
            load_dotenv()
            key = os.environ["DECRYPTION_KEY"]
            return key

        except Exception as e:
            print(f"There was an issue loading {e}! \nExiting...")
            exit()

    def get_files(self):
        """Build list of files in the Queued directory"""
        file_list = []

        for (dirpath, dirnames, filenames) in os.walk(self.data_path):
            file_list.extend(filenames)
            break

        return filenames

    def decrypt_files(self, key, file_list):
        """Setup list for encrypted data"""
        encrypted_file_list = []
        encrypted_var_dict = {}

        """Create new list for files ending in .bin"""
        for item in file_list:
            if item.endswith(".bin"):
                encrypted_file_list.append(item)

        """Retrieve key from .bin file"""
        for i, file in enumerate(encrypted_file_list):

            try:  # it's possble a new key was generated and it won't be able to decrypt
                # old .bin files in the folder
                cipher_suite = Fernet(key)
                with open(self.data_path + file, "rb") as file_object:
                    for line in file_object:
                        encrypted_data = line
                """Attempt file decrypt"""
                uncipher_text = cipher_suite.decrypt(encrypted_data)
                encrypted_item = bytes(uncipher_text).decode("utf-8")

                """Add filename and data to dictionary"""
                encrypted_var_dict[file] = encrypted_item
            except:
                """Add filename and data to dictionary"""
                encrypted_var_dict[file] = "Decryption FAIL"

        """Setup variables for printing"""
        Filename = "Filename:"
        PlainText = "Plain Text:"
        Line = "-----------"

        print(f"\n{Filename : <40}{PlainText : <40}")
        print(f"{Line : <40}{Line: <40}")
        for file in encrypted_var_dict.items():
            print(f"{file[0] : <40}{file[1] : <40}")

    def user_done(self):
        """Prompt user for repsonse when they are ready to go back to the main menu"""
        input('\nType "done" when finished: ')
        return  # Return to Main Menu
