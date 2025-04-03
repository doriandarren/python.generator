import os
from helpers.helper_print import create_folder



def create_service_file(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns):
    """
        Genera dinámicamente el archivo de servicios {singular_name}Service.js con nombres adaptados.
        """
    # Define la ruta del archivo
    services_dir = os.path.join(project_path, "src", "modules", plural_name_snake, "services")


    file_path = os.path.join(services_dir, f"{singular_first_camel}Service.js")


    # Crear la carpeta services si no existe
    create_folder(services_dir)

    # Contenido del archivo JS con nombres dinámicos
    content = f"""import {{ api }} from "../../../api/api";

/**
 * List
 */
export const get{plural_name} = async () => {{
    try {{
        const token = localStorage.getItem("token_portuarios");
        if (!token) {{
            console.warn("No hay token disponible en localStorage");
            return [];
        }}

        const response = await api("{plural_name_kebab}/list", "GET", null, token);

        // Verificar si la API devuelve datos válidos
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

/**
 * Show
 */
export const get{singular_name}ById = async (id) => {{
    try {{
        const token = localStorage.getItem("token_portuarios");
        if (!token) return null;

        const response = await api(`{plural_name_kebab}/show/${{id}}`, "GET", null, token);
        return response;
    }} catch (error) {{
        console.error("Error al obtener el registro:", error);
        return null;
    }}
}};

/**
 * Store
 */
export const create{singular_name} = async (data) => {{
    try {{
        const token = localStorage.getItem("token_portuarios");
        if (!token) {{
            console.warn("No hay token disponible en localStorage");
            return null;
        }}

        const response = await api("{plural_name_kebab}/store", "POST", data, token);

        if (!response || typeof response !== "object") {{
            console.error("Error en la respuesta de la API:", response);
            return null;
        }}

        return response;
    }} catch (error) {{
        console.error("Error al enviar los datos:", error);
        return null;
    }}
}};

/**
 * Update
 */
export const update{singular_name} = async (id, data) => {{
    try {{
        const token = localStorage.getItem("token_portuarios");
        if (!token) return null;

        const response = await api(`{plural_name_kebab}/update/${{id}}`, "PUT", data, token);
        return response;
    }} catch (error) {{
        console.error("Error al actualizar el registro:", error);
        return null;
    }}
}};

/**
 * Delete
 */
export const delete{singular_name} = async (id) => {{
    try {{
        const token = localStorage.getItem("token_portuarios");
        if (!token) return null;

        const response = await api(`{plural_name_kebab}/delete/${{id}}`, "DELETE", null, token);
        return response;
    }} catch (error) {{
        console.error("Error al eliminar el registro:", error);
        return null;
    }}
}};
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")
