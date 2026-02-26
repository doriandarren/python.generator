import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_alert(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Alerts")
    file_path = os.path.join(folder_path, "ThemedAlert.jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""import classNames from "classnames";
import { getVariantBgClass, getVariantTextClass } from "../../helpers/helperVariantClass";

export const ThemedAlert = ({ text, variant = "info", icon = null, className = "" }) => {
  return (
    <div
      role="alert"
      className={classNames(
        "flex items-center gap-3 rounded-lg px-4 py-3 text-sm",
        getVariantBgClass(variant),
        getVariantTextClass(variant),
        className
      )}
    >
      {icon && <span className="shrink-0 text-white">{icon}</span>}
      <span className="text-white">{text}</span>
    </div>
  );
};
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)