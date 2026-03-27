from django.db import models

# Create your models here.
from core.models.models import BaseModel
    
class AiPromptGeneration(BaseModel):
    system_role = models.CharField(max_length=255)
    system_message = models.CharField(max_length=255)
    user_role = models.CharField(max_length=255)
    user_message = models.CharField(max_length=255)
    is_text_processed = models.BooleanField(default=False)
    is_image_processed = models.BooleanField(default=False)
    is_video_processed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "AiPromptGeneration"
        verbose_name_plural = "AiPromptGenerations"

    def __str__(self):
        return str(self.id)
    
