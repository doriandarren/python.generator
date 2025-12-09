from php.main import start_php
from helpers.helper_print import print_header
from helpers.helper_menu import clear_screen, menu_list
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


if __name__ == '__main__':

    clear_screen()
    print_header("Bienvenodo al Sistema")

    str_input = menu_list(
        "Lenguajes",
        ["PHP", "React_TS"]
    )

    if str_input.lower() == 'php':
        start_php()
    
