import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_invoice_icon(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Icons")
    file_path = os.path.join(folder_path, "ThemedInvoiceIcon.jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""import classNames from "classnames";
import { getVariantTextClass } from "../../helpers/helperVariantClass";

export const ThemedInvoiceIcon = ({ variant = "neutral", className = "w-6 h-6" }) => {
  return (
    <svg
      className={classNames(className, getVariantTextClass(variant))}
      fill="currentColor"
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path d="M6 2a2 2 0 0 0-2 2v16l4-2 4 2 4-2 4 2V4a2 2 0 0 0-2-2H6zm2 4h8v2H8V6zm0 4h8v2H8v-2zm0 4h5v2H8v-2z" />
    </svg>
  );
};
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)