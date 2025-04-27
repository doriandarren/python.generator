import os
from helpers.helper_print import print_message, GREEN, CYAN


def generate_enums(full_path):
    create_enum_role(full_path)
    create_enum_user_statuses(full_path)


def create_enum_role(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "enums")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "enumRole.js")

    # Contenido por defecto
    content = r"""export const EnumRole = {
  // Slugs / nombres cortos
  ADMIN: "admin",
  MANAGER: "manager",
  USER: "user",
  ERP: "erp",

  // Descripciones
  ADMIN_DESCRIPTION: "Admin",
  MANAGER_DESCRIPTION: "Manager",
  USER_DESCRIPTION: "User",
  ERP_DESCRIPTION: "Erp",

  // IDs
  ADMIN_ID: 1,
  MANAGER_ID: 2,
  USER_ID: 3,
  ERP_ID: 4,
};
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)



def create_enum_user_statuses(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "enums")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "enumUserStatuses.js")

    # Contenido por defecto
    content = r"""export const EnumUserStatus = {
  STATUS_ACTIVE_ID: 1,
  STATUS_INACTIVE_ID: 2,

  STATUS_ACTIVE_NAME: "ACTIVE",
  STATUS_INACTIVE_NAME: "INACTIVE",
};
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
