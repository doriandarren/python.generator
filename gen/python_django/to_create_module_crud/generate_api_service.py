import os
from gen.python_django.helpers.helper_file import helper_create_init_file
from helpers.helper_print import print_message, GREEN, CYAN







def generate_api_service(
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
    
    create_init_file(full_path, plural_name_snake)
    
    
    create_file(
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
    )



def create_init_file(full_path, plural_name_snake):
    print_message("Instalando app...", CYAN)

    apps_path = os.path.join(full_path, "apps", plural_name_snake, "services")
    os.makedirs(apps_path, exist_ok=True)

    helper_create_init_file(apps_path) 



def create_file(
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

    folder_path = os.path.join(full_path, "apps", plural_name_snake, "services")
    file_path = os.path.join(folder_path, singular_name_snake + "_service.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''from apps.{plural_name_snake}.models import {singular_name}

class {singular_name}Service:

    def list(self):
        return {singular_name}.objects.all()


    def show(self, id):
        return {singular_name}.objects.filter(id=id).first()


    def store(self, model: {singular_name}):
        model.save()
        return model


    def update(self, id, data: dict):
        model = self.show(id)

        if not model:
            return None
'''

    for column in columns:
        column_name = column["name"]
        content += f'''
        if "{column_name}" in data:
            model.{column_name} = data["{column_name}"]
            
        '''


    content += '''
        model.save()
        return model


    def destroy(self, id) -> bool:
        model = self.show(id)

        if not model:
            return False

        model.delete()
        return True
'''

    content += f'''


    def set_{singular_name_snake}(
        self,'''

    for column in columns:
        column_name = column["name"]
        content += f'''
        {column_name},'''

    content += f'''
    ) -> {singular_name}:
        model = {singular_name}()
'''

    for column in columns:
        column_name = column["name"]
        content += f'        model.{column_name} = {column_name}\n'

    content += '''
        return model
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

