import os
import json
from datetime import datetime

def create_postman_structure(base_ruta):
    """
    Crea la estructura de carpetas 'base_ruta/public/Scripts' en la ruta especificada.
    """
    # Crear la ruta completa base_ruta/public/Scripts
    postman_folder_path = os.path.join(base_ruta, 'public', 'Scripts')

    if not os.path.exists(postman_folder_path):
        os.makedirs(postman_folder_path)
        print(f"Estructura de carpetas '{postman_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{postman_folder_path}' ya existe.")

    return postman_folder_path


def generate_postman_file(base_ruta, singular_name, plural_name, singular_name_kebab, columns):
    """
    Genera un archivo de colección Postman JSON basado en los nombres proporcionados y crea la estructura public/Scripts dentro de base_ruta.
    """
    # Crear la estructura de carpetas llamando a create_postman_structure
    postman_folder_path = create_postman_structure(base_ruta)

    # Nombre del archivo JSON
    file_name = f'{singular_name}Collection.json'
    postman_file_path = os.path.join(postman_folder_path, file_name)

    # Obtener los nombres de las columnas dinámicamente
    column_names = [column["name"] for column in columns]

    # Crear la estructura de la colección de Postman
    postman_content = {
        "info": {
            "_postman_id": "1e8ef847-456f-4806-9ab0-c4b861fe675d",  # Puedes generar un UUID único si es necesario
            "name": singular_name,
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
            "_exporter_id": "5599797"
        },
        "item": [
            {
                "name": plural_name,
                "item": [
                    {
                        "name": "List",
                        "protocolProfileBehavior": {
                            "disableBodyPruning": True
                        },
                        "request": {
                            "method": "GET",
                            "header": [
                                {"key": "Accept", "value": "application/json", "type": "text"},
                                {"key": "Authorization", "value": "Bearer {{token_api}}", "type": "text"}
                            ],
                            "url": {
                                "raw": f"{{{{base_url}}}}/{singular_name_kebab}/list",
                                "host": [f"{{{{base_url}}}}/{singular_name_kebab}"],
                                "path": ["list"]
                            }
                        },
                        "response": []
                    },
                    {
                        "name": "Show",
                        "protocolProfileBehavior": {
                            "disableBodyPruning": True
                        },
                        "request": {
                            "method": "GET",
                            "header": [
                                {"key": "Accept", "value": "application/json", "type": "text"},
                                {"key": "Authorization", "value": "Bearer {{token_api}}", "type": "text"}
                            ],
                            "url": {
                                "raw": f"{{{{base_url}}}}/{singular_name_kebab}/show/1",
                                "host": [f"{{{{base_url}}}}/{singular_name_kebab}"],
                                "path": ["show", "1"]
                            }
                        },
                        "response": []
                    },
                    {
                        "name": "Store",
                        "request": {
                            "method": "POST",
                            "header": [
                                {"key": "Accept", "value": "application/json", "type": "text"},
                                {"key": "Authorization", "value": "Bearer {{token_api}}", "type": "text"}
                            ],
                            "body": {
                                "mode": "formdata",
                                "formdata": [
                                    {"key": column, "value": f"New {column}", "type": "text"}
                                    for column in column_names
                                ]
                            },
                            "url": {
                                "raw": f"{{{{base_url}}}}/{singular_name_kebab}/store",
                                "host": [f"{{{{base_url}}}}/{singular_name_kebab}"],
                                "path": ["store"]
                            }
                        },
                        "response": []
                    },
                    {
                        "name": "Update",
                        "request": {
                            "method": "PUT",
                            "header": [
                                {"key": "Accept", "value": "application/json", "type": "text"},
                                {"key": "Authorization", "value": "Bearer {{token_api}}", "type": "text"}
                            ],
                            "body": {
                                "mode": "urlencoded",
                                "urlencoded": [
                                    {"key": column, "value": f"Update {column}", "type": "text"}
                                    for column in column_names
                                ]
                            },
                            "url": {
                                "raw": f"{{{{base_url}}}}/{singular_name_kebab}/update/1",
                                "host": [f"{{{{base_url}}}}/{singular_name_kebab}"],
                                "path": ["update", "1"]
                            }
                        },
                        "response": []
                    },
                    {
                        "name": "Delete",
                        "request": {
                            "method": "DELETE",
                            "header": [
                                {"key": "Accept", "value": "application/json", "type": "text"},
                                {"key": "Authorization", "value": "Bearer {{token_api}}", "type": "text"}
                            ],
                            "url": {
                                "raw": f"{{{{base_url}}}}/{singular_name_kebab}/delete/1",
                                "host": [f"{{{{base_url}}}}/{singular_name_kebab}"],
                                "path": ["delete", "1"]
                            }
                        },
                        "response": []
                    }
                ]
            }
        ]
    }

    # Escribir el archivo JSON de Postman
    try:
        with open(postman_file_path, 'w') as postman_file:
            json.dump(postman_content, postman_file, indent=4)
            print(f"Archivo de colección Postman '{file_name}' creado en: {postman_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo de colección Postman '{file_name}': {e}")
