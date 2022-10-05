import unittest
from Modules.base_logger import (
    load_user_settings,
    verify_config_exists,
    current_log_level,
    overwrite_log_file,
)

# TO RUN TESTS:
# Make sure __init__.py is in Tests folder
# In root directory, run command: python -m unittest
# This will discover and run all tests in the project
# NOTE: The tests run by number or alphabetically order


class TestBaseLogger(unittest.TestCase):
    """This class is used to test functions in Modules/base_logger.py"""

    def test_1_load_user_settings_1(self):
        """Test that returned value Types"""
        settings_location = "Settings/config.json"
        verify_config_exists(settings_location)
        log_level, overwrite_log, log_location = load_user_settings(settings_location)

        log_level_valid_string = None
        overwrite_log_valid_string = None
        log_location_valid_string = None

        if (type(log_level)) == str:
            log_level_valid_string = True

        if (type(overwrite_log)) == bool:
            overwrite_log_valid_string = True

        if (type(log_location)) == str:
            log_location_valid_string = True

        self.assertTrue(log_level_valid_string, "'log_level' should be a String")
        self.assertTrue(overwrite_log_valid_string, "'overwrite_log' should be a Boolean")
        self.assertTrue(log_location_valid_string, "'log_location' should be a String")

    def test_2_load_user_settings_2(self):
        """Test that returned values are equal to the mock data settings"""
        settings_location = "Tests/Mock_Data/Settings/config.json"
        mock_log_level = "DEBUG"
        mock_overwrite_log = True
        mock_log_location = "Logs/app.log"
        log_level, overwrite_log, log_location = load_user_settings(settings_location)

        self.assertEqual(log_level, mock_log_level, "Should be string: DEBUG")
        self.assertTrue(overwrite_log, "Should be Boolean: True")
        self.assertEqual(log_location, mock_log_location, "Should be string: 'Logs/app.log'")

    def test_3_current_log_level_1(self):
        """Test that returned value is an Integer"""
        log_level = "DEBUG"
        logLevel = current_log_level(log_level)

        log_level_valid_int = None

        if (type(logLevel)) == int:
            log_level_valid_int = True

        self.assertTrue(log_level_valid_int, "'logLevel' should be an Integer")

    def test_4_current_log_level_2(self):
        """Test that returned value from the function matches the appropriate logging level numeric value"""
        log_level_list = ["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        log_level_dict = {
            "NOTSET": 0,
            "DEBUG": 10,
            "INFO": 20,
            "WARNING": 30,
            "ERROR": 40,
            "CRITICAL": 50,
        }

        for level in log_level_list:
            logLevel = current_log_level(level)

            for key, values in log_level_dict.items():
                if level == key:
                    # print(level)  # EX: NOTSET
                    # print(values)  # EX: 0 <- from dictionary
                    # print(logLevel)  # EX: 0 <- from function
                    self.assertEqual(values, logLevel, "Integers do not match")

    def test_4_overwrite_log_file_1(self):
        """Test that returned value is a String"""
        settings_location = "Settings/config.json"
        log_level, overwrite_log, log_location = load_user_settings(settings_location)
        logFilemode = overwrite_log_file(overwrite_log)

        overwrite_log_valid_str = None

        if (type(logFilemode)) == str:
            overwrite_log_valid_str = True

        self.assertTrue(overwrite_log_valid_str, "'logFilemode' should be a String")

    def test_4_overwrite_log_file_2(self):
        """Testing that a boolean value is returned"""
        settings_location = "Tests/Mock_Data/Settings/config.json"
        log_level, overwrite_log, log_location = load_user_settings(settings_location)

        self.assertTrue(overwrite_log, "Should be Boolean: True")

    def test_6_verify_config_exists_1(self):
        """Testing that the .json file exists"""
        settings_location = "Settings/config.json"
        result = verify_config_exists(settings_location)

        self.assertIsNone(result, "'result' should return None")

    def test_7_verify_config_exists_2(self):
        """Verify that the app exits if no config file is found"""

        settings_location = "Settings/mycrazymadeuplocation.json"

        with self.assertRaises(SystemExit):
            verify_config_exists(settings_location)


if __name__ == "__main__":
    unittest.main()
