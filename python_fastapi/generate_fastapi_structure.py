import os


def create_folder_structure(base_path):
    """
    Crea la estructura de carpetas para un proyecto FastAPI.
    :param base_path: Ruta donde se creará el proyecto (última carpeta será el nombre del proyecto).
    """
    # Obtener el nombre del proyecto de la ruta
    project_name = os.path.basename(os.path.normpath(base_path))

    # Definir la estructura

    structure = [
        f"{base_path}/app",                     # Carpeta raíz para toda la lógica de la aplicación
        f"{base_path}/app/api/v1/endpoints",    # Endpoints organizados por versión y recursos
        f"{base_path}/app/core",                # Configuración central (e.g., config.py, middlewares)
        f"{base_path}/app/db",                  # Manejo de base de datos (modelos, sesiones, inicialización)
        f"{base_path}/app/schemas",             # Validación y definición de datos con Pydantic
        f"{base_path}/app/services",            # Lógica de negocio separada de los controladores
        f"{base_path}/app/integrations",        # Conexiones con APIs externas o servicios de terceros
        f"{base_path}/tests",                   # Pruebas unitarias y de integración del proyecto
    ]

    # Crear las carpetas
    for folder in structure:
        os.makedirs(folder, exist_ok=True)
        print(f"Carpeta creada: {folder}")

    # Crear archivos iniciales
    files = {
        f"{base_path}/app/main.py": main_template(project_name),
        f"{base_path}/app/api/v1/endpoints/__init__.py": "",
        f"{base_path}/app/core/config.py": config_template(),
        f"{base_path}/app/db/__init__.py": "",
        f"{base_path}/app/schemas/__init__.py": "",
        f"{base_path}/app/services/__init__.py": "",
        f"{base_path}/tests/__init__.py": "",
        f"{base_path}/.env": "SECRET_KEY=your_secret_key\n",
        f"{base_path}/requirements.txt": requirements_template(),
        f"{base_path}/README.md": f"# {project_name}\n\nGenerado con FastAPI.",
    }

    for file_path, content in files.items():
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")


def main_template(project_name):
    return f"""from fastapi import FastAPI
from app.api.v1.endpoints import example

app = FastAPI(
    title="{project_name}",
    description="API generada automáticamente",
    version="1.0.0"
)

app.include_router(example.router, prefix="/example", tags=["Example"])
"""


def config_template():
    return """from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Project"
    SECRET_KEY: str = "your_secret_key"

    class Config:
        env_file = ".env"

settings = Settings()
"""


def requirements_template():
    return """fastapi
uvicorn[standard]
pydantic
sqlalchemy
python-dotenv
"""


# Ejecutar el script
if __name__ == "__main__":
    base_path = input("Ruta proyecto ( Ex. /Users/dorian/PythonProjects/FastAPI ): ").strip()
    create_folder_structure(base_path)
    print(f"Estructura del proyecto creada con éxito en '{base_path}'.")
