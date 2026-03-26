import random
import time

from apps.ai_text_generation_prompts.services.ai_text_generation_prompt_service import AiTextGenerationPromptService
from apps.devs.services.ai_generation_service import AIGenerationService
from core.messages.message_channel import MessageChannel


def start():
    service_prompt = AiTextGenerationPromptService()
    service_generation = AIGenerationService()

    try:
        
        
        import requests

        try:
            r = requests.get("http://192.168.1.100:11434/api/tags", timeout=5)
            MessageChannel.send(
                text=f"Ollama reachable. status={r.status_code}",
                title="CRON DEBUG",
            )
        except Exception as e:
            MessageChannel.send(
                text=f"Ollama NO reachable: {str(e)}",
                title="CRON DEBUG",
                is_error=True
            )
            return
        
        
        
        
        
        prompts = service_prompt.list()

        if len(prompts) == 0:
            MessageChannel.send(
                text="No hay prompts disponibles",
                title="CRON",
                is_error=True
            )
            return

        prompt = prompts[random.randint(0, len(prompts) - 1)]

        ai_text_generation = service_generation.get_comfyui_text(prompt)

        if not ai_text_generation:
            MessageChannel.send(
                text=f"No se guardó ai_text_generation para el prompt_id={prompt.id}",
                title="CRON",
                is_error=True
            )
            return

        MessageChannel.send(
            text=f"invoke ejecutado: {time.time()} | ai_text_generation_id={ai_text_generation.id}",
            title="CRON",
        )

    except Exception as e:
        MessageChannel.send(
            text=f"error: {str(e)}",
            title="CRON",
            is_error=True
        )







def start____BK():
    
    # service_prompt = AiTextGenerationPromptService()
    # service_generation = AIGenerationService()
    
    
    try:
        pass  
        # prompt = self.service_prompt.findByIsProcessed()
        
        # 1.-
        # prompts = service_prompt.list()
        # prompt = prompts[random.randint(0, len(prompts)-1)]
        
        
        # ai_text_generation = service_generation.get_comfyui_text(prompt)
        
        
        # MessageChannel.send(
        #     text=f"invoke ejecutado: {time.time()}",
        #     title="CRON",
        # )
        
        
        
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
        
        
        # response = {
        #     "message": "OK",
        #     ##"text_generation": aiTextGenerationSerializer(ai_text_generation).data,
        #     "ai_text_generation": ai_text_generation.id,
        #     # "prompt_id": prompt_id,
        #     # "outputs": outputs,
        #     # "image_base64": image_base64
        # }
        # return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        MessageChannel.send(
            text=f"error: {str(e)}",
            title="CRON",
            is_error=True
        )

    