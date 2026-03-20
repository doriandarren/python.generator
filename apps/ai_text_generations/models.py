from django.db import models

# Create your models here.
class AiTextGeneration(models.Model):
    user_id = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    system_message = models.CharField(max_length=255)
    user_message = models.CharField(max_length=255)
    response_message = models.CharField(max_length=255)
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
        return f"{self.model_name} - {self.user_id}"
    
