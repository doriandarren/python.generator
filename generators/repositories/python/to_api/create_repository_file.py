# generators/repositories/python/to_api/create_repository_file.py

import os


def create_repository(base_path, plural_name):
    # Ruta completa para la carpeta 'repositories' y luego la subcarpeta con el nombre plural
    repositories_path = os.path.join(base_path, 'repositories')
    repository_folder_path = os.path.join(repositories_path, plural_name.lower())

    # Verificar si la carpeta 'repositories' ya existe, si no, crearla y agregar __init__.py
    if not os.path.exists(repositories_path):
        try:
            os.makedirs(repositories_path)
            print(f"Carpeta 'repositories' creada exitosamente en: {repositories_path}")

            # Crear un archivo '__init__.py' dentro de la carpeta 'repositories'
            init_file_path = os.path.join(repositories_path, '__init__.py')
            with open(init_file_path, 'w') as init_file:
                init_file.write('# Este archivo convierte a la carpeta repositories en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file_path}")

        except Exception as e:
            print(f"Error al crear la carpeta 'repositories' o el archivo '__init__.py': {e}")

    # Verificar si la subcarpeta con el nombre plural ya existe, si no, crearla y agregar __init__.py
    if not os.path.exists(repository_folder_path):
        try:
            os.makedirs(repository_folder_path)
            print(f"Carpeta 'repositories/{plural_name}' creada exitosamente en: {repository_folder_path}")

            # Crear un archivo '__init__.py' dentro de la subcarpeta plural
            init_file_path = os.path.join(repository_folder_path, '__init__.py')
            with open(init_file_path, 'w') as init_file:
                init_file.write('# Este archivo convierte a la carpeta en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file_path}")

        except Exception as e:
            print(f"Error al crear la carpeta 'repositories/{plural_name}' o el archivo '__init__.py': {e}")
    else:
        # print(f"La carpeta 'repositories/{plural_name}' ya existe en: {repository_folder_path}")

        # Verificar si '__init__.py' existe en la subcarpeta, si no, crearlo
        init_file_path = os.path.join(repository_folder_path, '__init__.py')
        if not os.path.exists(init_file_path):
            with open(init_file_path, 'w') as init_file:
                init_file.write('# Este archivo convierte a la carpeta en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file_path}")
        # else:
        #     print(f"El archivo '__init__.py' ya existe en: {init_file_path}")

    return repository_folder_path


def generate_repository_file(base_path, singular_name, plural_name, columns):
    # Crear la carpeta 'repositories/plural_name' y obtener su ruta
    repository_folder_path = create_repository(base_path, plural_name)

    # Nombre del archivo del repository
    repository_filename = f"{singular_name.lower()}_repository.py"
    repository_filepath = os.path.join(repository_folder_path, repository_filename)

    # Contenido básico del repository
    repository_content = f"""
from api_project.models.{plural_name.lower()}.{singular_name.lower()} import {singular_name}
from datetime import datetime

class {singular_name}Repository:
    def list(self):
        return {singular_name}.objects.all().order_by('-id')[:100]

    def show(self, {singular_name.lower()}_id):
        return {singular_name}.objects.filter(id={singular_name.lower()}_id).first()

    def store(self, data):
        instance = {singular_name}(
            {generate_fields_for_store(columns)}
        )
        instance.save()
        return instance

    def update(self, {singular_name.lower()}_id, data):
        instance = {singular_name}.objects.filter(id={singular_name.lower()}_id).first()
        if not instance:
            return None

        {generate_fields_for_update(columns, singular_name.lower())}

        instance.save()
        return instance

    def destroy(self, {singular_name.lower()}_id):
        instance = {singular_name}.objects.filter(id={singular_name.lower()}_id).first()
        if instance:
            instance.delete()
            return True
        return False
"""

    # Escribir el archivo del repository
    try:
        with open(repository_filepath, 'w') as repository_file:
            repository_file.write(repository_content.strip())
            print(f"Repository '{singular_name}_repository.py' creado exitosamente en: {repository_filepath}")
    except Exception as e:
        print(f"Error al crear el archivo del repository '{singular_name}': {e}")


def generate_fields_for_store(columns):
    # Genera las líneas para asignar valores al crear una nueva instancia
    return ",\n            ".join([f"{col['name']}=data.get('{col['name']}')" for col in columns])


def generate_fields_for_update(columns, instance_name):
    # Genera las líneas para actualizar los valores en la instancia existente
    update_lines = []
    for col in columns:
        update_lines.append(f"if data.get('{col['name']}') is not None:")
        update_lines.append(f"            instance.{col['name']} = data.get('{col['name']}')")
    return "\n        ".join(update_lines)
