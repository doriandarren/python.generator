# generator/repositories/to_api/create_models.py

import os


def create_model(base_path, plural_name):
    # Ruta completa para la carpeta con el nombre plural
    model_folder_path = os.path.join(base_path, plural_name.lower())

    # Verificar si la carpeta ya existe, si no, crearla
    if not os.path.exists(model_folder_path):
        try:
            os.makedirs(model_folder_path)
            print(f"Carpeta '{plural_name}' creada exitosamente en: {model_folder_path}")

            # Crear un archivo '__init__.py' dentro de la carpeta plural
            init_file_path = os.path.join(model_folder_path, '__init__.py')
            with open(init_file_path, 'w') as init_file:
                init_file.write('# Este archivo convierte a la carpeta en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file_path}")

        except Exception as e:
            print(f"Error al crear la carpeta '{plural_name}' o el archivo '__init__.py': {e}")
    else:
        print(f"La carpeta '{plural_name}' ya existe en: {model_folder_path}")

        # Verificar si '__init__.py' existe, si no, crearlo
        init_file_path = os.path.join(model_folder_path, '__init__.py')
        if not os.path.exists(init_file_path):
            with open(init_file_path, 'w') as init_file:
                init_file.write('# Este archivo convierte a la carpeta en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file_path}")
        else:
            print(f"El archivo '__init__.py' ya existe en: {init_file_path}")

    return model_folder_path


def generate_model_file(models_path, singular_name, plural_name, columns):
    # Crear la carpeta plural_name y obtener su ruta
    model_folder_path = create_model(models_path, plural_name)

    # Nombre del archivo de modelo
    model_filename = f"{singular_name.lower()}.py"
    model_filepath = os.path.join(model_folder_path, model_filename)

    # Generar las líneas para las columnas
    column_lines = "\n    ".join([f"{col['name']} = models.{col['type']}" for col in columns])

    # Contenido del archivo de modelo
    model_content = f"""
from django.db import models

class {singular_name.capitalize()}(models.Model):
    {column_lines}

    class Meta:
        verbose_name = '{singular_name}'
        verbose_name_plural = '{plural_name}'
        db_table = '{plural_name.lower()}'

    def __str__(self):
        return self.name
"""

    # Escribir el archivo de modelo
    try:
        with open(model_filepath, 'w') as model_file:
            model_file.write(model_content.strip())
            print(f"Modelo '{singular_name}' creado exitosamente en: {model_filepath}")
    except Exception as e:
        print(f"Error al crear el archivo del modelo '{singular_name}': {e}")
