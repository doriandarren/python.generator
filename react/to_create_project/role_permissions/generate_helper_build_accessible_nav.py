import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_generate_helper_build_accessible_nav(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "helpers")
    file_path = os.path.join(folder_path, "helperBuildAccessibleNav.js")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""
import { ROLE_MENU_ACCESS } from "./helperRoleMenuAccess.js";

// siempre visible
const DEFAULT_ITEMS = new Set(['dashboard']);

const getRoleNames = (rolesArr) =>
  Array.isArray(rolesArr) ? rolesArr.map(r => r && r.name).filter(Boolean) : [];

export function buildAccessibleNav(nav, rolesArr) {
  const roleNames = getRoleNames(rolesArr);

  // Si algún rol tiene acceso total → todo
  if (roleNames.some(r => ROLE_MENU_ACCESS[r]?.all)) {
    return nav;
  }

  const allowedItems = new Set(DEFAULT_ITEMS); // empieza con dashboard
  const allowedChildren = {};

  // Unir permisos de todos los roles del usuario
  roleNames.forEach(r => {
    const conf = ROLE_MENU_ACCESS[r];
    if (!conf) return;
    (conf.items || []).forEach(id => allowedItems.add(id));
    if (conf.children) {
      Object.entries(conf.children).forEach(([parentId, hrefs]) => {
        if (!allowedChildren[parentId]) allowedChildren[parentId] = new Set();
        hrefs.forEach(h => allowedChildren[parentId].add(h));
      });
    }
  });

  return nav
    .map(item => {
      if (!allowedItems.has(item.id)) return null;

      if (item.children) {
        const set = allowedChildren[item.id];
        // si no hay permisos para hijos, oculta el submenú entero
        if (!set) return null;
        const children = item.children.filter(ch => set.has(ch.href));
        if (children.length === 0) return null;
        return { ...item, children };
      }

      return item;
    })
    .filter(Boolean);
}
""".lstrip()


    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)