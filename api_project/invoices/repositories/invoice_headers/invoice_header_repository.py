from api_project.invoices.models.invoice_headers.invoice_header import InvoiceHeader

class InvoiceHeaderRepository:

    def list(self):
        return InvoiceHeader.objects.all()

    def get(self, invoice_header_id):
        try:
            return InvoiceHeader.objects.get(id=invoice_header_id)
        except InvoiceHeader.DoesNotExist:
            return None

    def create(self, data):
        invoice_header = InvoiceHeader(**data)
        invoice_header.save()
        return invoice_header

    def update(self, invoice_header_id, data):
        invoice_header = self.get(invoice_header_id)
        if invoice_header:
            for key, value in data.items():
                setattr(invoice_header, key, value)
            invoice_header.save()
        return invoice_header

    def delete(self, invoice_header_id):
        invoice_header = self.get(invoice_header_id)
        if invoice_header:
            invoice_header.delete()
        return invoice_header