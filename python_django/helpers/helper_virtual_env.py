import os
import platform


def get_venv_python(full_path):
    """
    Retorna la ruta del python del venv
    """
    
    # Windows
    if platform.system() == "Windows":
        return os.path.join(full_path, ".venv", "Scripts", "python.exe")

    # Mac/Linux
    return os.path.join(full_path, ".venv", "bin", "python")