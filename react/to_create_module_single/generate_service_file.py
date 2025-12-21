import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_service_file(
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

    folder_path = os.path.join(full_path, "src", "modules", plural_name_snake, 'services')
    file_path = os.path.join(folder_path, f"{singular_first_camel}Service.js")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''import {{ api }} from "../../../api/api";

/**
 * List
 */
export const get{plural_name} = async () => {{
  try {{
    const token = localStorage.getItem("token_{project_name}");
    if (!token) {{
      console.warn("No hay token disponible en localStorage");
      return [];
    }}

    const response = await api("{plural_name_kebab}/list", "GET", null, token);

    if (!response || typeof response !== "object") {{
      console.error("Respuesta no válida de la API:", response);
      return [];
    }}

    return response;
  }} catch (error) {{
    console.error("Error al obtener los registros:", error);
    return [];
  }}
}};
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)