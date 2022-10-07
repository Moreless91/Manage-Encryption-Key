import os
from pathlib import Path
import unittest
from unittest.mock import patch, PropertyMock
from Modules.encrypt_data import EncryptToFile

# TO RUN TESTS:
# Make sure __init__.py is in Tests folder
# In root directory, run command: python -m unittest
# This will discover and run all tests in the project
# NOTE: The tests run by number or alphabetically order


class TestEncryptData(unittest.TestCase):
    """This class is used to test functions in Modules/encrypt_data.py"""

    def test_1_init_data_path_check(self):
        """Test that the class object data_path value updated when initialized"""
        mock_location = "Tests/Mock_Data/Settings/config.json"
        mock_path = "Data/"
        mock_dotenv_path = "Tests/Mock_Data/mock_.env"

        # setup mock data variables
        create_binary = EncryptToFile()
        create_binary.config_file = mock_location
        create_binary.dotenv_path = mock_dotenv_path
        path_result = create_binary.data_path
        key_path_result = create_binary.dotenv_path

        self.assertEqual(path_result, mock_path, "Should be String: 'Data/'")
        self.assertEqual(key_path_result, mock_dotenv_path, "Should be String: 'Tests/Mock_Data/mock_.env'")

    def test_2_load_key_1(self):
        """Test loading missing .env"""
        mock_dotenv_path = ""

        # setup mock path variable
        create_binary = EncryptToFile()
        create_binary.dotenv_path = mock_dotenv_path

        with self.assertRaises(SystemExit):
            create_binary.load_key()

    def test_2_load_key_2(self):
        """Test loading the a mock .env"""
        mock_dotenv_path = "Tests/Mock_Data/mock_.env"
        mock_key = "zikiSlbESf_d8snWqiT9PvjbiyJuHY_EEblm-fvdFE4="

        # setup mock path variable
        create_binary = EncryptToFile()
        create_binary.dotenv_path = mock_dotenv_path
        result = create_binary.load_key()

        self.assertEqual(result, mock_key, f"Should be String: '{mock_key}'")

    def test_2_load_key_3(self):
        """Test loading the .env into a String"""
        create_binary = EncryptToFile()
        result = create_binary.load_key()

        valid_str = None

        if (type(result)) == str:
            valid_str = True

        self.assertTrue(valid_str, "'result' should be a String")

    mock_data_to_encrypt = "unittest_data"
    mock_filename = "filename_test"

    @patch("builtins.input", side_effect=[mock_data_to_encrypt, mock_filename])
    def test_3_ask_user_for_data_1(self, mock_user_input):
        """Test asking user for data to encrypt and filename to save to. It should return 2 strings"""

        create_binary = EncryptToFile()
        data, filename = create_binary.ask_user_for_data()

        valid_str_data = None
        valid_str_filename = None

        if (type(data)) == str:
            valid_str_data = True

        if (type(filename)) == str:
            valid_str_filename = True

        self.assertTrue(valid_str_data, "'data' should be a String")
        self.assertTrue(valid_str_filename, "'filename' should be a String")

    mock_data_to_encrypt = "back"
    mock_filename = "filename_test"

    @patch("builtins.input", side_effect=[mock_data_to_encrypt, mock_filename])
    def test_3_ask_user_for_data_2(self, mock_user_input):
        """Test cancelling when prompted to enter data to encrypt"""

        create_binary = EncryptToFile()
        result = create_binary.ask_user_for_data()
        self.assertIsNone(result, "'result' should return None")

    mock_data_to_encrypt = "filename_test"
    mock_filename = "back"

    @patch("builtins.input", side_effect=[mock_data_to_encrypt, mock_filename])
    def test_3_ask_user_for_data_3(self, mock_user_input):
        """Test cancelling when prompted to enter a filename to save to"""

        create_binary = EncryptToFile()
        result = create_binary.ask_user_for_data()
        self.assertIsNone(result, "'result' should return None")

    def test_4_check_cancel_list_1(self):
        """Test if user typed a cancel command to return to the Main Menu"""
        cancel_list = ["e", "exit", "quit", "exit()", "quit()", "cancel", "back"]

        for item in cancel_list:
            create_binary = EncryptToFile()
            result = create_binary.check_cancel_list(item)
            self.assertTrue(result, "'result' should return True")

    def test_5_create_file_1(self):
        """Test creating a file"""
        mock_path = "Tests/Mock_Data/Data/"
        answers_list = ("my_data", "my_filename")
        mock_key = "zikiSlbESf_d8snWqiT9PvjbiyJuHY_EEblm-fvdFE4="

        create_binary = EncryptToFile()
        create_binary.data_path = mock_path
        create_binary.create_file(mock_key, answers_list)

        # Create path with filename and .bin
        complete_path = f"{create_binary.data_path}{answers_list[1]}.bin"
        print(complete_path)

        # Check if file was created
        binary_file = Path(complete_path)
        if binary_file.is_file():
            file_exists = True

        self.assertTrue(file_exists, f"'my_filename.bin' should exist in {binary_file}")
        # Clean up directory
        os.remove(complete_path)

    def test_6_remove_extension_1(self):
        """Test formatting the filename String"""
        answers_list = ("my_data", "my_filename")
        mock_output = "my_filename"
        create_binary = EncryptToFile()
        filename = create_binary.remove_extension(answers_list)

        self.assertEqual(filename, mock_output, f"Should be String: '{mock_output}'")

    def test_6_remove_extension_2(self):
        """Test formatting the filename String"""
        answers_list = ("my_data", "my_filename.bin")
        mock_output = "my_filename"
        create_binary = EncryptToFile()
        filename = create_binary.remove_extension(answers_list)

        self.assertEqual(filename, mock_output, f"Should be String: '{mock_output}'")

    @patch("inquirer.prompt", return_value={"multiple_files_options": "Yes"})
    def test_7_multiple_files_prompt_1(self, mock_inquirer_prompt):
        """Test returned value from inquirer prompt is a Boolean"""

        create_binary = EncryptToFile()
        result = create_binary.multiple_files_prompt()

        valid_bool = None

        if (type(result)) == bool:
            valid_bool = True

        self.assertTrue(valid_bool, "'result' should be a Boolean")

    @patch("inquirer.prompt", return_value={"multiple_files_options": "Yes"})
    def test_7_multiple_files_prompt_2(self, mock_inquirer_prompt):
        """Test Yes option returns True"""

        create_binary = EncryptToFile()
        result = create_binary.multiple_files_prompt()

        self.assertTrue(result, "'result' should be a Boolean: True")

    @patch("inquirer.prompt", return_value={"multiple_files_options": "No"})
    def test_7_multiple_files_prompt_3(self, mock_inquirer_prompt):
        """Test No option returns False"""

        create_binary = EncryptToFile()
        result = create_binary.multiple_files_prompt()

        self.assertFalse(result, "'result' should be a Boolean: False")


if __name__ == "__main__":
    unittest.main()
