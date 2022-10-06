import os
from pathlib import Path
import unittest
from unittest.mock import patch, PropertyMock
from Modules.generate_key import GenerateKey

# TO RUN TESTS:
# Make sure __init__.py is in Tests folder
# In root directory, run command: python -m unittest
# This will discover and run all tests in the project
# NOTE: The tests run by number or alphabetically order


class TestGenerateKey(unittest.TestCase):
    """This class is used to test functions in Modules/generate_key.py"""

    def test_1_init_data_path_check(self):
        """Test that the class object data_path value updated when initialized"""
        mock_location = "Tests/Mock_Data/Settings/config.json"
        mock_path = "Data/"

        # setup mock data variable
        key_check = GenerateKey()
        key_check.config_file = mock_location
        result = key_check.data_path

        self.assertEqual(result, mock_path, "Should be String: 'Data/'")

    def test_2_check_for_existing_key_1(self):
        """Test that returned value type is a Boolean"""
        key_check = GenerateKey()
        result = key_check.check_for_existing_key()

        valid_bool = None

        if (type(result)) == bool:
            valid_bool = True

        self.assertTrue(valid_bool, "'result' should be a Boolean")

    def test_3_generate_new_key_1(self):
        """Verify a bytestring key is generating"""
        generate_key_count = 2
        key_check = GenerateKey()
        result = key_check.generate_new_key(generate_key_count)

        valid_byte = None

        if (type(result)) == bytes:
            valid_byte = True

        self.assertTrue(valid_byte, "'result' should be a ByteString")

    def test_4_write_key_to_file_1(self):
        """Test writing key to file"""
        mock_key: bytes = b"zikiSlbESf_d8snWqiT9PvjbiyJuHY_EEblm-fvdFE4="
        file_exists = None
        key_check = GenerateKey()
        key_check.env_path = "Tests/Mock_Data/.env"

        key_check.write_key_to_file(mock_key)

        # Check if file was created
        key = Path(key_check.env_path)
        if key.is_file():
            file_exists = True

        self.assertTrue(file_exists, f"'.env' should exist in {key}")
        # Clean up directory
        os.remove(key)

    @patch("inquirer.prompt", return_value={"overwrite_file_options": "Yes"})
    def test_5_overwrite_file_prompt_1(self, mock_inquirer_prompt):
        """Test returned value is a Boolean"""

        key_check = GenerateKey()
        result = key_check.overwrite_file_prompt()

        valid_bool = None

        if (type(result)) == bool:
            valid_bool = True

        self.assertTrue(valid_bool, "'result' should be a Boolean")

    @patch("inquirer.prompt", return_value={"overwrite_file_options": "Yes"})
    def test_5_overwrite_file_prompt_2(self, mock_inquirer_prompt):
        """Test Yes option returns True"""

        key_check = GenerateKey()
        result = key_check.overwrite_file_prompt()

        self.assertTrue(result, "'result' should be a Boolean: True")

    @patch("inquirer.prompt", return_value={"overwrite_file_options": "No"})
    def test_5_overwrite_file_prompt_3(self, mock_inquirer_prompt):
        """Test No option returns False"""

        key_check = GenerateKey()
        result = key_check.overwrite_file_prompt()

        self.assertFalse(result, "'result' should be a Boolean: False")

    generate_key_count: int = 5

    @patch("builtins.input", return_value=generate_key_count)
    def test_9_get_iteration_amount_1(self, mock_user_input):
        """Test retrieving amount of times a key should be generated from user"""
        generate_key_count = 5
        key_check = GenerateKey()
        result = key_check.get_iteration_amount()

        self.assertEqual(result, generate_key_count, "Should be Integer: 5")

    generate_key_count: str = "test_string"

    @patch("builtins.input", return_value=generate_key_count)
    def test_9_get_iteration_amount_2(self, mock_user_input):
        """Verify a String will return value None"""

        # Loop will run 1 time then change self.RUNNING to False
        my_side_effects = PropertyMock(side_effect=[True, False])
        GenerateKey.RUNNING = my_side_effects

        key_check = GenerateKey()
        result = key_check.get_iteration_amount()

        self.assertIsNone(result, "'result' should return None")

    generate_key_count: int = 5.5

    @patch("builtins.input", return_value=generate_key_count)
    def test_9_get_iteration_amount_3(self, mock_user_input):
        """Verify a Float will return value None"""

        # Loop will run 1 time then change self.RUNNING to False
        my_side_effects = PropertyMock(side_effect=[True, False])
        GenerateKey.RUNNING = my_side_effects

        key_check = GenerateKey()
        result = key_check.get_iteration_amount()

        self.assertIsNone(result, "'result' should return None")

    generate_key_count: int = -5

    @patch("builtins.input", return_value=generate_key_count)
    def test_9_get_iteration_amount_4(self, mock_user_input):
        """Verify a negative number will return value None"""

        # Loop will run 1 time then change self.RUNNING to False
        my_side_effects = PropertyMock(side_effect=[True, False])
        GenerateKey.RUNNING = my_side_effects

        key_check = GenerateKey()
        result = key_check.get_iteration_amount()

        self.assertIsNone(result, "'result' should return None")

    generate_key_count: int = ""

    @patch("builtins.input", return_value=generate_key_count)
    def test_9_get_iteration_amount_5(self, mock_user_input):
        """Verify an empty argument will return value None"""

        # Loop will run 1 time then change self.RUNNING to False
        my_side_effects = PropertyMock(side_effect=[True, False])
        GenerateKey.RUNNING = my_side_effects

        key_check = GenerateKey()
        result = key_check.get_iteration_amount()

        self.assertIsNone(result, "'result' should return None")


if __name__ == "__main__":
    unittest.main()
