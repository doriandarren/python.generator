import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_preloader_button_css(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Preloader")
    file_path = os.path.join(folder_path, "PreloaderButton.css")

    os.makedirs(folder_path, exist_ok=True)

    content = r""".preloader {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 9999;
}

.loader {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)