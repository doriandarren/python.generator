# Generator Project

## Flujo del proyecto

```sh
## Para proyectos (to_create_project)
pymain -> pystart -> pystartproject -> pygenerate

## Para modulos (to_create_module_crud)
pymain -> pystart -> pystartmodule -> pystandard -> pygenerate
```

# Pasos:

```sh
1. crear carpeta proyecto "xxx" y archivo "_ _ init _ _.py" y el archivo: "main_xxx"
2. crear carpetas con sus respectivos archivos "_ _ init _ _.py":

   - "to_create_module_crud"
   - "to_create_project"

3. crear dentro de la carpeta "to_create_project" el archivo: start_project_xxx.py
4. crear dentro de la carpeta "to_create_module_crud" el archivo: start_module_xxx.py

```


# Format Example -> columns

```sh
[{'name': 'user_id', 'type': 'fk', 'is_fk': True, 'related_table': 'users', 'related_model': 'User'}, {'name': 'name', 'type': 'string', 'is_fk': False}, {'name': 'age', 'type': 'integer', 'is_fk': False}, {'name': 'description', 'type': 'string', 'is_fk': False}]
```



# TODOS:

PYTHON:

- las cors: 'corsheaders.middleware.CorsMiddleware', # required for cors,
  va encima de: 'django.middleware.common.CommonMiddleware',

- En PHP: cuando se crea un proyecto, se tiene que cambiar en el ".env" y en el ".env.example" lo siguientes: "LOG_CHANNEL=daily"
- en el archivo para API de postman hay que agregar en el Dev: el "execute"
- En PHP: revisar el plural cambiar a inflect por que agrega una "s" al final de la palabra de las migraciones cuando es fk
- Crear React_TS

Tabla ai_text_generations

id
user_id
model_name

system_message
user_message

response_message

response_done
response_done_reason
response_total_duration
response_load_duration
response_prompt_eval_count
response_prompt_eval_duration
response_eval_count
response_eval_duration
response_created_at

created_at
updated_at







from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action

from core.http.api_request import ApiRequest

api_ollama = ApiRequest("http://192.168.1.100:11434/")

class DevApiViewSet(ModelViewSet):
permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'], url_path='test')
    def invoke(self, request):

        try:
            payload = {
                "model": "llama3:latest",
                "messages": [
                    {
                        "role": "system",
                        "content": "Eres un asistente experto en python y siempre devuelves código limpio, bien organizado y sin explicaciones innecesarias."
                    },
                    {
                        "role": "user",
                        "content": "responde solamnete hola mundo"
                    }
                ],
                "stream": False
            }

            response = api_ollama.post(
                path="api/chat",
                payload=payload
            )


            print(response["message"]["content"])


            return Response({
                'message': response,
            }, status=status.HTTP_200_OK)


        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


