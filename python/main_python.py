import sys
import os

from python.to_create_project.start_project_python import start_project_python

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from helpers.helper_print import print_header
from helpers.helper_menu import menu_list, clear_screen


def main_python():
    """Menú principal para generar código (proyectos / módulos)."""

    while True:
        clear_screen()
        print_header("main_python")

        str_input = menu_list(
            "¿Qué quieres crear?: ",
            [
                {"name": "Proyecto", "value": "project"},
                {"name": "Módulo CRUD", "value": "crud"},
                {"name": "Volver", "value": "back"},
            ]
        )

        opt = str_input.strip().lower()

        print(f"Crear un: {str_input} ")

        if opt == 'project':
            pass
            start_project_python()
            
        elif opt == 'crud':
            pass
            # start_module_X()
            
        elif opt == 'back':
            print("\nVolviendo al menú anterior...\n")
            break

        else:
            print("Opción no reconocida.")


if __name__ == "__main__":
    main_python()