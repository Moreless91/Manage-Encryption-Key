import platform
import unittest
from Modules.clear_terminal import clear_screen

# TO RUN TESTS:
# Make sure __init__.py is in Tests folder
# In root directory, run command: python -m unittest
# This will discover and run all tests in the project
# NOTE: The tests run by number or alphabetically order


class TestClearTerminal(unittest.TestCase):
    """This class is used to test functions in Modules/clear_terminal.py"""

    def test_1_clear_terminal_1(self):
        """Test that returned value type is an Integer"""
        result = clear_screen()

        valid_int = None

        if (type(result)) == int:
            valid_int = True

        self.assertTrue(valid_int, "'result' should be an Integer")

    def test_1_clear_terminal_2(self):
        """Test that returned value type is correct"""
        os_dict = {"Windows": 0, "Other": 1}
        platform_os = platform.system()

        for operating_system, values in os_dict.items():
            if operating_system == platform_os:
                result = clear_screen()
                self.assertEqual(result, values, "Should be Integer: 0")
                break
            elif operating_system == platform_os:
                result = clear_screen()
                self.assertEqual(result, values, "Should be Integer: 1")
                break


if __name__ == "__main__":
    unittest.main()
