from django.db import models

# Create your models here.
from core.models.models import BaseModel
    
class AgendaUnloading(BaseModel):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = "AgendaUnloading"
        verbose_name_plural = "AgendaUnloadings"

    def __str__(self):
        return str(self.name)
    
