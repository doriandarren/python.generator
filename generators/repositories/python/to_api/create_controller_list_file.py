import os


def create_controller(base_path, plural_name):
    # Ruta completa para la carpeta 'controllers' y luego la subcarpeta con el nombre plural
    controllers_path = os.path.join(base_path, 'controllers')
    controller_folder_path = os.path.join(controllers_path, plural_name.lower())

    # Verificar si la carpeta 'controllers' ya existe, si no, crearla y agregar __init__.py
    if not os.path.exists(controllers_path):
        try:
            os.makedirs(controllers_path)
            print(f"Carpeta 'controllers' creada exitosamente en: {controllers_path}")

            # Crear un archivo '__init__.py' dentro de la carpeta 'controllers'
            init_file_path = os.path.join(controllers_path, '__init__.py')
            with open(init_file_path, 'w') as init_file:
                init_file.write('# Este archivo convierte a la carpeta controllers en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file_path}")

        except Exception as e:
            print(f"Error al crear la carpeta 'controllers' o el archivo '__init__.py': {e}")

    # Verificar si la subcarpeta con el nombre plural ya existe, si no, crearla y agregar __init__.py
    if not os.path.exists(controller_folder_path):
        try:
            os.makedirs(controller_folder_path)
            print(f"Carpeta 'controllers/{plural_name}' creada exitosamente en: {controller_folder_path}")

            # Crear un archivo '__init__.py' dentro de la subcarpeta plural
            init_file_path = os.path.join(controller_folder_path, '__init__.py')
            with open(init_file_path, 'w') as init_file:
                init_file.write('# Este archivo convierte a la carpeta en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file_path}")

        except Exception as e:
            print(f"Error al crear la carpeta 'controllers/{plural_name}' o el archivo '__init__.py': {e}")
    else:
        # print(f"La carpeta 'controllers/{plural_name}' ya existe en: {controller_folder_path}")

        # Verificar si '__init__.py' existe en la subcarpeta, si no, crearlo
        init_file_path = os.path.join(controller_folder_path, '__init__.py')
        if not os.path.exists(init_file_path):
            with open(init_file_path, 'w') as init_file:
                init_file.write('# Este archivo convierte a la carpeta en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file_path}")
        # else:
        #     print(f"El archivo '__init__.py' ya existe en: {init_file_path}")

    return controller_folder_path


def generate_controller_list_file(base_path, singular_name, plural_name):
    # Crear la carpeta 'controllers/plural_name' y obtener su ruta
    controller_folder_path = create_controller(base_path, plural_name)

    # Nombre del archivo del controlador
    controller_filename = f"{singular_name.lower()}_list_controller.py"
    controller_filepath = os.path.join(controller_folder_path, controller_filename)

    # Contenido básico del controlador que extiende de BaseController en shared
    controller_content = f"""
from shared.base_controller import BaseController
from repositories.{plural_name.lower()}.{singular_name.lower()}_repository import {singular_name}Repository

class {singular_name}ListController(BaseController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = {singular_name}Repository()

    def get(self, request):
        data = self.repository.list()
        return self.respond_with_data('{plural_name} list', data)
"""

    # Escribir el archivo del controlador
    try:
        with open(controller_filepath, 'w') as controller_file:
            controller_file.write(controller_content.strip())
            print(f"Controlador '{singular_name}_list_controller.py' creado exitosamente en: {controller_filepath}")
    except Exception as e:
        print(f"Error al crear el archivo del controlador '{singular_name}': {e}")
