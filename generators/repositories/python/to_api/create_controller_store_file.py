import os

def create_controllers_structure(base_path, plural_name_snake):
    # Crear la carpeta 'controllers' si no existe
    controllers_path = os.path.join(base_path, 'controllers')
    if not os.path.exists(controllers_path):
        os.makedirs(controllers_path)
        print(f"Carpeta 'controllers' creada en: {controllers_path}")

    # Crear la carpeta con el nombre plural_name_snake dentro de 'controllers'
    specific_controller_path = os.path.join(controllers_path, plural_name_snake)
    if not os.path.exists(specific_controller_path):
        os.makedirs(specific_controller_path)
        print(f"Carpeta '{plural_name_snake}' creada en: {specific_controller_path}")

    # Crear el archivo '__init__.py' en cada carpeta para que sean módulos de Python
    init_paths = [controllers_path, specific_controller_path]
    for path in init_paths:
        init_file = os.path.join(path, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write('# Este archivo convierte a la carpeta en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file}")

    return specific_controller_path


def generate_controller_store_file(base_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, namespace, app_name):
    # Crear la estructura de carpetas para los controladores
    controller_path = create_controllers_structure(base_path, plural_name_snake)

    # Nombre del archivo del controlador (en singular y en snake_case)
    controller_file_path = os.path.join(controller_path, f'{singular_name_snake}_store_controller.py')

    # Construir el contenido del archivo del controlador
    controller_content = f"""
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ...repositories.{plural_name_snake}.{singular_name_snake}_repository import {singular_name}Repository
import json

@method_decorator(csrf_exempt, name='dispatch')  # Excluir CSRF para simplificar
class {singular_name}StoreController(View):

    def post(self, request):
        # Obtener los datos del cuerpo de la solicitud
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({{
                'success': False,
                'message': 'Invalid JSON data'
            }}, status=400)

        # Llamar al método store del repositorio para crear el registro
        repository = {singular_name}Repository()
        new_record = repository.store(data)

        return JsonResponse({{
            'success': True,
            'message': '{singular_name} created successfully',
            'data': {{'id': new_record.id}}
        }}, status=201)
    """

    # Escribir el archivo del controlador
    try:
        with open(controller_file_path, 'w') as controller_file:
            controller_file.write(controller_content.strip())
            print(f"Archivo de controlador '{singular_name_snake}_store_controller.py' creado en: {controller_file_path}")
    except Exception as e:
        print(f"Error al crear el archivo de controlador '{singular_name_snake}_store_controller.py': {e}")
