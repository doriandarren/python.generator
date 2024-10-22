import os

def create_composable_structure(base_ruta, path_composable):
    """
    Crea la estructura de carpetas 'base_ruta/src/modules/path_composable' en la ruta especificada.
    """
    # Crear la ruta completa base_ruta/src/modules/path_composable
    composable_folder_path = os.path.join(base_ruta, path_composable)

    if not os.path.exists(composable_folder_path):
        os.makedirs(composable_folder_path)
        print(f"Estructura de carpetas '{composable_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{composable_folder_path}' ya existe.")

    return composable_folder_path


def generate_composable_file(base_ruta, path_composable, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns):
    """
    Genera un archivo de composable en Vue.js basado en los nombres proporcionados y crea la estructura base_ruta/path_composable.
    """
    # Crear la estructura de carpetas llamando a create_composable_structure
    composable_folder_path = create_composable_structure(base_ruta, path_composable)

    # Nombre del archivo JS será igual a singular_name en snake_case
    file_name = f'use{singular_name}.js'
    composable_file_path = os.path.join(composable_folder_path, file_name)

    # Construir la lista de campos de las columnas
    reactive_data = ""
    for column in columns:
        field_name = column["name"]
        reactive_data += f"'{field_name}', "

    # Eliminar la última coma y espacio extra
    reactive_data = reactive_data.strip(", ")

    # Contenido del archivo de composable JS adaptado
    composable_content = f"""import {{ ref }} from 'vue';
import {{ useI18n }} from 'vue-i18n';


export default function use{singular_name}() {{

    const {singular_name_snake} = ref();
    const {plural_name_snake} = ref([]);
    const {singular_name_snake}Errors = ref([]);
    const {{ t }} = useI18n();

    const get{plural_name} = async () => {{
        {singular_name_snake}Errors.value = [];
        await fetch(`{{{{import.meta.env.VITE_API_URL}}}}{plural_name_kebab}/list`,{{
            method: 'GET',
            headers: {{
                "Content-Type": "application/json",
                "Authorization": `Bearer ${{localStorage.getItem('token')}}`
            }},
        }})
        .then(res => res.json())
        .then((res) => {{
            if (!res.success) {{
                {singular_name_snake}Errors.value = res.errors;
            }} else {{
                {plural_name_snake}.value = res.data;
            }}
        }})
        .catch((e) => {{
            {singular_name_snake}Errors.value.push(t("errors.error_internal"));
        }});
    }}


    const get{singular_name} = async (id) => {{
        {singular_name_snake}Errors.value = [];
        await fetch(`{{{{import.meta.env.VITE_API_URL}}}}{plural_name_kebab}/show/${{id}}`,{{
            method: 'GET',
            headers: {{
                "Content-Type": "application/json",
                "Authorization": `Bearer ${{localStorage.getItem('token')}}`
            }},
        }})
        .then(res => res.json())
        .then((res) => {{
            if (!res.success) {{
                {singular_name_snake}Errors.value = res.errors;
            }} else {{
                {singular_name_snake}.value = res.data;
            }}
        }})
        .catch((e) => {{
            {singular_name_snake}Errors.value.push(t("errors.error_internal"));
        }});
    }}


    const store{singular_name} = async (data) => {{
        {singular_name_snake}Errors.value = [];
        await fetch(`{{{{import.meta.env.VITE_API_URL}}}}{plural_name_kebab}/store`,{{
            method: 'POST',
            headers: {{
                "Content-Type": "application/json",
                "Authorization": `Bearer ${{localStorage.getItem('token')}}`
            }},
            body: JSON.stringify(data),
        }})
        .then(res => res.json())
        .then((res) => {{
            if (!res.success) {{
                {singular_name_snake}Errors.value = res.errors;
            }} else {{
                {singular_name_snake}.value = res.data;
            }}
        }})
        .catch((e) => {{
            {singular_name_snake}Errors.value.push(t("errors.error_internal"));
        }});
    }}


    const update{singular_name} = async (id, data) => {{
        {singular_name_snake}Errors.value = [];
        await fetch(`{{{{import.meta.env.VITE_API_URL}}}}{plural_name_kebab}/update/${{id}}`,{{
            method: 'PUT',
            headers: {{
                "Content-Type": "application/json",
                "Authorization": `Bearer ${{localStorage.getItem('token')}}`
            }},
            body: JSON.stringify(data),
        }})
        .then(res => res.json())
        .then((res) => {{
            if (!res.success) {{
                {singular_name_snake}Errors.value = res.errors;
            }} else {{
                {singular_name_snake}.value = res.data;
            }}
        }})
        .catch((e) => {{
            {singular_name_snake}Errors.value.push(t("errors.error_internal"));
        }});
    }}


    const destroy{singular_name} = async (id) => {{
        {singular_name_snake}Errors.value = [];
        await fetch(`{{{{import.meta.env.VITE_API_URL}}}}{plural_name_kebab}/delete/${{id}}`,{{
            method: 'DELETE',
            headers: {{
                "Content-Type": "application/json",
                "Authorization": `Bearer ${{localStorage.getItem('token')}}`
            }},
        }})
        .then(res => res.json())
        .then((res) => {{
            if (!res.success) {{
                {singular_name_snake}Errors.value = res.errors;
            }} else {{
                {singular_name_snake}.value = res.data;
            }}
        }})
        .catch((e) => {{
            {singular_name_snake}Errors.value.push(t("errors.error_internal"));
        }});
    }}


    return {{
        {singular_name_snake}Errors,
        {singular_name_snake},
        {plural_name_snake},
        get{singular_name},
        get{plural_name},
        store{singular_name},
        update{singular_name},
        destroy{singular_name},
    }}

}}
"""

    # Escribir el archivo de composable JS
    try:
        with open(composable_file_path, 'w') as composable_file:
            composable_file.write(composable_content)
            print(f"Archivo Vue.js composable '{file_name}' creado en: {composable_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo Vue.js composable '{file_name}': {e}")
