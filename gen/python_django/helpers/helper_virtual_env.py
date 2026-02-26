import os
import platform

def get_venv_python(full_path):
    candidates = []

    if platform.system() == "Windows":
        candidates = [
            os.path.join(full_path, ".venv", "Scripts", "python.exe"),
            ##os.path.join(full_path, "backend", ".venv", "Scripts", "python.exe"),
        ]
    else:
        candidates = [
            os.path.join(full_path, ".venv", "bin", "python"),
            os.path.join(full_path, ".venv", "bin", "python3"),
            # os.path.join(full_path, "backend", ".venv", "bin", "python"),
            # os.path.join(full_path, "backend", ".venv", "bin", "python3"),
        ]

    for c in candidates:
        if os.path.isfile(c):
            return c

    raise FileNotFoundError(
        f"No se encontró python del venv dentro de:\n{full_path}\n"
        "Asegúrate de tener una carpeta .venv creada."
    )






# import os
# import platform


# def get_venv_python(full_path):
#     """
#     Retorna la ruta del python del venv
#     """
    
#     # Windows
#     if platform.system() == "Windows":
#         return os.path.join(full_path, ".venv", "Scripts", "python.exe")

#     # Mac/Linux
#     return os.path.join(full_path, ".venv", "bin", "python")