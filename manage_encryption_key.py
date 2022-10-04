import time
from Modules.clear_terminal import clear_screen
from Modules.main_menu import MainMenu
from Modules.generate_key import GenerateKey
from Modules.settings import Settings


def main():
    while True:
        """Clear terminal screen"""
        clear_screen()

        """Check for existing config.json"""
        Settings()

        """Check for existing key"""
        key_check = GenerateKey()
        if key_check.check_for_existing_key() == False:
            print("Encryption Key file not found!")
            print("Create new .env file")
            key_check.create_key_workflow()

        """Launch main menu options"""
        main_menu = MainMenu()
        main_menu.main_menu_options()

        """Exit options"""
        exit_list = ["e", "exit", "quit", "exit()", "quit()"]

        """Get user response"""
        user_input = input(" Pick a Letter: ")
        user_input = user_input.lower()  # sanitize input

        """User input"""
        if user_input == "a":
            clear_screen()
            main_menu.option_a()
            time.sleep(1)
        elif user_input == "b":
            clear_screen()
            main_menu.option_b()
            time.sleep(1)
        elif user_input == "c":
            clear_screen()
            main_menu.option_c()
            time.sleep(1)
        elif user_input == "d":
            clear_screen()
            main_menu.option_d()
            time.sleep(1)
        elif user_input in exit_list:
            exit()
        else:
            print("Invalid Input!")
            time.sleep(2)


if __name__ == "__main__":
    main()
