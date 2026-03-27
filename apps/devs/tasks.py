import random
import time
from celery import shared_task
from apps.ai_text_generation_prompts.services.ai_text_generation_prompt_service import AiTextGenerationPromptService
from apps.devs.services.ai_generation_service import AIGenerationService
from core.messages.message_channel import MessageChannel


@shared_task
def start():
    
    service_prompt = AiTextGenerationPromptService()
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
        
    
    return "ok"