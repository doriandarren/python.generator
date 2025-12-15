from helpers.helper_menu import menu_list, clear_screen
from helpers.helper_print import print_header
from react.to_create_module.start_module import start_module
from react.to_create_project.start_project import start_project


def start_react():
    while True:
        clear_screen()
        print_header("REACT")

        opt = menu_list(
            "¿Qué quieres crear?: ",
            ["Proyecto", "Módulo", "Volver"]
        ).strip().lower()

        if opt == "volver":
            return

        if opt == "proyecto":
            start_project()
        elif opt in ("módulo", "modulo"):
            start_module()
        else:
            print("Opción no válida.")

