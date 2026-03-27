from django.db import models

# Create your models here.
from core.models.models import BaseModel
    
class AiTextGeneration(BaseModel):
    ai_prompt_generation = models.ForeignKey("ai_prompt_generations.AiPromptGeneration", on_delete=models.CASCADE, related_name="ai_text_generations")
    model_name = models.CharField(max_length=255)
    response_message = models.TextField()
    response_done = models.CharField(max_length=255)
    response_done_reason = models.CharField(max_length=255)
    response_total_duration = models.CharField(max_length=255)
    response_load_duration = models.CharField(max_length=255)
    response_prompt_eval_count = models.CharField(max_length=255)
    response_prompt_eval_duration = models.CharField(max_length=255)
    response_eval_count = models.CharField(max_length=255)
    response_eval_duration = models.CharField(max_length=255)

    class Meta:
        verbose_name = "AiTextGeneration"
        verbose_name_plural = "AiTextGenerations"

    def __str__(self):
        return str(self.id)
    
