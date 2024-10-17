import os

def create_repositories_structure(base_path, plural_name_snake):
    # Crear la carpeta 'repositories' si no existe
    repositories_path = os.path.join(base_path, 'repositories')
    if not os.path.exists(repositories_path):
        os.makedirs(repositories_path)
        print(f"Carpeta 'repositories' creada en: {repositories_path}")

    # Crear la carpeta con el nombre plural_name_snake dentro de 'repositories'
    specific_repository_path = os.path.join(repositories_path, plural_name_snake)
    if not os.path.exists(specific_repository_path):
        os.makedirs(specific_repository_path)
        print(f"Carpeta '{plural_name_snake}' creada en: {specific_repository_path}")

    # Crear el archivo '__init__.py' en cada carpeta para que sean módulos de Python
    init_paths = [repositories_path, specific_repository_path]
    for path in init_paths:
        init_file = os.path.join(path, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write('# Este archivo convierte a la carpeta en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file}")

    return specific_repository_path

def generate_repository_file(base_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, namespace, app_name):
    # Crear la estructura de carpetas para los repositorios
    repository_path = create_repositories_structure(base_path, plural_name_snake)

    # Nombre del archivo del repositorio (en singular y en snake_case)
    repository_file_path = os.path.join(repository_path, f'{singular_name_snake}_repository.py')

    # Construir el contenido del archivo del repositorio
    repository_content = f"""
from {namespace}.{app_name}.models.{plural_name_snake}.{singular_name_snake} import {singular_name}

class {singular_name}Repository:

    def list(self):
        return {singular_name}.objects.all()

    def get(self, {singular_name_snake}_id):
        try:
            return {singular_name}.objects.get(id={singular_name_snake}_id)
        except {singular_name}.DoesNotExist:
            return None

    def create(self, data):
        {singular_name_snake} = {singular_name}(**data)
        {singular_name_snake}.save()
        return {singular_name_snake}

    def update(self, {singular_name_snake}_id, data):
        {singular_name_snake} = self.get({singular_name_snake}_id)
        if {singular_name_snake}:
            for key, value in data.items():
                setattr({singular_name_snake}, key, value)
            {singular_name_snake}.save()
        return {singular_name_snake}

    def delete(self, {singular_name_snake}_id):
        {singular_name_snake} = self.get({singular_name_snake}_id)
        if {singular_name_snake}:
            {singular_name_snake}.delete()
        return {singular_name_snake}
"""

    # Escribir el archivo del repositorio
    try:
        with open(repository_file_path, 'w') as repository_file:
            repository_file.write(repository_content.strip())
            print(f"Archivo de repositorio '{singular_name_snake}_repository.py' creado en: {repository_file_path}")
    except Exception as e:
        print(f"Error al crear el archivo de repositorio '{singular_name_snake}_repository.py': {e}")
