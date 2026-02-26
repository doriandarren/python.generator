import os
import sys
from pathlib import Path

# Ruta a tu proyecto (ajústala)
PROJECT_DIR = Path(__file__).resolve().parent

# Si tu proyecto está en otra carpeta, pon la ruta real:
# PROJECT_DIR = Path("/var/www/vhosts/TU_DOMINIO/httpdocs")

sys.path.insert(0, str(PROJECT_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
