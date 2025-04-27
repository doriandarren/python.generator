import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_postman_file(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path)

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "Node - Api.postman_collection.json")

    # Contenido por defecto
    content = r"""{
	"info": {
		"_postman_id": "c39ca656-ba06-4e7f-9563-8974ddcffc08",
		"name": "Node - API",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "5599797",
		"_collection_link": "https://warped-satellite-11290.postman.co/workspace/Splytin~bac4189f-178f-4428-8a25-dabd0d5190ca/collection/5599797-c39ca656-ba06-4e7f-9563-8974ddcffc08?action=share&source=collection_link&creator=5599797"
	},
	"item": [
		{
			"name": "DEV",
			"item": [
				{
					"name": "test",
					"request": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{base_url}}",
							"host": [
								"{{base_url}}"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "users",
			"item": [
				{
					"name": "user list / paginados",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "passwrod",
									"value": "loteria",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{url}}users",
							"host": [
								"{{url}}users"
							],
							"query": [
								{
									"key": "from",
									"value": "10",
									"disabled": true
								},
								{
									"key": "limit",
									"value": "10",
									"disabled": true
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "user show",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "passwrod",
									"value": "loteria",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{url}}users?q=hola&nombre=fercho&apikey=87878787",
							"host": [
								"{{url}}users"
							],
							"query": [
								{
									"key": "q",
									"value": "hola"
								},
								{
									"key": "nombre",
									"value": "fercho"
								},
								{
									"key": "apikey",
									"value": "87878787"
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "user store",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"name\": \"Chop 17\",\n    \"email\": \"chop17@google.com\",\n    \"password\": \"12343455\",\n    \"role\": \"USER_ROLE\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{url}}users",
							"host": [
								"{{url}}users"
							]
						}
					},
					"response": []
				},
				{
					"name": "user update",
					"request": {
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"name\": \"Fercho1111\",\n    \"google\": true,\n    \"email\": \"fercho_lol@google.com\",\n    \"password\": \"123477787\",\n    \"role\": \"ADMIN_ROLE\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{url}}users/67fbc2b7d6044e804a88ba70111",
							"host": [
								"{{url}}users"
							],
							"path": [
								"67fbc2b7d6044e804a88ba70111"
							]
						}
					},
					"response": []
				},
				{
					"name": "user delete",
					"request": {
						"method": "DELETE",
						"header": [],
						"url": {
							"raw": "{{url}}users/67fbc2bcd6044e804a88ba75",
							"host": [
								"{{url}}users"
							],
							"path": [
								"67fbc2bcd6044e804a88ba75"
							]
						}
					},
					"response": []
				}
			]
		}
	],
	"event": [
		{
			"listen": "prerequest",
			"script": {
				"type": "text/javascript",
				"packages": {},
				"exec": [
					""
				]
			}
		},
		{
			"listen": "test",
			"script": {
				"type": "text/javascript",
				"packages": {},
				"exec": [
					""
				]
			}
		}
	],
	"variable": [
		{
			"key": "base_url",
			"value": "http://localhost:8080",
			"type": "string"
		}
	]
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
