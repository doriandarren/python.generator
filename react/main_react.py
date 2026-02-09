import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from helpers.helper_print import print_header
from helpers.helper_menu import menu_list, clear_screen
from react.to_create_module_crud.start_module_react import start_module_react
from react.to_create_module_single.start_module_single_react import start_module_single_react
from react.to_create_project.start_project_react import start_project_react


def main_react():
    """Menú principal para generar código (proyectos / módulos)."""

    while True:
        clear_screen()
        print_header("REACT")

        str_input = menu_list(
            "¿Qué quieres crear?: ",
            [
                {"name": "Proyecto", "value": "project"},
                {"name": "Módulo CRUD", "value": "crud"},
                {"name": "Módulo SINGLE", "value": "single"},
                {"name": "Volver", "value": "back"},
            ]
        )

        opt = str_input.strip().lower()

        print(f"Crear un: {str_input} ")

        if opt == 'project':
            start_project_react()
            
        elif opt == 'crud':
            start_module_react()
            
        elif opt == 'single':
            start_module_single_react()
            
        elif opt == 'back':
            print("\nVolviendo al menú anterior...\n")
            break

        else:
            print("Opción no reconocida.")

        


# if __name__ == "__main__":
#     main_react()
