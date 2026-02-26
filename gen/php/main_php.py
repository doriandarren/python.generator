import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from gen.helpers.helper_print import print_header
from gen.helpers.helper_menu import menu_list, clear_screen
from gen.php.to_module_crud.start_module_php import start_module_php
from gen.php.to_create_project.start_project_php import start_project_php
from gen.php.to_delete_module.start_module_delete_php import start_module_delete_php

def main_php():
    """Menú principal para generar código (proyectos / módulos)."""

    while True:
        clear_screen()
        print_header("main_php")

        str_input = menu_list(
            "¿Qué quieres crear?: ",
            [
                {"name": "Proyecto", "value": "project"},
                {"name": "Módulo CRUD", "value": "crud"},
                {"name": "Borrar Módulo", "value": "module_delete"},
                {"name": "Volver", "value": "back"},
            ]
        )

        opt = str_input.strip().lower()

        print(f"Crear un: {str_input} ")

        if opt == 'project':
            start_project_php()
            
        elif opt == 'crud':
            start_module_php()
            
        elif opt == 'module_delete':
            start_module_delete_php()
            
        elif opt == 'back':
            print("\nVolviendo al menú anterior...\n")
            break
        
        else:
            print("Opción no reconocida.")


if __name__ == "__main__":
    main_php()