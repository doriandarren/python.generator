import os
from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django
from helpers.helper_print import print_message, GREEN, CYAN


def generate_module_devs(full_path, project_name_format, app_name):
    create_module_devs(full_path, project_name_format, app_name)
    update_file_api_views(full_path, project_name_format, app_name)



def create_module_devs(full_path, project_name_format, app_name):
    """
    Crea el modulo
    """
    print_message(f"Generando el modulo de Users", CYAN)
    singular_name = "Dev"
    plural_name = "Devs"
    columns = "test"
    input_menu_checkbox = ['api_route', 'api_serializer', 'api_wiewset']
    formatColumns = parse_columns_input(columns)
    
    standard_module_crud_python_django(full_path, app_name, singular_name, plural_name, formatColumns, input_menu_checkbox)
    


def update_file_api_views(full_path, project_name_format, app_name):
    """
    Actualiza el archivo
    """
    folder_path = os.path.join(full_path, "apps", "devs", "api")
    file_path = os.path.join(folder_path, "views.py")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action


class DevApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=False, methods=['get'], url_path='test')
    def invoke(self, request):
        try:
            
            response = {
                "message": "OK"
            }
            return Response({
                'message': response,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


