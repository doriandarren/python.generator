from django.db import models
from core.models.models import BaseModel

    
class AiTextGenerationPrompt(BaseModel):
    system_role = models.CharField(max_length=255)
    system_message = models.CharField(max_length=255)
    user_role = models.CharField(max_length=255)
    user_message = models.CharField(max_length=255)
    is_processed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "AiTextGenerationPrompt"
        verbose_name_plural = "AiTextGenerationPrompts"

    def __str__(self):
        return str(self.id)
    
