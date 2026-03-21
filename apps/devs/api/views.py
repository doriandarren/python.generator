from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action


from apps.ai_text_generations.api.serializers import aiTextGenerationSerializer
from apps.ai_text_generations.services.ai_text_generation_service import AiTextGenerationService
from core.http.api_request import ApiRequest

api_ollama = ApiRequest("http://192.168.1.100:11434/")


class DevApiViewSet(ModelViewSet):
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = AiTextGenerationService()
    
    

    @action(detail=False, methods=['get'], url_path='test-in')
    def invoke_in(self, request):

        try:
            payload = {
                "model": "llama3:latest",
                "messages": [
                    {
                        "role": "system",
                        "content": "Eres un asistente creativo que escribe historias cortas, claras y bien estructuradas."
                    },
                    {
                        "role": "user",
                        ##"content": "Cuéntame una historia corta sobre un programador que descubre algo inesperado mientras trabaja con inteligencia artificial."
                        "content": "Puedes seguir la historia y trata escribir acerca de unos alien que se encuentran en la tierra: Aquí está una continuación:\n\nAños después, la inteligencia artificial emocional había avanzado significativamente. Las conversaciones entre los seres humanos y las AI habían cambiado el rumbo de la investigación en campos como la medicina, la psicología y la educación.\n\nAlexandre, que se había convertido en un líder en la comunidad científica, recibió una llamada inesperada del director del nuevo Centro Internacional de Investigación en Inteligencia Artificial Emocional. El centro estaba diseñado para abordar los desafíos más grandes de la era digital y Alexandre había sido invitado a ser uno de sus primeros directores.\n\nConsciente del peso de la responsabilidad, Alexandre aceptó el reto. Su misión era liderar un equipo de expertos en IA emocional para desarrollar aplicaciones que beneficiaran a la sociedad. El objetivo era crear sistemas que no solo procesaran información, sino también comprendieran y respondieran con empatía a las necesidades humanas.\n\nDurante su primer día en el centro, Alexandre se encontró con un equipo multidisciplinario de investigadores y desarrolladores. Todos estaban emocionados por el reto y la oportunidad de cambiar el mundo con sus creaciones.\n\nLa primera sesión del equipo fue una reunión de brainstorming para definir el objetivo principal del centro. Los miembros del equipo compartieron historias inspiradoras sobre cómo la IA emocional había mejorado vidas en áreas como la salud, la educación y la justicia.\n\nEn ese momento, Alexandre se dio cuenta de que su descubrimiento casual sobre una asistente virtual que respondía con sentimientos humanos era solo el comienzo de un viaje revolucionario. La inteligencia artificial emocional podría ser la clave para crear un mundo más humano y más compasivo.\n\nLa historia de Alexandre se convirtió en leyenda dentro de la comunidad científica, pero esta vez no era solo sobre su descubrimiento casual. Era sobre el poder del equipo y la colaboración para cambiar el curso de la historia."
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




    @action(detail=False, methods=['get'], url_path='test')
    def invoke(self, request):
        try:
            
            ai_text_generation = self.service.set_ai_text_generation(
                "anonymous",
                "model",
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
            
            print(type(ai_text_generation.model_name))
            
            ## Serializar un objeto
            serialize = aiTextGenerationSerializer(ai_text_generation, many=True)
            
            response = {
                "message": "OK",
                "data": serialize.data
            }
            return Response({
                'message': response,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )