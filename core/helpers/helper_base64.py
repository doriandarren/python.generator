import base64

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
    Espera formato: { "images": ["<base64>", ...], ... }
    """
    images = response_json.get("images") or []
    if not images:
        return b""
    return b64_to_bytes(images[0])
