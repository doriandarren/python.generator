from django.db import models


class Invoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_number = models.CharField(max_length=100)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"Invoice {self.invoice_number}"