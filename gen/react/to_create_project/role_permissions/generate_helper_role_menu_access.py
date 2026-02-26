import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_helper_role_menu_access(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "helpers")
    file_path = os.path.join(folder_path, "helperRoleMenuAccess.js")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""export const ROLE_MENU_ACCESS = {
  admin: { all: true },
  manager: { all: true },

  user: {
    items: ['dashboard', 'washes', 'customers'],
    children: {
      customers: ['/admin/companies', '/admin/customer-vehicles'],
    },
  },

  //TODO other roles
};
   

"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)