import os

def create_seeders_structure(base_path):
    # Crear la carpeta 'settings' si no existe
    database_path = os.path.join(base_path, 'settings')
    if not os.path.exists(database_path):
        os.makedirs(database_path)
        print(f"Carpeta 'settings' creada en: {database_path}")

    # Crear la carpeta 'seeders' dentro de 'settings'
    seeders_path = os.path.join(database_path, 'seeders')
    if not os.path.exists(seeders_path):
        os.makedirs(seeders_path)
        print(f"Carpeta 'seeders' creada en: {seeders_path}")

    # Crear el archivo '__init__.py' en cada carpeta para que sean módulos de Python
    init_paths = [database_path, seeders_path]
    for path in init_paths:
        init_file = os.path.join(path, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write('# Este archivo convierte a la carpeta en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file}")

    return seeders_path

def get_faker_method(column_type):
    if 'CharField' in column_type:
        return 'company'
    elif 'DecimalField' in column_type:
        return 'pydecimal(left_digits=5, right_digits=2, positive=True)'
    elif 'TextField' in column_type:
        return 'text'
    else:
        return 'word'  # Método de respaldo por si no se reconoce el tipo de campo

def generate_seeder_file(base_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, namespace, app_name, columns):
    # Crear la estructura de carpetas para los seeders
    seeders_path = create_seeders_structure(base_path)

    # Nombre del archivo del seeder
    seeder_file_path = os.path.join(seeders_path, f'{singular_name}Seeder.py')

    # Construir el contenido del archivo del seeder
    seeder_content = f"""
from faker import Faker
from {namespace}.models.{plural_name_snake}.{singular_name_snake} import {singular_name}

def create_fake_{singular_name_snake}():
    fake = Faker()

    for _ in range(10):  # Generar 10 registros falsos
        {singular_name}.objects.create(
"""

    # Recorrer las columnas y agregar los métodos de Faker correspondientes
    for column in columns:
        faker_method = get_faker_method(column['type'])
        seeder_content += f"            {column['name']}=fake.{faker_method}(),\n"

    # Cerrar la llamada a .create() y completar el seeder
    seeder_content += f"""        )
    print("10 registros falsos de {singular_name} creados con éxito.")
"""

    # Escribir el archivo del seeder
    try:
        with open(seeder_file_path, 'w') as seeder_file:
            seeder_file.write(seeder_content.strip())
            print(f"Archivo de seeder '{singular_name}Seeder.py' creado en: {seeder_file_path}")
    except Exception as e:
        print(f"Error al crear el archivo de seeder '{singular_name}Seeder.py': {e}")
