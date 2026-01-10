import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_docker_file(full_path, project_name_format):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path)
    file_path = os.path.join(folder_path, "docker-compose.yml")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''services:
  db:
    image: postgres:16-alpine
    container_name: {project_name_format}_postgres
    environment:
      POSTGRES_DB: {project_name_format}_db
      POSTGRES_USER: {project_name_format}_user
      POSTGRES_PASSWORD: {project_name_format}_pass
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)