import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helpers.helper_menu import menu_list, clear_screen
from helpers.helper_print import print_header
from react.to_create_module.start_module import start_module
from react.to_create_project.start_project import start_project




if __name__ == "__main__":

    clear_screen()
    print_header("REACT")

    str_input = menu_list(
        "¿Que quieres crear?: ",
        ["Proyecto", "Modulo"]
    )

    print(f"Crear un: {str_input} ")

    if str_input.lower() == 'proyecto':
        start_project()
    if str_input.lower() == 'modulo':
        start_module()

    print("Bye...")




# portuarios-office.globalfleet.es
# AgendaUnloading / AgendaUnloadings : transporeon_code name msoft_code
# AgendaUpload / AgendaUploads : transporeon_code name msoft_code
# Service / Services : description service_code
# Item / Items : description transporeon_item_id msoft_item_id
# Tow / Tows : transporeon_plate msoft_plate