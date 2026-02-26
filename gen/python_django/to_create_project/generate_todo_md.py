import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_todo_md(full_path, project_name):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path,)
    file_path = os.path.join(folder_path, "todo.md")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''# {project_name}

```sh

```

## TODOS Pendientes:
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)