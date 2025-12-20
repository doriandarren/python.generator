# Generator Project

# Pasos:

```sh
1. crear carpeta proyecto "xxx" y archivo "_ _ init _ _.py" y el archivo: "main_xxx"
2. crear carpetas con sus respectivos archivos "_ _ init _ _.py":

   - "to_create_module_crud"
   - "to_create_project"

4. crear dentro de la carpeta "to_create_project" el archivo: start_project_xxx.py
4. crear dentro de la carpeta "to_create_module_crud" el archivo: start_module_xxx.py
```

# TODOS:

- En PHP: cuando se crea un proyecto, se tiene que cambiar en el ".env" y en el ".env.example" lo siguientes: "LOG_CHANNEL=daily"
- en el archivo para API de postman hay que agregar en el Dev: el "execute"
- En PHP: revisar el plural cambiar a inflect por que agrega una "s" al final de la palabra de las migraciones cuando es fk

- Crear React_TS
- Crear Python

import os

def generate\_(project_path):
"""
Genera el archivo
"""
file_path = os.path.join(project_path, "")

    # Contenido del archivo
    content = r"""

"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")

"PyGenerator Main": {
"prefix": "pymain",
"body": [
"import sys",
"import os",
"",
"BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(**file**), '..'))",
"if BASE_DIR not in sys.path:",
" sys.path.append(BASE_DIR)",
"",
"from helpers.helper_print import print_header",
"from helpers.helper_menu import menu_list, clear_screen",
"",
"",
"def ${TM_FILENAME_BASE}():",
    "    \"\"\"Menú principal para generar código (proyectos / módulos).\"\"\"",
    "",
    "    while True:",
    "        clear_screen()",
    "        print_header(\"${TM_FILENAME_BASE}\")",
"",
" str_input = menu_list(",
" \"¿Qué quieres crear?: \",",
" [",
" {\"name\": \"Proyecto\", \"value\": \"project\"},",
" {\"name\": \"Módulo CRUD\", \"value\": \"crud\"},",
" {\"name\": \"Volver\", \"value\": \"back\"},",
" ]",
" )",
"",
" opt = str_input.strip().lower()",
"",
" print(f\"Crear un: {str_input} \")",
"",
" if opt == 'project':",
" pass",
" # start_project_react()",
" ",
" elif opt == 'crud':",
" pass",
" # start_module_react()",
" ",
" elif opt == 'back':",
" print(\"\\nVolviendo al menú anterior...\\n\")",
" break",
"",
" else:",
" print(\"Opción no reconocida.\")",
"",
"",
"if **name** == \"**main**\":",
" main_react()"
],
"description": "Menú principal generador (proyectos y módulos)"
},
