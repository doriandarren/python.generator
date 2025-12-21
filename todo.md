# Generator Project

## Flujo del proyecto

```sh
## Para proyectos
pymain -> pystart -> pystartproject -> pygenerate

## Para modulos
pymain -> pystart -> pystartmodule -> pystandard -> pygenerate
```

# Pasos:

```sh
1. crear carpeta proyecto "xxx" y archivo "_ _ init _ _.py" y el archivo: "main_xxx"
2. crear carpetas con sus respectivos archivos "_ _ init _ _.py":

   - "to_create_module_crud"
   - "to_create_project"

3. crear dentro de la carpeta "to_create_project" el archivo: start_project_xxx.py
4. crear dentro de la carpeta "to_create_module_crud" el archivo: start_module_xxx.py

```

# TODOS:

- En PHP: cuando se crea un proyecto, se tiene que cambiar en el ".env" y en el ".env.example" lo siguientes: "LOG_CHANNEL=daily"
- en el archivo para API de postman hay que agregar en el Dev: el "execute"
- En PHP: revisar el plural cambiar a inflect por que agrega una "s" al final de la palabra de las migraciones cuando es fk

- Crear React_TS
- Crear Python

Copiar:




"Python Def": {
"prefix": "def",
"body": [
"def ${TM_FILENAME_BASE}(self, ${2}):",
"\tpass",
],
"description": "Python def"
},
"PyGenerator Main": {
"prefix": "pymain",
"body": [
"import sys",
"import os",
"",
"BASE*DIR = os.path.abspath(os.path.join(os.path.dirname(**file**), '..'))",
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
" ${TM_FILENAME_BASE}()"
],
"description": "Menú principal generador (proyectos y módulos)"
},
"PyGenerator Start Project": {
"prefix": "pystartproject",
"body": [
"from helpers.helper_menu import pause",
"from helpers.helper_print import input_with_validation",
"",
"",
"def ${TM_FILENAME_BASE}():",
" ",
" # Defaults",
" default_path = \"/Users/dorian/ReactProjects\"",
" default_name = \"app-1\"",
"",
" # Inputs",
" project_name = input_with_validation(",
" f\"Nombre del proyecto (defecto: {default_name}): \",",
" default_name",
" )",
" project_path = input_with_validation(",
" f\"Ruta del proyecto (defecto: {default_path}): \",",
" default_path",
" )",
"",
" # Split",
" full_path = f\"{project_path}/{project_name}\"",
" ",
" ## TODO llamadas a las funciones \"generate*\"",
" # generate_by_command_line(full_path)",
"",
" pause()"
],
"description": "Starter para creación de proyecto"
},
"PyGenerator Start Module": {
"prefix": "pystartmodule",
"body": [
"from helpers.helper_columns import parse_columns_input",
"from helpers.helper_menu import menu_checkbox, pause",
"from helpers.helper_print import input_with_validation",
"",
"",
"def ${TM_FILENAME_BASE}():",
"",
" opt = [",
" (\"Route\", \"route\"),",
" (\"List\", \"list\"),",
" (\"Create\", \"create\"),",
" (\"Edit\", \"edit\"),",
" (\"Barril\", \"barrel\"),",
" (\"Service\", \"service\"),",
" ]",
"",
" input_menu_checkbox = menu_checkbox(\"Componentes: \", opt)",
"",
" project_path = input_with_validation(\"Carpeta Proyecto (defecto es: /Users/dorian/ReactProjects/app-1): \", \"/Users/dorian/ReactProjects/app-1\")",
" singular_name = input_with_validation(\"Nombre singular (AgendaUnloading): \", \"AgendaUnloading\")",
" plural_name = input_with_validation(\"Nombre plural (AgendaUnloadings): \", \"AgendaUnloadings\")",
" input_columns = input_with_validation(\"Columnas: \", \"user_id:fk name age:integer description\")",
"",
" columns = parse_columns_input(input_columns)",
"",
" # TODO refactor",
" # generate_module_standard_XXX(project_path, singular_name, plural_name, columns, input_menu_checkbox)",
],
"description": "Inicializa el generador estándar de módulos CRUD en React"
},
"PyGenerator Standard": {
"prefix": "pystandard",
"body": [
"import os",
"from helpers.helper_menu import pause",
"from helpers.helper_print import camel_to_kebab, camel_to_snake",
"from helpers.helper_string import normalize_project_name",
"",
"",
"def ${TM_FILENAME_BASE}(full_path, singular_name, plural_name, columns, input_menu_checkbox=None):",
"",
" # Input Default",
" if input_menu_checkbox is None:",
" input_menu_checkbox = [\"route\", \"list\", \"create\", \"edit\", \"barrel\", \"service\"]",
"",
" # Convertir nombres",
" singular_name_kebab = camel_to_kebab(singular_name)",
" plural_name_kebab = camel_to_kebab(plural_name)",
" singular_name_snake = camel_to_snake(singular_name)",
" plural_name_snake = camel_to_snake(plural_name)",
" ",
" ## Project Name",
" temp_name = os.path.basename(full_path.rstrip(os.sep))",
" project_name = normalize_project_name(temp_name)",
" ",
"",
" # Camel (para services)",
" singular_first_camel = singular_name[:1].lower() + singular_name[1:]",
" plural_first_camel = plural_name[:1].lower() + plural_name[1:]",
"",
" # TODO refactor",
" # if \"route\" in input_menu_checkbox:",
" # create_routes(full_path, singular_name, plural_name_snake)",
"",
" # if \"list\" in input_menu_checkbox:",
" # generate_list_page(",
" # full_path,",
" # singular_name,",
" # plural_name,",
" # singular_name_kebab,",
" # plural_name_kebab,",
" # singular_name_snake,",
" # plural_name_snake,",
" # singular_first_camel,",
" # plural_first_camel,",
" # columns,",
" # )",
"",
" # if \"create\" in input_menu_checkbox:",
" # generate_create_page(",
" # full_path,",
" # singular_name,",
" # plural_name,",
" # singular_name_kebab,",
" # plural_name_kebab,",
" # singular_name_snake,",
" # plural_name_snake,",
" # singular_first_camel, # singular_name_camel",
" # plural_first_camel, # plural_name_camel",
" # columns,",
" # )",
"",
" # if \"edit\" in input_menu_checkbox:",
" # generate_edit_page(",
" # full_path,",
" # singular_name,",
" # plural_name,",
" # singular_name_kebab,",
" # plural_name_kebab,",
" # singular_name_snake,",
" # plural_name_snake,",
" # singular_first_camel,",
" # plural_first_camel,",
" # columns,",
" # )",
"",
" # if \"barrel\" in input_menu_checkbox:",
" # generate_barrel_file(full_path, singular_name, plural_name_snake)",
"",
" # if \"service\" in input_menu_checkbox:",
" # generate_service_file(",
" # full_path,",
" # project_name,",
" # singular_name,",
" # plural_name,",
" # singular_name_kebab,",
" # plural_name_kebab,",
" # singular_name_snake,",
" # plural_name_snake,",
" # singular_first_camel,",
" # plural_first_camel,",
" # columns,",
" # )",
" ",
" pause()"
],
"description": "Generador de módulo (standard)"
},
"PyGenerator Generate": {
"prefix": "pygenerate",
"body": [
"import os",
"from helpers.helper_print import print_message, GREEN, CYAN",
"",
"def ${TM_FILENAME_BASE}(",
" full_path,",
" project_name,",
" singular_name,",
" plural_name,",
" singular_name_kebab,",
" plural_name_kebab,",
" singular_name_snake,",
" plural_name_snake,",
" singular_first_camel,",
" plural_first_camel,",
" columns,",
" ):",
" \"\"\"",
" Genera el archivo",
" \"\"\"",
"",
" folder_path = os.path.join(full_path, \"src\", \"components\", \"\")",
" file_path = os.path.join(folder_path, \".jsx\")",
"",
" os.makedirs(folder_path, exist_ok=True)",
"",
" content = f'''",
" ## TODO Content",
"'''",
"",
" try:",
" with open(file_path, \"w\") as f:",
" f.write(content)",
" print_message(f\"Archivo generado: {file_path}\", GREEN)",
" except Exception as e:",
" print_message(f\"Error al generar el archivo {file_path}: {e}\", CYAN)"
],
"description": "Generador base de archivo de rutas JSX (usa full_path)"
}
