import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_badges(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Badges")
    file_path = os.path.join(folder_path, "ThemedBadge.jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""import classNames from "classnames";
import { getVariantBgClass } from "../../helpers/helperVariantClass";

export const ThemedBadge = ({ text, variant = "gray", className = "" }) => {
  return (
    <span
      className={classNames(
        "inline-flex items-center rounded-full px-2 py-1 text-xs font-medium",
        getVariantBgClass(variant),
        "text-white",
        className
      )}
    >
      {text}
    </span>
  );
};
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
