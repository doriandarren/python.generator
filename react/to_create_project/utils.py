
# Colores para mensajes
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"
NC = "\033[0m"  # Sin color


def print_message(message, color=NC):
    print(f"{color}{message}{NC}")
