from django.db import models

# Create your models here.
from core.models.models import BaseModel
    
class User(BaseModel):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return str(self.id)
    
