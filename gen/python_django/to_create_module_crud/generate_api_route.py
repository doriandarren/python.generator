import os
from gen.python_django.helpers.helper_file import create_init_file
from helpers.helper_print import print_message, GREEN, CYAN


def generate_api_route(
        full_path,
        project_name,
        singular_name,
        plural_name,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        singular_first_camel,
        plural_first_camel,
        columns,
    ):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", plural_name_snake, "api")
    file_path = os.path.join(folder_path, "router.py")

    os.makedirs(folder_path, exist_ok=True)
    
    create_init_file(folder_path)

    content = f'''from rest_framework.routers import DefaultRouter
from apps.{plural_name_snake}.api.views import {singular_name}ApiViewSet

# Add urls.py:
# from apps.{plural_name_snake}.api.router import router_{singular_name_snake}
# path('api/v1/', include(router_{singular_name_snake}.urls))


# example
router_{singular_name_snake} = DefaultRouter()

# examples
router_{singular_name_snake}.register(
    prefix='{plural_name_snake}',
    basename='{plural_name_snake}',
    viewset={singular_name}ApiViewSet
)
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)