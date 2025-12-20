import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from helpers.helper_print import print_header
from helpers.helper_menu import menu_list, clear_screen
from cpp.to_create_module_crud.start_module_crud_cpp import start_module_crud_cpp
from cpp.to_create_project.start_project_cpp import start_project_cpp


def main_cpp():
    """Menú principal para generar código (proyectos / módulos)."""

    while True:
        clear_screen()
        print_header("CPP")

        str_input = menu_list(
            "¿Qué quieres crear?: ",
            ["Proyecto", "Modulo", "<-Back"]
        )

        opt = str_input.strip().lower()

        print(f"Crear un: {str_input} ")

        if opt.startswith('proyecto'):
            start_project_cpp()

        elif opt.startswith("módulo") or opt.startswith("modulo"):
            start_module_crud_cpp()

        elif opt.startswith("<-") or opt.startswith("back"):
            print("\nVolviendo al menú anterior...\n")
            break

        else:
            print("Opción no reconocida.")

        


if __name__ == "__main__":
    main_cpp()









import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from helpers.helper_print import print_header
from helpers.helper_menu import menu_list, clear_screen


def main_cpp():
    """Menú principal para generar código (proyectos / módulos)."""

    while True:
        clear_screen()
        print_header("main_cpp")

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
            # start_project_react()
            
        elif opt == 'crud':
            pass
            # start_module_react()
            
        elif opt == 'back':
            print("\nVolviendo al menú anterior...\n")
            break

        else:
            print("Opción no reconocida.")


if __name__ == "__main__":
    main_cpp()
