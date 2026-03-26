import base64
import random

from apps.ai_text_generation_prompts.services.ai_text_generation_prompt_service import AiTextGenerationPromptService
from apps.ai_text_generations.services.ai_text_generation_service import AiTextGenerationService
from core.http.api_request import ApiRequest
from core.messages.message_channel import MessageChannel


api_ollama = ApiRequest("http://192.168.1.100:11434/")
api_confyui = ApiRequest("http://192.168.1.100:8188/")



class AIGenerationService:
   
    def __init__(self):
        self.service_text_generation_prompt = AiTextGenerationPromptService()
        self.service_text_generation = AiTextGenerationService()
        self.service_text_generation_prompt = AiTextGenerationPromptService()
   

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

            response_message = response.get("message", {}).get("content", "")
            response_done = response.get("done", "")
            response_done_reason = response.get("done_reason", "")
            response_total_duration = response.get("total_duration", "")
            response_load_duration = response.get("load_duration", "")
            response_prompt_eval_count = response.get("prompt_eval_count", "")
            response_prompt_eval_duration = response.get("prompt_eval_duration", "")
            response_eval_count = response.get("eval_count", "")
            response_eval_duration = response.get("eval_duration", "")

            ai_text_generation = self.service_text_generation.set_ai_text_generation(
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

            ai_text_generation_new = self.service_text_generation.store(ai_text_generation)
            self.service_text_generation_prompt.update(prompt.id, {"is_processed": True,})

            ##return aiTextGenerationSerializer(ai_text_generation)
            return ai_text_generation_new
            
        except Exception as e:
            MessageChannel.send(
                text=f"Error en get_comfyui_text: {str(e)}",
                title="AIGenerationService",
                is_error=True
            )
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

