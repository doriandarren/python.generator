import base64
from math import e
import time
import random
from urllib.parse import urlencode

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
from core.messages.message_channel import MessageChannel


api_ollama = ApiRequest("http://192.168.1.100:11434/")
api_confyui = ApiRequest("http://192.168.1.100:8188/")


class DevApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = AiTextGenerationService()
        self.service_prompt = AiTextGenerationPromptService()

    @action(detail=False, methods=['get'], url_path='test_')
    def invoke_(self, request):

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
                "model": "gpt-oss:20b",
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
            response_prompt_eval_duration = response.get(
                "prompt_eval_duration", "")
            response_eval_count = response.get("eval_count", "")
            response_eval_duration = response.get("eval_duration", "")

            ai_text_generation = self.service.set_ai_text_generation(
                str(request.user.id) if request.user.is_authenticated else "anonymous",
                payload.get("model", ""),
                req_messages[0].get("content", "") if len(
                    req_messages) > 0 else "",
                req_messages[1].get("content", "") if len(
                    req_messages) > 0 else "",
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

                # Buscar por system_message y user_message
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



    def get_comfyui_image_base64(self, outputs):
        try:
            if not outputs:
                return ""
            
            for node_id, node_data in outputs.items():
                images = node_data.get("images", [])
                if images:
                    image = images[0]
                    
                    params = {
                        "filename": image.get("filename", ""),
                        "subfolder": image.get("subfolder", ""),
                        "type": image.get("type", ""),
                    }
                                        
                    
                    image_bytes = api_confyui.get_binary("view", params=params)

                    if image_bytes:
                        return base64.b64encode(image_bytes).decode("utf-8")
                    
            return ""
        
        except Exception:
            return ""
        


    def get_comfyui_text(self, prompt):
        try:
            payload = {
                "model": "gpt-oss:20b",
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
                1,
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

            ai_text_generation_new = self.service.store(ai_text_generation)
            self.service_prompt.update(prompt.id, {"is_processed": True,})

            ##return aiTextGenerationSerializer(ai_text_generation)
            return ai_text_generation_new
            
        except Exception:
            return None



    def get_comfyui_image(self, prompt):
        payload = {
            "client_id": "postman-mac-001",
            "prompt": {
                "3": {
                    "class_type": "KSampler",
                    "inputs": {
                        "seed": random.randint(1, 999999999),
                        "steps": 20,
                        "cfg": 7,
                        "sampler_name": "euler",
                        "scheduler": "normal",
                        "denoise": 1,
                        "model": ["4", 0],
                        "positive": ["6", 0],
                        "negative": ["7", 0],
                        "latent_image": ["5", 0]
                    }
                },
                "4": {
                    "class_type": "CheckpointLoaderSimple",
                    "inputs": {
                        "ckpt_name": "sd_xl_base_1.0.safetensors"
                    }
                },
                "5": {
                    "class_type": "EmptyLatentImage",
                    "inputs": {
                        "width": 1024,
                        "height": 1024,
                        "batch_size": 1
                    }
                },
                "6": {
                    "class_type": "CLIPTextEncode",
                    "inputs": {
                        "text": prompt.system_message,
                        "clip": ["4", 1]
                    }
                },
                "7": {
                    "class_type": "CLIPTextEncode",
                    "inputs": {
                        "text": "blurry, low quality, distorted, bad anatomy, deformed, ugly",
                        "clip": ["4", 1]
                    }
                },
                "8": {
                    "class_type": "VAEDecode",
                    "inputs": {
                        "samples": ["3", 0],
                        "vae": ["4", 2]
                    }
                },
                "9": {
                    "class_type": "SaveImage",
                    "inputs": {
                        "filename_prefix": "postman_test",
                        "images": ["8", 0]
                    }
                }
            }
        }
        response_prompt = api_confyui.post("/prompt", payload)
        
        prompt_id = response_prompt.get("prompt_id", "")
        
        return prompt_id




    @action(detail=False, methods=['get'], url_path='test')
    def invoke(self, request):  
        try:
            
            MessageChannel.send(
                text=f"invoke ejecutado: {time.time()}",
                title="CRON",
            )
            
            #prompt = self.service_prompt.findByIsProcessed()
            
            
            
            # 1.-
            # prompts = self.service_prompt.list()
            # prompt = prompts[random.randint(0, len(prompts)-1)]
            
            # if not prompt:
            #     return Response(
            #         {
            #             "message": "No prompt found"
            #         },
            #         status=status.HTTP_400_BAD_REQUEST
            #     )
            
            # ai_text_generation = self.get_comfyui_text(prompt)
            
            # print(type(ai_text_generation))
            
            
            
            # 2.-
            # prompt_id = self.get_comfyui_image(prompt)
            # if not prompt_id:
            #     return Response(
            #         {"error": "No se pudo obtener el prompt_id"},
            #         status=status.HTTP_500_INTERNAL_SERVER_ERROR
            #     )
         
                   
            # 3.-
            # response_history = {}
            # outputs = {}
            # image_base64 = ""
            
            # for _ in range(30):
            #     response_history = api_confyui.get(f"/history/{prompt_id}")
                
            #     if response_history and response_history.get(prompt_id):
            #         data = response_history.get(prompt_id, {})
            #         outputs = data.get("outputs", {})
            #         if outputs:
            #             image_base64 = self.get_comfyui_image_base64(outputs)
            #             break
                
            #     time.sleep(1)
            
            
            response = {
                "message": "OK",
                ##"text_generation": aiTextGenerationSerializer(ai_text_generation).data,
                "ai_text_generation": ai_text_generation.id,
                # "prompt_id": prompt_id,
                # "outputs": outputs,
                # "image_base64": image_base64
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
