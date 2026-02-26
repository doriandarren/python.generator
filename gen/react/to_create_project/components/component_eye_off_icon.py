import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_eye_off_icon(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Icons")
    file_path = os.path.join(folder_path, "ThemedEyeOffIcon.jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""import classNames from "classnames";
import { getVariantTextClass } from "../../helpers/helperVariantClass";

export const ThemedEyeOffIcon = ({ variant = "neutral", className = "w-5 h-5" }) => {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      className={classNames(className, getVariantTextClass(variant))}
      viewBox="0 0 20 20"
      fill="currentColor"
    >
      <path d="M2.854 2.146a.5.5 0 1 0-.708.708l3.5 3.498a8.1 8.1 0 0 0-3.366 5.046a.5.5 0 1 0 .98.204a7.1 7.1 0 0 1 3.107-4.528L7.953 8.66a3.5 3.5 0 1 0 4.886 4.886l4.307 4.308a.5.5 0 0 0 .708-.708zm9.265 10.68A2.5 2.5 0 1 1 8.673 9.38zm-1.995-4.824l3.374 3.374a3.5 3.5 0 0 0-3.374-3.374M10 6c-.57 0-1.129.074-1.666.213l-.803-.803A7.7 7.7 0 0 1 10 5c3.693 0 6.942 2.673 7.72 6.398a.5.5 0 0 1-.98.204C16.058 8.327 13.207 6 10 6"/>
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