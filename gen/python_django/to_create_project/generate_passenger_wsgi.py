import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_passenger_wsgi(full_path, app_name):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path)
    file_path = os.path.join(folder_path, "passenger_wsgi.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''import os
import sys
from pathlib import Path

# Ruta a tu proyecto (ajústala)
PROJECT_DIR = Path(__file__).resolve().parent

# Si tu proyecto está en otra carpeta, pon la ruta real:
# PROJECT_DIR = Path("/var/www/vhosts/TU_DOMINIO/httpdocs")

sys.path.insert(0, str(PROJECT_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{app_name}.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)