import os
import unittest
from unittest.mock import patch
from Modules.decrypt_data import DecryptFile

# TO RUN TESTS:
# Make sure __init__.py is in Tests folder
# In root directory, run command: python -m unittest
# This will discover and run all tests in the project
# NOTE: The tests run by number or alphabetically order


class TestDecryptData(unittest.TestCase):
    """This class is used to test functions in Modules/decrypt_data.py"""

    @patch.dict(os.environ, {"TEMP_VAR": "mytemp"}, clear=True)  # Clears os environmental variable
    def test_1_load_key_1(self):
        """Test loading missing .env"""
        mock_dotenv_path = ""

        # setup mock path variable
        decrypt_file = DecryptFile()
        decrypt_file.dotenv_path = mock_dotenv_path

        with self.assertRaises(SystemExit):
            decrypt_file.load_key()

    def test_1_load_key_2(self):
        """Test loading the a mock .env"""
        mock_dotenv_path = "Tests/Mock_Data/mock_.env"
        mock_key = "zikiSlbESf_d8snWqiT9PvjbiyJuHY_EEblm-fvdFE4="

        # setup mock path variable
        decrypt_file = DecryptFile()
        decrypt_file.dotenv_path = mock_dotenv_path
        result = decrypt_file.load_key()

        self.assertEqual(result, mock_key, f"Should be String: '{mock_key}'")

    def test_1_load_key_3(self):
        """Test loading the .env into a String"""
        decrypt_file = DecryptFile()
        result = decrypt_file.load_key()

        valid_str = None

        if (type(result)) == str:
            valid_str = True

        self.assertTrue(valid_str, "'result' should be a String")

    def test_2_get_files_1(self):
        """Test returning a list"""

        decrypt_file = DecryptFile()
        result = decrypt_file.get_files()

        valid_list = None

        if (type(result)) == list:
            valid_list = True

        self.assertTrue(valid_list, "'result' should be a List")

    def test_2_get_files_2(self):
        """Test the returned items match files in Data folder"""
        mock_file_path = "Tests/Mock_Data/Data/"

        decrypt_file = DecryptFile()
        decrypt_file.data_path = mock_file_path
        results = decrypt_file.get_files()

        self.assertEqual(results[0], ".gitkeep", "Should be String: '.gitkeep'")
        self.assertEqual(results[1], "test.bin", "Should be String: 'test.bin'")

    def test_3_decrypt_files_1(self):
        """Test that None is returned when running function"""
        key = "zikiSlbESf_d8snWqiT9PvjbiyJuHY_EEblm-fvdFE4="
        file_list = [".gitkeep", "test.bin"]
        decrypt_file = DecryptFile()
        result = decrypt_file.decrypt_files(key, file_list)
        self.assertIsNone(result, "'result' should return None")

    mock_data: str = "RandomText"

    @patch("builtins.input", return_value=mock_data)
    def test_4_user_done_1(self, mock_user_input):
        """Test user entering ANY data into prompt to return to Main Menu"""

        decrypt_file = DecryptFile()
        result = decrypt_file.user_done()
        self.assertIsNone(result, "'result' should return None")


if __name__ == "__main__":
    unittest.main()
