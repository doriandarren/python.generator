import sys
import os

from python_django.to_create_module_crud.start_module_crud_python_django import start_module_crud_python_django
from python_django.to_create_project.start_project_python_django import start_project_python_django

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from helpers.helper_print import print_header
from helpers.helper_menu import menu_list, clear_screen


def main_python_django():
    """Menú principal para generar código (proyectos / módulos)."""

    while True:
        clear_screen()
        print_header("PYTHON DJANGO")

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
            start_project_python_django()
            
        elif opt == 'crud':
            start_module_crud_python_django()
            
        elif opt == 'back':
            print("\nVolviendo al menú anterior...\n")
            break

        else:
            print("Opción no reconocida.")


if __name__ == "__main__":
    main_python_django()