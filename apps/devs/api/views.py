from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action

from core.http.api_request import ApiRequest


api_ollama = ApiRequest("http://192.168.1.100:11434/")   



class DevApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    # {
    #     "model": "llama3:latest",
    #     "messages": [
    #     {
    #         "role": "system",
    #         "content": "Eres un asistente experto en python y siempre devuelves código limpio, bien organizado y sin explicaciones innecesarias."
    #     },
    #     {
    #         "role": "user",
    #         "content": "me puedes ayudar hacer musica lofi?? necesito que me generes el archivo mid con python, dame un script que yo lo ejecuto en mi pc"
    #     }
    #     ],
    #     "stream": false
    # }
    
    
    
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
                        "content": "me puedes ayudar hacer musica lofi?? necesito que me generes el archivo mid con python, dame un script que yo lo ejecuto en mi pc"
                    }
                ],        
                "stream": False
            }

            response = api_ollama.post(
                path="api/chat",
                payload=payload
            )
            
            
            print(response)
        
            
            return Response({
                'message': response,
            })
            
            
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        
    
