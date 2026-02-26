import os
from dotenv import load_dotenv

# Carga .env desde la raíz del proyecto (directorio actual)
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL no está definido. Crea un archivo .env en la raíz "
        "con DATABASE_URL=postgresql+psycopg2://... o mysql+pymysql://..."
    )