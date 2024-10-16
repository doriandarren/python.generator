# generator/repositories/to_api/create_models.py

import os


def create_model(base_path):
    # Ruta completa para la carpeta 'models'
    models_path = os.path.join(base_path, 'models')

    # Verificar si la carpeta 'models' ya existe
    if not os.path.exists(models_path):
        try:
            os.makedirs(models_path)
            print(f"Carpeta 'models' creada exitosamente en: {models_path}")

            # Crear un archivo '__init__.py' dentro de 'models' para que sea un paquete de Python
            init_file_path = os.path.join(models_path, '__init__.py')
            with open(init_file_path, 'w') as init_file:
                init_file.write('# Este archivo convierte a la carpeta models en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file_path}")

        except Exception as e:
            print(f"Error al crear la carpeta 'models' o el archivo '__init__.py': {e}")
    else:
        print(f"La carpeta 'models' ya existe en: {models_path}")

        # Verificar si '__init__.py' existe, si no, crearlo
        init_file_path = os.path.join(models_path, '__init__.py')
        if not os.path.exists(init_file_path):
            with open(init_file_path, 'w') as init_file:
                init_file.write('# Este archivo convierte a la carpeta models en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file_path}")
        else:
            print(f"El archivo '__init__.py' ya existe en: {init_file_path}")


def generate_model_file(models_path, singular_name, plural_name):
    # Nombre del archivo de modelo
    model_filename = f"{singular_name.lower()}.py"
    model_filepath = os.path.join(models_path, model_filename)

    # Contenido del archivo de modelo
    model_content = f"""
from django.db import models

class {singular_name.capitalize()}(models.Model):
    # Define your fields here
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
