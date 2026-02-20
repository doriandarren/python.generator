import os
from gen.helpers.helper_print import print_message, GREEN, CYAN


def generate_file_helpers(full_path):
    create_file_init(full_path)
    create_file_helpers(full_path)


def create_file_helpers(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "core", "helpers")
    file_path = os.path.join(folder_path, "helper_base64.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''import base64

def b64_to_bytes(b64_string: str) -> bytes:
    """
    Convierte un string base64 (con o sin prefijo data:image/..;base64,) a bytes.
    """
    if not b64_string:
        return b""

    # Si viene con prefijo "data:image/png;base64,...."
    if "," in b64_string:
        _, b64_string = b64_string.split(",", 1)

    return base64.b64decode(b64_string)




def sd_txt2img_first_image_bytes(response_json: dict) -> bytes:
    """
    Extrae la primera imagen del JSON de Stable Diffusion (txt2img) y la devuelve en bytes.
    Espera formato: {{ "images": ["<base64>", ...], ... }}
    """
    images = response_json.get("images") or []
    if not images:
        return b""
    return b64_to_bytes(images[0])
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
        


def create_file_init(full_path):
    """
    Genera el archivo init
    """
    folder_path = os.path.join(full_path, "core", "helpers")
    file_path = os.path.join(folder_path, "__init__.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f''''''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)