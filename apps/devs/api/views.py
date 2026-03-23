from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from apps.ai_text_generation_prompts.data.data_prompt import get_data_prompts
from apps.ai_text_generation_prompts.services.ai_text_generation_prompt_service import AiTextGenerationPromptService
from apps.ai_text_generations.api.serializers import aiTextGenerationSerializer
from apps.ai_text_generations.services.ai_text_generation_service import AiTextGenerationService
from core.http.api_request import ApiRequest

api_ollama = ApiRequest("http://192.168.1.100:11434/")


class DevApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = AiTextGenerationService()
        self.service_prompt = AiTextGenerationPromptService()
    
    

    @action(detail=False, methods=['get'], url_path='test')
    def invoke(self, request):

        try:
            
            prompt = self.service_prompt.findByIsProcessed()
            
            
            if not prompt:
                return Response(
                    {
                        "message": "No prompt found"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            
            payload = {
                "model": "llama3:latest",
                "messages": [
                    {
                        "role": "system",
                        "content": prompt.system_message
                    },
                    {
                        "role": "user",
                        "content": prompt.user_message
                    }
                ],
                "stream": False
            }

            response = api_ollama.post(
                path="api/chat",
                payload=payload
            )


            req_messages = payload.get("messages") or []
            
            
            response_message = response.get("message", "").get("content", "")
            response_done = response.get("done", "")
            response_done_reason = response.get("done_reason", "")
            response_total_duration = response.get("total_duration", "")
            response_load_duration = response.get("load_duration", "")
            response_prompt_eval_count = response.get("prompt_eval_count", "")
            response_prompt_eval_duration = response.get("prompt_eval_duration", "")
            response_eval_count = response.get("eval_count", "")
            response_eval_duration = response.get("eval_duration", "")
            


            ai_text_generation = self.service.set_ai_text_generation(
                str(request.user.id) if request.user.is_authenticated else "anonymous",
                payload.get("model", ""),
                req_messages[0].get("content", "") if len(req_messages) > 0 else "",
                req_messages[1].get("content", "") if len(req_messages) > 0 else "",
                response_message,
                response_done,
                response_done_reason,
                response_total_duration,
                response_load_duration,
                response_prompt_eval_count,
                response_prompt_eval_duration,
                response_eval_count,
                response_eval_duration,
            )
            
            self.service.store(ai_text_generation)
            
            
            serialize = aiTextGenerationSerializer(ai_text_generation)
            
            self.service_prompt.update(
                prompt.id,
                {
                    "is_processed": True,
                }
            )
            
            return Response({
                'response': response,
                'data': serialize.data
            }, status=status.HTTP_200_OK)


        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )





    @action(detail=False, methods=['get'], url_path='test__')
    def invoke__(self, request):
        try:
            
            
            for payload in get_data_prompts():
                
                ## Buscar por system_message y user_message
                ai_text_generation_prompt = self.service_prompt.list().filter(
                    system_message=payload.get("system_message", ""),
                    user_message=payload.get("user_message", ""),
                ).first()
                
                if ai_text_generation_prompt:
                    continue
                
                ai_text_generation_prompt = self.service_prompt.set_ai_text_generation_prompt(
                    payload.get("system_role", ""),
                    payload.get("system_message", ""),
                    payload.get("user_role", ""),
                    payload.get("user_message", ""),
                    False,
                )
                
                self.service_prompt.store(ai_text_generation_prompt)
                
            
            response = {
                "message": "OK"
            }
            return Response({
                'message': response,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )