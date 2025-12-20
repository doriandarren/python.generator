import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from helpers.helper_print import print_header
from helpers.helper_menu import menu_list, clear_screen
from react_native.to_create_module_crud.start_module_crud_react_native import start_module_crud_react_native
from react_native.to_create_project.start_project_react_native import start_project_react_native

def main_react_native():
    """Menú principal para generar código (proyectos / módulos)."""

    while True:
        clear_screen()
        print_header("React_Native")

        str_input = menu_list(
            "¿Qué quieres crear?: ",
            ["Proyecto", "Modulo", "<-Back"]
        )

        opt = str_input.strip().lower()

        print(f"Crear un: {str_input} ")

        if opt.startswith('proyecto'):
            pass
            start_project_react_native() ## TODO refactor

        elif opt.startswith("módulo") or opt.startswith("modulo"):
            pass
            start_module_crud_react_native() ## TODO refactor

        elif opt.startswith("<-") or opt.startswith("back"):
            print("\nVolviendo al menú anterior...\n")
            break

        else:
            print("Opción no reconocida.")

        


if __name__ == "__main__":
    main_react_native()
