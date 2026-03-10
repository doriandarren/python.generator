import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_api_viewset(
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

    folder_path = os.path.join(full_path,  "apps", plural_name_snake, "api")
    file_path = os.path.join(folder_path, "views.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend

from apps.{plural_name_snake}.api.serializers import {singular_name}Serializer
from apps.{plural_name_snake}.models import {singular_name}


class {singular_name}ApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = {singular_name}Serializer
    queryset = {singular_name}.objects.all()
    # Filtros...
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category', 'active']
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)