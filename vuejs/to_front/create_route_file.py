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


def generate_route_file(ruta, namespace, path_composable, singular_name, plural_name, singular_name_kebab, plural_name_kebab,
                        singular_name_snake, plural_name_snake, columns, singular_name_first_lower,
                        plural_name_first_lower):
    """
        Genera un archivo de rutas en formato Vue.js en la ubicación especificada.

        Args:
            ruta (str): La ruta donde se guardará el archivo.
            path_composable (str): Ruta adicional que compone la ubicación final.
            plural_name_snake (str): Nombre en plural en formato snake_case.
            module_path (str): Ruta del módulo Vue.js.
            component_name (str): Nombre del componente Vue.js.
        """
    # Crear la ruta completa para el archivo de ruta
    route_file_path = os.path.join(ruta, path_composable, f"{plural_name_snake}_routes.js")

    # Asegurarse de que la ruta existe
    os.makedirs(os.path.dirname(route_file_path), exist_ok=True)

    # Contenido del archivo de ruta en formato export default para Vue.js
    route_content = f"""export default [
      {{
        path: '/{plural_name_snake}',
        name: '{plural_name_snake}',
        component: () => import('@/modules/{namespace}/views/{plural_name_kebab}/{singular_name}List.vue')
      }},
    ];
    """

    # Escribir el archivo de ruta
    with open(route_file_path, "w") as route_file:
        route_file.write(route_content)
        print(f"Archivo de ruta generado en: {route_file_path}")