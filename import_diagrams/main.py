import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helpers.helper_menu import clear_screen, menu_list
from helpers.helper_print import print_header
from import_diagrams.to_generate.generate_tables_columns import generate_tables_columns
from import_diagrams.to_list.list_diagrams import list_diagrams


EXCLUDED_COLUMNS = {"id", "created_at", "updated_at", "deleted_at"}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # python.generator/
xml_path = os.path.join(BASE_DIR, "import_diagrams", "Truckwash.drawio.xml")



if __name__ == '__main__':

    clear_screen()
    print_header("IMPORT DIAGRAMS")

    str_input = menu_list(
        "¿Que quieres crear?: ",
        ["Listar", "Generar"]
    )

    print(f"Crear un: {str_input} ")

    if str_input.lower() == 'listar':
        list_diagrams(xml_path, EXCLUDED_COLUMNS)
    if str_input.lower() == 'generar':
        generate_tables_columns(xml_path, EXCLUDED_COLUMNS)


    print("✅ Bye...")


## /Users/dorian/PhpstormProjects81/docker-laravel-84/projects/api.truckwashvilamalla.eu/

## /Users/dorian/ReactProjects/office.truckwashvilamalla.eu/

## dorian.gonzalez@globaltank.eu