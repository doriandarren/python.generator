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

