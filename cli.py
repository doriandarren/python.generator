import sys
import os
# Ajustar sys.path para poder importar desde el proyecto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from react.main import start_react
from react_ts.main import start_react_ts
from helpers.helper_menu import clear_screen, menu_list
from helpers.helper_print import print_header
from php.main import start_php

def start():
    clear_screen()
    print_header("Bienvenodo al Sistema")

    while True:
        str_input = menu_list(
            "Lenguajes",
            ["PHP", "React", "React_TS", "Salir"]
        )

        opt = str_input.strip().lower()

        if opt.startswith('php'):
            start_php()

        elif opt.startswith('react'):
            start_react()
        
        elif opt.startswith('react_ts'):
            start_react_ts()

        elif opt.startswith('salir'):
            break

    print("\nBye...")


if __name__ == '__main__':
    start()
