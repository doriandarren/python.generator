from helpers.helper_menu import menu_list, clear_screen
from helpers.helper_print import print_header
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# from php.to_module.start_module import start_module
# from php.to_project.start_project import start_project


def start_react_ts():
    """Menú principal para generar código (proyectos / módulos)."""

    while True:
        clear_screen()
        print_header("react_ts")

        str_input = menu_list(
            "¿Qué quieres crear?: ",
            ["Proyecto", "Modulo", "<-Back"]
        )

        opt = str_input.strip().lower()

        print(f"Crear un: {str_input} ")

        if opt.startswith('proyecto'):
            pass
            # start_project()

        elif opt.startswith("módulo") or opt.startswith("modulo"):
            pass
            # start_module()

        elif opt.startswith("<-") or opt.startswith("back"):
            print("\nVolviendo al menú anterior...\n")
            break

        else:
            print("Opción no reconocida.")


if __name__ == "__main__":
    start_react_ts()
