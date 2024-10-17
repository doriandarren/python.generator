from api_project.models.invoiceheaders.invoiceheader import InvoiceHeader
from datetime import datetime

class InvoiceHeaderRepository:
    def list(self):
        return InvoiceHeader.objects.all().order_by('-id')[:100]

    def show(self, invoiceheader_id):
        return InvoiceHeader.objects.filter(id=invoiceheader_id).first()

    def store(self, data):
        instance = InvoiceHeader(
            name=data.get('name'),
            amount=data.get('amount'),
            description=data.get('description')
        )
        instance.save()
        return instance

    def update(self, invoiceheader_id, data):
        instance = InvoiceHeader.objects.filter(id=invoiceheader_id).first()
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

    def destroy(self, invoiceheader_id):
        instance = InvoiceHeader.objects.filter(id=invoiceheader_id).first()
        if instance:
            instance.delete()
            return True
        return False