from django.http import JsonResponse
from django.views import View
from ...repositories.invoice_headers.invoice_header_repository import InvoiceHeaderRepository


class InvoiceHeaderListController(View):

    def get(self, request):
        # Crear una instancia del repositorio
        repository = InvoiceHeaderRepository()
            
        # Obtener los datos del repositorio
        data = repository.list()
        
        data = {
            'message': 'InvoiceHeaders list',
            'data': data,
            'success': True
        }
        return JsonResponse(data, status=200)