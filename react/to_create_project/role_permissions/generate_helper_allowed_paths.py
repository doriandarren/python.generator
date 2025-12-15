import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_helper_allowed_paths(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "helpers")
    file_path = os.path.join(folder_path, "helperAllowedPaths.js")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""
// helpers/helperAllowedPaths.js
import { ROLE_MENU_ACCESS } from "./helperRoleMenuAccess.js";

// Dashboard siempre permitido
export const DEFAULT_ITEMS = new Set(["dashboard"]);

/**
 * Mapea IDs raíz de tu navigation → rutas base reales del router.
 * Deben existir en tu AppRouter (path=".../*").
 */
export const ROOT_ID_TO_HREF = {
  dashboard: "/admin/dashboard",
  teams: "/admin/teams",
  // Usa la página índice real de Settings como base:
  settings: "/admin/systems",
  // Si prefieres no tener base para settings, elimina la línea de arriba.
};

/**
 * Convierte roles del usuario → conjunto de rutas permitidas.
 * - Admin/manager (all:true): permite todo /admin/*
 * - Para el resto: permite las bases por id y los hijos explícitos.
 */
export function getAllowedPathsByRoles(rolesArr = []) {
  const roleNames = (Array.isArray(rolesArr) ? rolesArr : [])
    .map((r) => (r?.name ?? r))
    .filter(Boolean)
    .map((s) => String(s).toLowerCase().trim());

  // Acceso total
  if (roleNames.some((r) => ROLE_MENU_ACCESS[r]?.all)) {
    return new Set(["/admin"]);
  }

  const allowedRootIds = new Set(DEFAULT_ITEMS); // arranca con dashboard
  const allowedChildren = new Set();

  for (const r of roleNames) {
    const conf = ROLE_MENU_ACCESS[r];
    if (!conf) continue;

    (conf.items || []).forEach((id) => allowedRootIds.add(id));

    if (conf.children) {
      Object.values(conf.children).forEach((hrefs) => {
        hrefs.forEach((h) => allowedChildren.add(h));
      });
    }
  }

  // ids raíz → rutas base reales
  const allowedPaths = new Set(
    [...allowedRootIds]
      .map((id) => ROOT_ID_TO_HREF[id])
      .filter(Boolean)
  );

  // hijos explícitos
  allowedChildren.forEach((h) => allowedPaths.add(h));

  return allowedPaths;
}
""".lstrip()


    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)