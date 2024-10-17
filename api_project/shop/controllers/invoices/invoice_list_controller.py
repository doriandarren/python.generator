from django.http import JsonResponse
from django.views import View
from ...repositories.invoices.invoice_repository import InvoiceRepository


class InvoiceListController(View):
    def get(self, request):
        repository = InvoiceRepository()

        # Definir el array de 2 registros básicos
        data = repository.list()

        # Construir la respuesta JSON
        response_data = {
            'message': 'Shop items list',
            'success': True,
            'data': data
        }

        return JsonResponse(response_data, status=200)
