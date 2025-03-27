import os
import re
import subprocess
import pprint
import sys
from colorama import Fore




# Colores para mensajes
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"
NC = "\033[0m"  # Sin color


def print_message(message, color=NC):
    print(f"{color}{message}{NC}")




def run_command(command, cwd=None):
    """Ejecuta un comando en la terminal."""
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print_message(f"Error ejecutando el comando: {command}", CYAN)
        raise e



def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print_message(f"Carpeta creada: {path}", GREEN)
    else:
        print_message(f"Carpeta ya existe: {path}", CYAN)



def camel_to_kebab(name):
    """Convierte un string CamelCase a kebab-case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()


def camel_to_snake(name):
    """Convierte un string CamelCase a snake_case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()




# Función para manejar input con validación y valores por defecto
def input_with_validation(prompt, default_value=None):
    while True:  # Bucle para solicitar una entrada válida
        if default_value:  # Si hay un valor por defecto, se muestra
            user_input = input(f"{prompt} [{default_value}]: ").strip()
            if user_input:  # Si el usuario escribe algo, lo retorna
                return user_input
            return default_value  # Si presiona Enter, usa el valor por defecto
        else:  # Si no hay un valor por defecto
            user_input = input(f"{prompt}").strip()
            if user_input:  # Si el usuario escribe algo, lo retorna
                return user_input
            print("La entrada no puede estar en blanco. Por favor, inténtalo de nuevo.")



def capitalize_camel_case(name):
    return ''.join(word.capitalize() for word in name.split('_'))




def dd(data):
    pprint.pprint(data)
    sys.exit()



def print_header(title, width=50):
    # Asegurarse que el título no sea más largo que el ancho permitido
    clean_title = f"🚀 {title}"
    if len(clean_title) > width - 4:
        width = len(clean_title) + 4

    border = '+' + '-' * (width - 1) + '+'
    empty_line = f"|{' ' * (width - 1)}|"

    # Centrar el título
    padding = (width - 2 - len(clean_title)) // 2
    line = f"|{' ' * padding}{clean_title}{' ' * (width - 2 - len(clean_title) - padding)}|"

    final_box = f"""
{border}
{empty_line}
{line}
{empty_line}
{border}
"""
    print_message(final_box, CYAN)
