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

## Tables:

📄 Table: ai_text_generations - AiTextGeneration - AiTextGenerations
Columns: user_id model_name system_message user_message response_message response_done response_done_reason response_total_duration response_load_duration response_prompt_eval_count response_prompt_eval_duration response_eval_count response_eval_duration




from apps.ai_text_generations.models import AiTextGeneration

class AiTextGenerationService:

    def list(self):
        return AiTextGeneration.objects.all()


    def show(self, id):
        return AiTextGeneration.objects.filter(id=id).first()


    def store(self, model: AiTextGeneration):
        model.save()
        return model


    def update(self, id, data: dict):
        model = self.show(id)

        if not model:
            return None

        if "user_id" in data:
            model.user_id = data["user_id"]

        if "model_name" in data:
            model.model_name = data["model_name"]

        if "system_message" in data:
            model.system_message = data["system_message"]

        if "user_message" in data:
            model.user_message = data["user_message"]

        if "response_message" in data:
            model.response_message = data["response_message"]

        if "response_done" in data:
            model.response_done = data["response_done"]

        if "response_done_reason" in data:
            model.response_done_reason = data["response_done_reason"]

        if "response_total_duration" in data:
            model.response_total_duration = data["response_total_duration"]

        if "response_load_duration" in data:
            model.response_load_duration = data["response_load_duration"]

        if "response_prompt_eval_count" in data:
            model.response_prompt_eval_count = data["response_prompt_eval_count"]

        if "response_prompt_eval_duration" in data:
            model.response_prompt_eval_duration = data["response_prompt_eval_duration"]

        if "response_eval_count" in data:
            model.response_eval_count = data["response_eval_count"]

        if "response_eval_duration" in data:
            model.response_eval_duration = data["response_eval_duration"]

        model.save()
        return model



    def destroy(self, id) -> bool:
        model = self.show(id)

        if not model:
            return False

        model.delete()
        return True



    def set_ai_text_generation(
        self,
        user_id,
        model_name,
        system_message,
        user_message,
        response_message,
        response_done,
        response_done_reason,
        response_total_duration,
        response_load_duration,
        response_prompt_eval_count,
        response_prompt_eval_duration,
        response_eval_count,
        response_eval_duration,
    ) -> AiTextGeneration:
        model = AiTextGeneration()
        model.user_id = user_id
        model.model_name = model_name
        model.system_message = system_message
        model.user_message = user_message
        model.response_message = response_message
        model.response_done = response_done
        model.response_done_reason = response_done_reason
        model.response_total_duration = response_total_duration
        model.response_load_duration = response_load_duration
        model.response_prompt_eval_count = response_prompt_eval_count
        model.response_prompt_eval_duration = response_prompt_eval_duration
        model.response_eval_count = response_eval_count
        model.response_eval_duration = response_eval_duration

        return model









DEV:::

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action

from apps.ai_text_generations.services.ai_text_generation_service import AiTextGenerationService
from core.http.api_request import ApiRequest

api_ollama = ApiRequest("http://192.168.1.100:11434/")


class DevApiViewSet(ModelViewSet):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = AiTextGenerationService()
    
    

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



            ai_text_generation = self.service.set_ai_text_generation(
                str(request.user.id) if request.user.is_authenticated else "anonymous",
                payload.get("model", ""),
                "mensaje sistema",
                "mensaje usuario",
                "respuesta",
                "true",
                "stop",
                "123",
                "45",
                "10",
                "20",
                "30",
                "40",
            )
            
            print(type(ai_text_generation))
            
            
            ## print(response["message"]["content"])


            return Response({
                'message': response,
            }, status=status.HTTP_200_OK)


        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


