import os


def create_route_structure(base_ruta, path_views):
    """
    Crea la estructura de carpetas 'base_ruta/path_views' en la ruta especificada.

    Args:
        base_ruta (str): La ruta base donde se creará la estructura.
        path_views (str): La subruta específica a crear dentro de la ruta base.

    Returns:
        str: La ruta completa de la estructura de carpetas creada.
    """
    # Crear la ruta completa base_ruta/path_views
    list_folder_path = os.path.join(base_ruta, path_views)

    if not os.path.exists(list_folder_path):
        os.makedirs(list_folder_path)
        print(f"Estructura de carpetas '{list_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{list_folder_path}' ya existe.")

    return list_folder_path


def generate_route_file(ruta, namespace, path_composable, singular_name, plural_name, singular_name_kebab,
                        plural_name_kebab,
                        singular_name_snake, plural_name_snake, columns, singular_name_first_lower,
                        plural_name_first_lower):
    """
    Genera un archivo de rutas en formato Vue.js en la ubicación especificada. Si el archivo ya existe,
    agrega un nuevo objeto en el array de rutas justo antes de la última línea.

    Args:
        ruta (str): La ruta donde se guardará el archivo.
        namespace (str): Nombre del espacio de nombres del módulo.
        path_composable (str): Ruta adicional que compone la ubicación final.
        singular_name (str): Nombre en singular del recurso.
        plural_name (str): Nombre en plural del recurso.
        singular_name_kebab (str): Nombre en singular en formato kebab-case.
        plural_name_kebab (str): Nombre en plural en formato kebab-case.
        singular_name_snake (str): Nombre en singular en formato snake_case.
        plural_name_snake (str): Nombre en plural en formato snake_case.
        columns (list): Lista de columnas para el archivo.
        singular_name_first_lower (str): Nombre en singular con la primera letra en minúscula.
        plural_name_first_lower (str): Nombre en plural con la primera letra en minúscula.
    """
    # Crear la ruta completa para el archivo de ruta
    route_file_path = os.path.join(ruta, path_composable, "index.js")

    # Asegurarse de que la ruta completa para el archivo existe
    os.makedirs(os.path.dirname(route_file_path), exist_ok=True)

    # Definir el nuevo objeto que se añadirá
    new_route = f"""    {{
        path: '/{plural_name_snake}',
        name: '{plural_name_snake}',
        component: () => import('@/modules/{namespace}/views/{plural_name_kebab}/{singular_name}List.vue')
    }},
"""

    # Si el archivo no existe, crearlo con el contenido inicial y el nuevo objeto
    if not os.path.exists(route_file_path):
        with open(route_file_path, "w") as route_file:
            route_file.write("export default [\n")
            route_file.write(new_route)
            route_file.write("];\n")
        print(f"Archivo de ruta creado en: {route_file_path}")

    # Si el archivo existe, agregar el nuevo objeto justo antes de la última línea "];"
    else:
        with open(route_file_path, "r") as route_file:
            lines = route_file.readlines()

        # Insertar el nuevo objeto antes de la línea de cierre "];"
        if lines[-1].strip() == "];":
            lines.insert(-1, new_route)

        # Escribir el contenido actualizado en el archivo
        with open(route_file_path, "w") as route_file:
            route_file.writelines(lines)
        print(f"Nuevo objeto agregado al archivo de ruta en: {route_file_path}")
