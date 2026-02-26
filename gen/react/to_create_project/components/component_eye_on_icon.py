import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_eye_on_icon(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Icons")
    file_path = os.path.join(folder_path, "ThemedEyeOnIcon.jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""import classNames from "classnames";
import { getVariantTextClass } from "../../helpers/helperVariantClass";

export const ThemedEyeOnIcon = ({ variant = "neutral", className = "w-5 h-5" }) => {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      className={classNames(className, getVariantTextClass(variant))}
      viewBox="0 0 16 16"
      fill="currentColor"
    >
      <path d="M2.984 8.625v.003a.5.5 0 0 1-.612.355c-.431-.114-.355-.611-.355-.611l.018-.062s.026-.084.047-.145a6.7 6.7 0 0 1 1.117-1.982C4.096 5.089 5.605 4 8 4s3.904 1.089 4.802 2.183a6.7 6.7 0 0 1 1.117 1.982a4 4 0 0 1 .06.187l.003.013v.004l.001.002a.5.5 0 0 1-.966.258l-.001-.004l-.008-.025l-.035-.109a5.7 5.7 0 0 0-.945-1.674C11.286 5.912 10.045 5 8 5s-3.285.912-4.028 1.817a5.7 5.7 0 0 0-.945 1.674l-.035.109zM5.5 9.5a2.5 2.5 0 1 1 5 0a2.5 2.5 0 0 1-5 0"/>
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