import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from helpers.helper_print import print_header
from helpers.helper_menu import menu_list, clear_screen
from php.to_module.start_module_php import start_module
from php.to_project.start_project import start_project



def start_php():
    """Menú principal para generar código en PHP (proyectos / módulos)."""
    
    while True:
        clear_screen()
        print_header("PHP")

        str_input = menu_list(
            "¿Que quieres crear?: ",
            ["Proyecto", "Modulo", "<-Back"]
        )
        
        opt = str_input.strip().lower()

        print(f"Crear un: {str_input} ")

        if opt.startswith('proyecto'):
            start_project()
        
        elif opt.startswith("módulo") or opt.startswith("modulo"):
            start_module()
            
        elif opt.startswith("<-") or opt.startswith("back"):
            # Volver al menú anterior (por ejemplo, menú general de lenguajes)
            print("\nVolviendo al menú anterior...\n")
            break

        else:
            print("Opción no reconocida.")

        print("Bye...")


if __name__ == "__main__":
    start_php()