from django.db import models

# Create your models here.
class Dev(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Dev"
        verbose_name_plural = "Devs"

    def __str__(self):
        return str(self.name)
    
