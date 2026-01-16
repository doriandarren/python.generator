import os
from helpers.helper_print import print_message, GREEN, CYAN


def generate_http(full_path):
    create_file_init(full_path)
    create_http(full_path)



def create_http(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "core", "http")
    file_path = os.path.join(folder_path, "api_request.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''import requests
from typing import Optional


class ApiRequest:
    
    def __init__(
        self,
        base_url: str,
        token: Optional[str] = None,
        timeout: int = 300,
    ):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout

    def _headers(self, extra_headers: dict | None = None) -> dict:
        headers = {{
            "Accept": "application/json",
            "Content-Type": "application/json",
        }}

        if self.token:
            headers["Authorization"] = f"Bearer {{self.token}}"

        if extra_headers:
            headers.update(extra_headers)

        return headers

    def _url(self, path: str) -> str:
        return f"{{self.base_url}}/{{path.lstrip('/')}}"

    def get(self, path: str, params: dict | None = None) -> dict:
        r = requests.get(
            self._url(path),
            params=params,
            headers=self._headers(),
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

    def post(self, path: str, payload: dict) -> dict:
        r = requests.post(
            self._url(path),
            json=payload,
            headers=self._headers(),
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

    def put(self, path: str, payload: dict) -> dict:
        r = requests.put(
            self._url(path),
            json=payload,
            headers=self._headers(),
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

    def delete(self, path: str) -> dict:
        r = requests.delete(
            self._url(path),
            headers=self._headers(),
            timeout=self.timeout,
        )
        r.raise_for_status()
        return r.json()

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
    folder_path = os.path.join(full_path, "core", "http")
    file_path = os.path.join(folder_path, "__init__.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f''''''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)