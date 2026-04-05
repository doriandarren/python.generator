from django.db import models

# Create your models here.
from core.models.models import BaseModel
    
class AiPromptCategory(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "AiPromptCategory"
        verbose_name_plural = "AiPromptCategories"

    def __str__(self):
        return str(self.name)
    
