import os


def generate_env(full_path):
    create_env_file(full_path)
    create_env_example_file(full_path)


def create_env_file(project_path):
    """
    Genera el archivo
    """
    file_path = os.path.join(project_path, ".env")



    # Contenido del archivo
    content = """VITE_APP_NAME=SiteLocal
VITE_APP_ENV=local
VITE_API_URL=http://project.test/api/v1/

## SWEETALERT2
VITE_SWEETALERT_COLOR_BTN_SUCCESS=#10B981  # Verde (Tailwind "emerald-500")
VITE_SWEETALERT_COLOR_BTN_DANGER=#EF4444   # Rojo (Tailwind "red-500")
VITE_SWEETALERT_COLOR_BTN_WARNING=#F59E0B  # Amarillo (Tailwind "amber-500")
VITE_SWEETALERT_COLOR_BTN_INFO=#3B82F6     # Azul (Tailwind "blue-500")
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")

def create_env_example_file(project_path):
    """
    Genera el archivo
    """
    file_path = os.path.join(project_path, ".env.example")

    # Contenido del archivo
    content = """VITE_APP_NAME=SiteLocal
VITE_APP_ENV=local
VITE_API_URL=http://project.test/api/v1/

## SWEETALERT2
VITE_SWEETALERT_COLOR_BTN_SUCCESS=#10B981  # Verde (Tailwind "emerald-500")
VITE_SWEETALERT_COLOR_BTN_DANGER=#EF4444   # Rojo (Tailwind "red-500")
VITE_SWEETALERT_COLOR_BTN_WARNING=#F59E0B  # Amarillo (Tailwind "amber-500")
VITE_SWEETALERT_COLOR_BTN_INFO=#3B82F6     # Azul (Tailwind "blue-500")
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")