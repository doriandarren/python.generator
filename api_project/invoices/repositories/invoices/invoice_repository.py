from api_project.models.invoices.invoice import Invoice
from datetime import datetime

class InvoiceRepository:
    def list(self):
        return Invoice.objects.all().order_by('-id')[:100]

    def show(self, invoice_id):
        return Invoice.objects.filter(id=invoice_id).first()

    def store(self, data):
        instance = Invoice(
            name=data.get('name'),
            amount=data.get('amount'),
            description=data.get('description')
        )
        instance.save()
        return instance

    def update(self, invoice_id, data):
        instance = Invoice.objects.filter(id=invoice_id).first()
        if not instance:
            return None

        if data.get('name') is not None:
                    instance.name = data.get('name')
        if data.get('amount') is not None:
                    instance.amount = data.get('amount')
        if data.get('description') is not None:
                    instance.description = data.get('description')

        instance.save()
        return instance

    def destroy(self, invoice_id):
        instance = Invoice.objects.filter(id=invoice_id).first()
        if instance:
            instance.delete()
            return True
        return False