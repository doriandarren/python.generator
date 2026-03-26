import random

from apps.ai_text_generation_prompts.services.ai_text_generation_prompt_service import AiTextGenerationPromptService
from apps.devs.services.ai_generation_service import AIGenerationService
from core.messages.message_channel import MessageChannel


class AIGenerationJob:
    def handle(self):
        service_prompt = AiTextGenerationPromptService()
        service_generation = AIGenerationService()

        prompts = list(service_prompt.list())

        if not prompts:
            MessageChannel.send(
                text="No hay prompts disponibles",
                title="SCHEDULER",
                is_error=True
            )
            return

        prompt = random.choice(prompts)

        ai_text_generation = service_generation.get_comfyui_text(prompt)

        if not ai_text_generation:
            MessageChannel.send(
                text=f"No se guardó ai_text_generation para el prompt_id={prompt.id}",
                title="SCHEDULER",
                is_error=True
            )
            return

        MessageChannel.send(
            text=f"OK ai_text_generation_id={ai_text_generation.id}",
            title="SCHEDULER",
        )