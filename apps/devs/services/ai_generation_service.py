import base64
import random
import time
from apps.ai_image_generations.services.ai_image_generation_service import AiImageGenerationService
from apps.ai_prompt_generations.services.ai_prompt_generation_service import AiPromptGenerationService
from apps.ai_text_generations.services.ai_text_generation_service import AiTextGenerationService

from core.http.api_request import ApiRequest
from core.messages.message_channel import MessageChannel


api_ollama = ApiRequest("http://192.168.1.100:11434/")
api_confyui = ApiRequest("http://192.168.1.100:8188/")



class AIGenerationService:
   
    def __init__(self):
        self.service_prompt_generation = AiPromptGenerationService()
        self.service_text_generation = AiTextGenerationService()
        self.service_image_generation = AiImageGenerationService()
   

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
            self.service_prompt_generation.update(prompt.id, {"is_processed": True,})

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
        
        client_id = f"postman-mac-001"
        seed = random.randint(1, 999999999)
        filename_prefix = f"postman_test_{seed}"
        width = 1024
        height = 1024
        clip_text_encode = "blurry, low quality, distorted, bad anatomy, deformed, ugly"
        
        
        payload = {
            "client_id": client_id,
            "prompt": {
                "3": {
                    "class_type": "KSampler",
                    "inputs": {
                        "seed": seed,
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
                        "width": width,
                        "height": height,
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
                        "text": clip_text_encode,
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
                        "filename_prefix": filename_prefix,
                        "images": ["8", 0]
                    }
                }
            }
        }
        
        response_prompt = api_confyui.post("/prompt", payload)
        
        image_prompt_id = response_prompt.get("prompt_id", "")
        
        
        ## TODO guardar en DB
        
        image_image_generation_obj = self.service_image_generation.set_ai_image_generation(
            ai_prompt_generation_id=prompt.id,
            comfyui_prompt_id=image_prompt_id,
            comfyui_output_path=f"outputs/{filename_prefix}",
            mime_type="image/png",
            width=width,
            height=height,
            image_url=""
        )
        
        image_image_generation = self.service_image_generation.store(image_image_generation_obj)
        
        
        return image_image_generation




    def get_comfyui_image_history(self, comfyui_prompt_id):
        try:
            for _ in range(30):
                response_history = api_confyui.get(path=f"history/{comfyui_prompt_id}")

                if not response_history:
                    time.sleep(1)
                    continue

                data = response_history.get(comfyui_prompt_id)

                if not data:
                    time.sleep(1)
                    continue
                
                # 🔥 comprobar si ya terminó
                status = data.get("status", {})
                completed = status.get("completed", False)

                if not completed:
                    time.sleep(1)
                    continue

                # 🔥 ahora sí leer outputs
                outputs = data.get("outputs", {})

                if outputs:
                    return outputs
                    
                    
            return None

        except Exception as e:
            MessageChannel.send(
                text=f"Error en get_comfyui_image_history: {str(e)}",
                title="AIGenerationService",
                is_error=True
            )
            return None
   
   
   
   
   
   
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

