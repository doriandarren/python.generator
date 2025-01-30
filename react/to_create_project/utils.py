import subprocess


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