from django.db import models

# Create your models here.
from core.models.models import BaseModel
    
class AiImageGeneration(BaseModel):
    ai_prompt_generation = models.ForeignKey("ai_prompt_generations.AiPromptGeneration", on_delete=models.CASCADE, related_name="ai_image_generations")
    comfyui_prompt_id = models.CharField(max_length=255)
    comfyui_output_path = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    image_url = models.CharField(max_length=255)

    class Meta:
        verbose_name = "AiImageGeneration"
        verbose_name_plural = "AiImageGenerations"

    def __str__(self):
        return str(self.id)
    
