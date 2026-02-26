import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_preloader_main(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Preloader")
    file_path = os.path.join(folder_path, "PreloaderMain.jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""import { PreloaderSVG } from "./PreloaderSVG";
import "./PreloaderMain.css";

export const PreloaderMain = () => {
  return (
    <div className="preloader flex justify-center">
      <PreloaderSVG />
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