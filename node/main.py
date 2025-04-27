import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helpers.helper_menu import menu_list, clear_screen
from node.to_create_project.start_project import start_project
from node.to_create_module.start_module import start_module





if __name__ == "__main__":
    clear_screen()
    print("REACT")
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