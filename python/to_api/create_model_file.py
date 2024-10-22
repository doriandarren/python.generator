import os

def create_models_structure(base_path, plural_name_snake):
    # Crear la carpeta 'models' si no existe
    models_path = os.path.join(base_path, 'models')
    if not os.path.exists(models_path):
        os.makedirs(models_path)
        print(f"Carpeta 'models' creada en: {models_path}")

    # Crear la carpeta con el nombre plural_name_snake dentro de 'models'
    specific_model_path = os.path.join(models_path, plural_name_snake)
    if not os.path.exists(specific_model_path):
        os.makedirs(specific_model_path)
        print(f"Carpeta '{plural_name_snake}' creada en: {specific_model_path}")

    # Crear el archivo '__init__.py' en cada carpeta para que sean módulos de Python
    init_paths = [models_path, specific_model_path]
    for path in init_paths:
        init_file = os.path.join(path, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write('# Este archivo convierte a la carpeta en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file}")

    return specific_model_path

def generate_model_file(base_path, singular_name, plural_name, columns, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake):
    # Crear la estructura de carpetas para los modelos
    model_path = create_models_structure(base_path, plural_name_snake)

    # Nombre del archivo del modelo (en singular)
    model_file_path = os.path.join(model_path, f'{singular_name_snake}.py')

    # Construir el contenido del archivo del modelo
    model_content = f"""
from django.db import models

class {singular_name}(models.Model):
    id = models.AutoField(primary_key=True)
"""
    # Agregar las columnas adicionales
    for column in columns:
        model_content += f"    {column['name']} = models.{column['type']}\n"

    # Campos comunes para todas las tablas
    model_content += """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
"""

    # Escribir el archivo del modelo
    try:
        with open(model_file_path, 'w') as model_file:
            model_file.write(model_content.strip())
            print(f"Archivo de modelo '{singular_name_snake}.py' creado en: {model_file_path}")
    except Exception as e:
        print(f"Error al crear el archivo de modelo '{singular_name_snake}.py': {e}")
