import unittest
from unittest.mock import patch
from Modules.settings import Settings

# TO RUN TESTS:
# Make sure __init__.py is in Tests folder
# In root directory, run command: python -m unittest
# This will discover and run all tests in the project
# NOTE: The tests run by number or alphabetically order


class TestSettings(unittest.TestCase):
    """This class is used to test functions in Modules/settings.py"""

    def test_1_init_verify_config_exists_1(self):
        """Test that returned value type is boolean"""
        update_settings = Settings()
        result = update_settings.verify_config_exists()

        valid_bool = None

        if (type(result)) == bool:
            valid_bool = True

        self.assertTrue(valid_bool, "'result' should be a Boolean")

    def test_1_init_verify_config_exists_2(self):
        """Verify that the app exits if no config file is found"""
        update_settings = Settings()

        # Change config_file to mock location
        mock_location = "Settings/mycrazymadeuplocation.json"
        update_settings.config_file = mock_location

        with self.assertRaises(SystemExit):
            update_settings.verify_config_exists()

    def test_2_settings_1(self):
        """Test that the config file can be loaded into a dictionary"""
        update_settings = Settings()
        result = update_settings.settings()

        valid_dict = None

        if (type(result)) == dict:
            valid_dict = True

        self.assertTrue(valid_dict, "'result' should be a Dictionary")

    @patch("inquirer.prompt", return_value={"settings_options": "--Main Menu--"})
    def test_3_update_settings_inquirer_prompt_1(self, mock_inquirer_prompt):
        """Test inquirer prompt by pressing --Main Menu--"""
        choice = "--Main Menu--"
        update_settings = Settings()
        result = update_settings.update_settings_inquirer_prompt()

        self.assertEqual(result, choice, "Should be String: '--Main Menu--'")

    @patch("inquirer.prompt", return_value={"settings_options": "Binary Save Location"})
    def test_3_update_settings_inquirer_prompt_2(self, mock_inquirer_prompt):
        """Test inquirer prompt by pressing Binary Save Location"""
        choice = "Binary Save Location"
        update_settings = Settings()

        result = update_settings.update_settings_inquirer_prompt()

        self.assertEqual(result, choice, "Should be String: 'Binary Save Location'")

    new_loc: str = "Data/"

    @patch("builtins.input", return_value=new_loc)
    def test_4_get_new_binary_path_1(self, mock_user_input):
        """Test user input prompt for new path"""
        new_location = "Data/"
        update_settings = Settings()
        result = update_settings.get_new_binary_path()

        self.assertEqual(result, new_location, "Should be String: 'Data/'")

    def test_5_format_binary_path_1(self):
        """Test if user typed a cancel command to return to the Main Menu"""
        cancel_list = ["e", "exit", "quit", "exit()", "quit()", "cancel", "back"]

        for item in cancel_list:
            update_settings = Settings()
            result = update_settings.format_binary_path(item)
            self.assertIsNone(result, "'result' should return None")

    def test_5_format_binary_path_2(self):
        """Add a slash if the provided binary path didn't have one"""
        mock_binary_path = "test"  # no slash

        update_settings = Settings()
        result = update_settings.format_binary_path(mock_binary_path)

        expected_result = "test/"
        self.assertEqual(result, expected_result, "Should be String: 'test/'")

    def test_5_format_binary_path_3(self):
        """Replace backslash with forward slash"""
        mock_binary_path = "test\\"  # backslash

        update_settings = Settings()
        result = update_settings.format_binary_path(mock_binary_path)

        expected_result = "test/"
        self.assertEqual(result, expected_result, "Should be String: 'test/'")

    def test_5_format_binary_path_4(self):
        """Replace double forward slash with single foward slash"""
        mock_binary_path = "test//"  # double forward slash

        update_settings = Settings()
        result = update_settings.format_binary_path(mock_binary_path)

        expected_result = "test/"
        self.assertEqual(result, expected_result, "Should be String: 'test/'")

    def test_6_update_binary_path_1(self):
        """Test writing data to file"""
        mock_settings_path = "Tests/Mock_Data/Settings/config.json"
        update_settings = Settings()

        path_list = ["test/", "Data/"]

        for path in path_list:
            # Change settings to "test/" or "Data/"
            mock_formatted_binary_path = path
            update_settings.config_file = mock_settings_path
            update_settings.update_binary_path(mock_formatted_binary_path)

            # Build dictionary from mock config_file to grab path_dir data location
            config_file: dict[str, str] = update_settings.settings()
            binary_path: str = config_file["path_dir"]["data"]

            self.assertEqual(binary_path, mock_formatted_binary_path, f"Should be String: '{path}'")


if __name__ == "__main__":
    unittest.main()
