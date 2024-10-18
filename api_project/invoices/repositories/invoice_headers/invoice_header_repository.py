from invoices.models.invoice_headers.invoice_header import InvoiceHeader
from django.forms.models import model_to_dict

class InvoiceHeaderRepository:

    def list(self, columns=None):
        # Usar columnas proporcionadas o columnas predeterminadas
        if columns is None:
            columns = ['id', 'name', 'amount', 'description', 'created_at', 'updated_at']
        invoice_headers = InvoiceHeader.objects.all()
        data = list(invoice_headers.values(*columns))
        return data
        

    def show(self, invoice_header_id):
        try:
            # Obtener el objeto y convertirlo a un diccionario serializable
            obj = InvoiceHeader.objects.get(id=invoice_header_id)
            return model_to_dict(obj)
        except InvoiceHeader.DoesNotExist:
            return None
            

    def store(self, data):
        invoice_header = InvoiceHeader(**data)
        invoice_header.save()
        
        invoice_header_dict = model_to_dict(invoice_header, fields=[field.name for field in invoice_header._meta.fields])
    
        if 'created_at' not in invoice_header_dict:
            invoice_header_dict['created_at'] = invoice_header.created_at
        if 'updated_at' not in invoice_header_dict:
            invoice_header_dict['updated_at'] = invoice_header.updated_at
            
        return invoice_header_dict
        

    def update(self, invoice_header_id, data):
        invoice_header = self.show(invoice_header_id)
        if invoice_header:
            for key, value in data.items():
                setattr(invoice_header, key, value)
            invoice_header.save()
            
            # Convertir el objeto actualizado en un diccionario
            invoice_header_dict = model_to_dict(invoice_header, fields=[field.name for field in invoice_header._meta.fields])

            if 'created_at' not in invoice_header_dict:
                invoice_header_dict['created_at'] = invoice_header.created_at
            if 'updated_at' not in invoice_header_dict:
                invoice_header_dict['updated_at'] = invoice_header.updated_at
            
            return invoice_header_dict
        return None
        

    def delete(self, invoice_header_id):
        invoice_header = self.show(invoice_header_id)
        if invoice_header:
            invoice_header.delete()
        return invoice_header