import os
from gen.helpers.helpers import dd
from helpers.helper_print import print_message, GREEN, CYAN

def generate_api_serializer(
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
    file_path = os.path.join(folder_path, "serializers.py")

    os.makedirs(folder_path, exist_ok=True)
    
    
    format_cols = ",".join(f"'{col["name"]}'" for col in columns)

      

    content = f'''from rest_framework.serializers import ModelSerializer
from apps.{plural_name_snake}.models import {singular_name}


class {singular_first_camel}Serializer(ModelSerializer):

    class Meta:
        model = {singular_name}
        ## fields = "__all__"
        fields = ['id', {format_cols}]
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)