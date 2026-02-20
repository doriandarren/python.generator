import os
from gen.helpers.helper_print import print_message, GREEN, CYAN


def generate_message_channel(full_path):
    create_file_init(full_path)
    create_message_channel(full_path)




def create_message_channel(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "core", "messages")
    file_path = os.path.join(folder_path, "message_channel.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''import os
import requests
from django.conf import settings

class MessageChannel:
    
    @staticmethod
    def send(text: str, title: str = "Title", is_error: bool = False) -> None:

        url = settings.MESSAGE_CHANNEL_URL
        if not url:
            return

        title = f"{{title}} {{settings.APP_NAME}} {{settings.APP_ENV}}"

        text = text[:500]

        payload = {{
            "embeds": [{{
                "title": title,
                "description": text,
                "color": 0xFF0000 if is_error else 0x00FF00,
            }}]
        }}

        try:
            requests.post(url, json=payload, timeout=5)
        except requests.RequestException:
            pass
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
    folder_path = os.path.join(full_path, "core", "messages")
    file_path = os.path.join(folder_path, "__init__.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f''''''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

