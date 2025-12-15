import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_preloader(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Preloader")
    file_path = os.path.join(folder_path, "Preloader.jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""import { PreloaderSVG } from "./PreloaderSVG";

export const Preloader = () => {
  return (
    <div className="flex justify-center">
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