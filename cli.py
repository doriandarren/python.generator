import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from helpers.helper_menu import clear_screen, menu_list
from helpers.helper_print import print_header
from export_diagrams.main_export_diagrams import main_export_diagrams
from import_diagrams.main_import_diagrams import main_import_diagrams
from react.main_react import main_react
from react_ts.main_react_ts import main_react_ts
from php.main_php import main_php


def start():
    clear_screen()
    print_header("Bienvenido al Sistema")

    while True:
        opt = menu_list("Lenguajes", [
            {"name": "Import Diagrams", "value": "import_diagrams"},
            {"name": "Export Diagrams", "value": "export_diagrams"},
            {"name": "PHP", "value": "php"},
            {"name": "React", "value": "react"},
            {"name": "React TS", "value": "react_ts"},
            {"name": "React Native", "value": "react_native"},
            {"name": "CPP", "value": "cpp"},
            {"name": "Salir", "value": "salir"},
        ])

        match opt:
            case "export_diagrams":
                main_export_diagrams()
            case "import_diagrams":
                main_import_diagrams()
            case "php":
                main_php()
            case "react":
                main_react()
            case "react_ts":
                main_react_ts()
            case "salir" | None:
                break
            case _:
                # por seguridad si llega algo raro
                pass

    print("\nBye...")




if __name__ == "__main__":
    start()
