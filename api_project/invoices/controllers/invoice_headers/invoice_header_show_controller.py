from django.http import JsonResponse
from django.views import View
from ...repositories.invoice_headers.invoice_header_repository import InvoiceHeaderRepository

class InvoiceHeaderShowController(View):

    def get(self, request, invoice_header_id):
        repository = InvoiceHeaderRepository()
        data = repository.show(invoice_header_id)
        if data:
            return JsonResponse({
                'success': True,
                'message': 'InvoiceHeader show',
                'data': data
            }, status=200)
        else:
            return JsonResponse({
                'success': False,
                'message': 'InvoiceHeader show'
            }, status=404)