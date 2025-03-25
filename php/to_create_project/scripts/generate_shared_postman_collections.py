import os
from helpers.helper_print import print_message, GREEN, CYAN




def generate_shared_postman_collections(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "public", "SCRIPTS")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "API.postman.collection.json")

    # Contenido por defecto
    content = r"""{
	"info": {
		"_postman_id": "c45bcd65-d68b-4fbe-a0b6-b87a5632cbff",
		"name": "API",
		"description": "Api Rest Full para GlobalFleet\n\nApi URL:\n\n[https://apistaging.globaltank.eu/api/](https://apistaging.globaltank.eu/api/)\n\nEstructura principales de ENDPOINT para la gestión:\n\n- base_url/list\n- base_url/list-paginate\n- base_url/list/paginate?filter=cosoltrans\n- base_url/show/id\n- base_url/store\n- base_url/update\n- base_url/destroy",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "5599797",
		"_collection_link": "https://warped-satellite-11290.postman.co/workspace/GlobalFleet~ae865b4b-fd0c-416a-bcd9-0c9108578f23/collection/5599797-c45bcd65-d68b-4fbe-a0b6-b87a5632cbff?action=share&source=collection_link&creator=5599797"
	},
	"item": [
		{
			"name": "Authentication",
			"item": [
				{
					"name": "Restore Password",
					"item": [
						{
							"name": "forgot Password",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "email",
											"value": "dorian.gonzalez@globaltank.eu",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "{{base_url}}auth/password/email",
									"host": [
										"{{base_url}}auth"
									],
									"path": [
										"password",
										"email"
									]
								}
							},
							"response": []
						},
						{
							"name": "Restore Password",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "token",
											"value": "o3T8UOouVBmNYe48QEGgE7AGYycgxHlKA5ySHitAnaGa50bHtVdu57Pp2Kv6",
											"type": "text"
										},
										{
											"key": "password",
											"value": "pepepe",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "{{base_url}}auth/password/restore",
									"host": [
										"{{base_url}}auth"
									],
									"path": [
										"password",
										"restore"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "login",
					"event": [
						{
							"listen": "test",
							"script": {
								"exec": [
									"let response = JSON.parse(pm.response.text());",
									"pm.collectionVariables.set(\"token_api\", response.token);"
								],
								"type": "text/javascript",
								"packages": {}
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text",
								"uuid": "b15de912-b133-4bec-b152-12fb3986d9eb"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "email",
									"value": "webmaster@globalfleet.es",
									"description": "Email usuario demo",
									"type": "text"
								},
								{
									"key": "password",
									"value": "Tailandia2024",
									"description": "Password de usuario demo",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}auth/login",
							"host": [
								"{{base_url}}auth"
							],
							"path": [
								"login"
							]
						},
						"description": "This HTTP POST request is used to authenticate and login a user. The request is sent to the endpoint `{{base_url}}auth/login`.\n\nThe request does not require any specific parameters to be passed in the body or as query parameters.\n\nThe response received after a successful login has a status code of 201. The response body contains the following properties:\n\n- `message`: A string that may contain additional information or a success message.\n- `token`: A string representing the authentication token for the logged-in user.\n- `token_type`: A string representing the type of the authentication token.\n- `success`: A boolean value indicating whether the login was successful or not.\n- `status_code`: An integer representing the status code of the response.\n    \n\nPlease note that the actual values of the `message`, `token`, and `token_type` properties may vary based on the specific implementation of the authentication system.\n\nTo use this endpoint, send an HTTP POST request to `{{base_url}}auth/login` without any request parameters. The response will contain the authentication token if the login is successful.\n\nExample:\n\n```\nPOST {{base_url}}auth/login\n\n ```\n\nResponse:\n\n```\nStatus: 201\n{\n  \"message\": \"\",\n  \"token\": \"\",\n  \"token_type\": \"\",\n  \"success\": true,\n  \"status_code\": 0\n}\n\n ```"
					},
					"response": []
				},
				{
					"name": "show",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text",
								"uuid": "8ee147c7-1c9c-4f5a-b54c-019db3f93c1c"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"type": "text",
								"uuid": "28341df2-dcf3-4211-bcfa-9def40c0c15c"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}auth/user",
							"host": [
								"{{base_url}}auth"
							],
							"path": [
								"user"
							]
						}
					},
					"response": []
				},
				{
					"name": "logout",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"type": "text",
								"uuid": "d326a93e-c13f-4d10-b0ac-e7b618d44a2b"
							},
							{
								"key": "Authorization",
								"value": "Bearer  {{token_api}}",
								"type": "text",
								"uuid": "ceb2cd55-8f07-4f33-b225-aa776f852e8e"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}auth/logout",
							"host": [
								"{{base_url}}auth"
							],
							"path": [
								"logout"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Dev",
			"item": [
				{
					"name": "Test",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{base_url}}dev/test",
							"host": [
								"{{base_url}}dev"
							],
							"path": [
								"test"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Abilities",
			"item": [
				{
					"name": "List",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "11f6afea-eee9-4fbd-bff6-5f12bf0c49bd"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "c8614f09-c19d-4009-b8fa-2327999619ea"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}abilities/list",
							"host": [
								"{{base_url}}abilities"
							],
							"path": [
								"list"
							]
						}
					},
					"response": []
				},
				{
					"name": "Show",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "320d88fb-c04d-4338-8f09-1e93f8f9b32d"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "ac170de5-2512-49cb-929e-81c8a823e859"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}abilities/show/1",
							"host": [
								"{{base_url}}abilities"
							],
							"path": [
								"show",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Store",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "f00d6e4a-e620-4dc6-bf64-f6746b0a4cbb"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "df6bcd51-d58c-4c08-b21c-aed977f24acc"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "name",
									"value": "New name",
									"type": "text"
								},
								{
									"key": "label",
									"value": "New label",
									"type": "text"
								},
								{
									"key": "ability_group_id",
									"value": "1",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}abilities/store",
							"host": [
								"{{base_url}}abilities"
							],
							"path": [
								"store"
							]
						}
					},
					"response": []
				},
				{
					"name": "Update",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "81bbeb58-37cd-438e-b434-3d8ed3e5969c"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "51408beb-6274-4cd3-ac4f-75abdcfd46c6"
							}
						],
						"body": {
							"mode": "urlencoded",
							"urlencoded": [
								{
									"key": "name",
									"value": "Update name",
									"type": "text"
								},
								{
									"key": "label",
									"value": "Update label",
									"type": "text"
								},
								{
									"key": "ability_group_id",
									"value": "1",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}abilities/update/1",
							"host": [
								"{{base_url}}abilities"
							],
							"path": [
								"update",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "dabbaf0e-fea5-4264-a74d-ca89545b1b8d"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "67c34718-e632-4dbb-bf50-162df3107f0d"
							}
						],
						"url": {
							"raw": "{{base_url}}abilities/delete/1",
							"host": [
								"{{base_url}}abilities"
							],
							"path": [
								"delete",
								"1"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "AbilityGroups",
			"item": [
				{
					"name": "List",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "a0885dea-f00d-4db6-8640-dc7b1441e700"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "fea63a97-b9be-494d-b94f-5f3a588a4bc6"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}ability-groups/list",
							"host": [
								"{{base_url}}ability-groups"
							],
							"path": [
								"list"
							]
						}
					},
					"response": []
				},
				{
					"name": "Show",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "11c01d7e-24c9-4a30-9959-077dd9a624fb"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "fa45d2c7-471f-4b6e-8cfc-060d6ae101c2"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}ability-groups/show/1",
							"host": [
								"{{base_url}}ability-groups"
							],
							"path": [
								"show",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Store",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "5ef744f2-6f8d-4446-bb89-72f4336d45ef"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "26f07958-8e0a-4489-a014-db5bccb32c78"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "name",
									"value": "New name",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}ability-groups/store",
							"host": [
								"{{base_url}}ability-groups"
							],
							"path": [
								"store"
							]
						}
					},
					"response": []
				},
				{
					"name": "Update",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "1a2663b1-ad7b-41b4-913c-99639cbedb2e"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "6d5a9c9f-a52c-4637-a862-1738d7a88ff4"
							}
						],
						"body": {
							"mode": "urlencoded",
							"urlencoded": [
								{
									"key": "name",
									"value": "Update name",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}ability-groups/update/1",
							"host": [
								"{{base_url}}ability-groups"
							],
							"path": [
								"update",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "99d3b66c-954d-412a-a63b-d6cdc2fe7684"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "87c7b280-8a88-43aa-a030-e1e1e20588cc"
							}
						],
						"url": {
							"raw": "{{base_url}}ability-groups/delete/1",
							"host": [
								"{{base_url}}ability-groups"
							],
							"path": [
								"delete",
								"1"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "AbilityUsers",
			"item": [
				{
					"name": "List",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "1e011b46-90f7-4586-85b2-ad54c4390682"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "c79c8e54-5ce1-466b-aea3-6f437493c548"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}ability-users/list",
							"host": [
								"{{base_url}}ability-users"
							],
							"path": [
								"list"
							]
						}
					},
					"response": []
				},
				{
					"name": "Show",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "b3f24eb5-3dd5-43b1-bedc-de3f1d2453c1"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "c4473217-c1cf-4409-a82a-3c758b46b907"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}ability-users/show/1",
							"host": [
								"{{base_url}}ability-users"
							],
							"path": [
								"show",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Store",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "6a05c939-dabe-469b-b1ed-ff1ac8dc4c77"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "6ca1b424-bd84-4285-988e-0197dae69e71"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "user_id",
									"value": "1",
									"type": "text"
								},
								{
									"key": "ability_id",
									"value": "1",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}ability-users/store",
							"host": [
								"{{base_url}}ability-users"
							],
							"path": [
								"store"
							]
						}
					},
					"response": []
				},
				{
					"name": "Update",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "2066b0a5-11e9-469e-bb51-1d39ccece843"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "e7a96858-9791-4280-b3de-8b968d134033"
							}
						],
						"body": {
							"mode": "urlencoded",
							"urlencoded": [
								{
									"key": "user_id",
									"value": "1",
									"type": "text"
								},
								{
									"key": "ability_id",
									"value": "1",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}ability-users/update/1",
							"host": [
								"{{base_url}}ability-users"
							],
							"path": [
								"update",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "6caad92f-7ca7-4d9e-a429-da872d7c5c10"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "5491d269-c1b7-4b16-9683-76673c14dff0"
							}
						],
						"url": {
							"raw": "{{base_url}}ability-users/delete/1",
							"host": [
								"{{base_url}}ability-users"
							],
							"path": [
								"delete",
								"1"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "RoleUsers",
			"item": [
				{
					"name": "List",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "0f419ea6-3df9-45f6-82f1-542c32ba7595"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "90c51d34-a9a6-4bd0-b758-0f476b9001b1"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}role-users/list",
							"host": [
								"{{base_url}}role-users"
							],
							"path": [
								"list"
							]
						}
					},
					"response": []
				},
				{
					"name": "Show",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "a6cebf54-e155-4f21-9504-dd9ee411280c"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "23885482-c7b1-4850-b55b-9f9dc483316e"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}role-users/show/1",
							"host": [
								"{{base_url}}role-users"
							],
							"path": [
								"show",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Store",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "a290879f-81f7-4319-892b-9f1000f30767"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "ff96cf5a-6953-4cab-979d-9e856ffaaf53"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "role_id",
									"value": "1",
									"type": "text"
								},
								{
									"key": "user_id",
									"value": "1",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}role-users/store",
							"host": [
								"{{base_url}}role-users"
							],
							"path": [
								"store"
							]
						}
					},
					"response": []
				},
				{
					"name": "Update",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "cabe1bce-50ce-40a4-a36c-374a51d53eef"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "82ee7fac-c9ed-459b-a247-198db348e411"
							}
						],
						"body": {
							"mode": "urlencoded",
							"urlencoded": [
								{
									"key": "role_id",
									"value": "1",
									"type": "text"
								},
								{
									"key": "user_id",
									"value": "1",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}role-users/update/1",
							"host": [
								"{{base_url}}role-users"
							],
							"path": [
								"update",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "aef43afd-1b27-4021-9fe7-9b6b560b9bba"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "291278aa-204a-417c-a28a-98df00b70678"
							}
						],
						"url": {
							"raw": "{{base_url}}role-users/delete/1",
							"host": [
								"{{base_url}}role-users"
							],
							"path": [
								"delete",
								"1"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Roles",
			"item": [
				{
					"name": "List",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "f5f5dd9a-3191-4145-8c96-eff31368fef8"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "e3289006-ab5d-451d-af3a-0f2337d44c00"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}roles/list",
							"host": [
								"{{base_url}}roles"
							],
							"path": [
								"list"
							]
						}
					},
					"response": []
				},
				{
					"name": "Show",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "6b8b1fb9-61af-45ca-99a0-2e148d2527be"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "47c11368-b30d-4c87-8ff3-11c6879f95d7"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}roles/show/1",
							"host": [
								"{{base_url}}roles"
							],
							"path": [
								"show",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Store",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "c6ae51d7-3679-4d73-b133-1bf9343e20f9"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "e3cb0ad1-8791-4815-8542-0f5fa1d1e69a"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "name",
									"value": "New name",
									"type": "text"
								},
								{
									"key": "description",
									"value": "New description",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}roles/store",
							"host": [
								"{{base_url}}roles"
							],
							"path": [
								"store"
							]
						}
					},
					"response": []
				},
				{
					"name": "Update",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "fb06cfba-1cff-4870-bf24-27519ef1b8b2"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "f562b402-277a-492a-916c-ac156d308823"
							}
						],
						"body": {
							"mode": "urlencoded",
							"urlencoded": [
								{
									"key": "name",
									"value": "Update name",
									"type": "text"
								},
								{
									"key": "description",
									"value": "Update description",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}roles/update/1",
							"host": [
								"{{base_url}}roles"
							],
							"path": [
								"update",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "5a9c8bc9-c0c8-4b82-8237-ab5528d8948c"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "ce6ce348-9ac7-4348-b83e-d1d96f14fbd7"
							}
						],
						"url": {
							"raw": "{{base_url}}roles/delete/1",
							"host": [
								"{{base_url}}roles"
							],
							"path": [
								"delete",
								"1"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "UserStatuses",
			"item": [
				{
					"name": "List",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "f896b670-2bdc-44aa-b813-e08a7b912a00"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "e0064dfa-fc91-4aa5-8903-3da60753f719"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}user-statuses/list",
							"host": [
								"{{base_url}}user-statuses"
							],
							"path": [
								"list"
							]
						}
					},
					"response": []
				},
				{
					"name": "Show",
					"protocolProfileBehavior": {
						"disableBodyPruning": true
					},
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "bcc1cea1-7378-4f97-ba6d-9e1c52f6d2c8"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "94038b5d-1cc8-4c52-bc49-5535f092d0f8"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": []
						},
						"url": {
							"raw": "{{base_url}}user-statuses/show/1",
							"host": [
								"{{base_url}}user-statuses"
							],
							"path": [
								"show",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Store",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "f3b17046-88d8-4ba4-878c-24ca7b86eb92"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "3f8d7f57-275b-4ec2-838d-923d0d070171"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "name",
									"value": "New name",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}user-statuses/store",
							"host": [
								"{{base_url}}user-statuses"
							],
							"path": [
								"store"
							]
						}
					},
					"response": []
				},
				{
					"name": "Update",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "965ebd5b-8043-4c13-9b49-a8f4c0b1e935"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "f9e3d04f-8869-45ca-a09e-141a179153f0"
							}
						],
						"body": {
							"mode": "urlencoded",
							"urlencoded": [
								{
									"key": "name",
									"value": "Update name",
									"type": "text"
								}
							]
						},
						"url": {
							"raw": "{{base_url}}user-statuses/update/1",
							"host": [
								"{{base_url}}user-statuses"
							],
							"path": [
								"update",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Accept",
								"value": "application/json",
								"uuid": "7913047d-8600-4ef4-a4b7-5c326a27dbe2"
							},
							{
								"key": "Authorization",
								"value": "Bearer {{token_api}}",
								"uuid": "0dfd6460-eded-4302-9087-0a4bf33a037c"
							}
						],
						"url": {
							"raw": "{{base_url}}user-statuses/delete/1",
							"host": [
								"{{base_url}}user-statuses"
							],
							"path": [
								"delete",
								"1"
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
				"exec": [
					""
				]
			}
		},
		{
			"listen": "test",
			"script": {
				"type": "text/javascript",
				"exec": [
					""
				]
			}
		}
	],
	"variable": [
		{
			"key": "base_url",
			"value": "https://invoices-api.globalfleet.es/api/v1/",
			"type": "string",
			"disabled": true
		},
		{
			"key": "base_url",
			"value": "https://invoices-api-staging.globalfleet.es/api/v1/",
			"type": "string",
			"disabled": true
		},
		{
			"key": "base_url",
			"value": "http://invoices-api.globalfleet.test/api/v1/",
			"type": "string"
		},
		{
			"key": "token_api",
			"value": ""
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
