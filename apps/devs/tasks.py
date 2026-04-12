import random
import time
from celery import shared_task
from django.tasks import task
from apps.ai_prompt_generations.services.ai_prompt_generation_service import AiPromptGenerationService
from apps.devs.services.ai_generation_service import AIGenerationService
from core.messages.message_channel import MessageChannel


@shared_task
def start():
    
    service_prompt = AiPromptGenerationService()
    service_generation = AIGenerationService()
    
    
    # import requests

    # try:
    #     r = requests.get("http://192.168.1.100:11434/api/tags", timeout=5)
    #     MessageChannel.send(
    #         text=f"Ollama reachable. status={r.status_code}",
    #         title="CRON DEBUG",
    #     )
    # except Exception as e:
    #     MessageChannel.send(
    #         text=f"Ollama NO reachable: {str(e)}",
    #         title="CRON DEBUG",
    #         is_error=True
    #     )
    #     return
    
    
    try: 
        
        prompt = service_prompt.findByIsTextProcessed()
        # prompts = service_prompt.list()
        # prompt = prompts[random.randint(0, len(prompts) - 1)]
        
        if not prompt:
            return

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
            title="CRON ERROR TEXT GENERATION",
            is_error=True
        )
        
    
    return "ok"



@shared_task
def start2():
    service_prompt = AiPromptGenerationService()
    service_generation = AIGenerationService()
    
    try: 
        
        prompt = service_prompt.findByIsImageProcessed()
        
        # prompts = service_prompt.list()
        # prompt = prompts[random.randint(0, len(prompts) - 1)]

        if not prompt:
            return
        
        ## 2.-
        image_generation = service_generation.get_comfyui_image(prompt)
        
                
        # 3.-
        ##comfyui_prompt_id = '69a2442e-fd71-44b2-a0c1-d8142d213eb1'
        comfyui_prompt_id = image_generation.comfyui_prompt_id
        filename = service_generation.get_comfyui_image_history(comfyui_prompt_id, image_generation)
        
    
        
        # 4.- 
        image_download = service_generation.get_comfyui_image_download(filename)
        

        MessageChannel.send(
            text=f"invoke ejecutado: {time.time()} | ai_image_generation_id={image_generation.id}",
            title="CRON",
        )

    except Exception as e:
        MessageChannel.send(
            text=f"error: {str(e)}",
            title="CRON ERROR IMAGE GENERATION",
            is_error=True
        )
        
    
    return "ok"