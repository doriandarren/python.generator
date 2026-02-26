import os
from gen.helpers.helper_print import create_folder



def create_barrel_file(project_path, singular_name, plural_name_snake):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", plural_name_snake, "pages")
    file_path = os.path.join(routes_dir, "index.js")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo
    content = f"""export * from './{singular_name}Page';
export * from './{singular_name}CreatePage';
export * from './{singular_name}EditPage';
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")
