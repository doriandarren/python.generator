import sys
import os

from react_native.start_react_native import start_react_native

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from export_diagrams.main import start_export_diagrams
from import_diagrams.main import start_import_diagrams
from react.main import start_react
from react_ts.main import start_react_ts
from helpers.helper_menu import clear_screen, menu_list
from helpers.helper_print import print_header
from php.main import start_php


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
            {"name": "Salir", "value": "salir"},
        ])

        match opt:
            case "export_diagrams":
                start_export_diagrams()
            case "import_diagrams":
                start_import_diagrams()
            case "php":
                start_php()
            case "react":
                start_react()
            case "react_ts":
                start_react_ts()
            case "react_native":
                start_react_native()
            case "salir" | None:
                break
            case _:
                # por seguridad si llega algo raro
                pass

    print("\nBye...")


if __name__ == "__main__":
    start()
