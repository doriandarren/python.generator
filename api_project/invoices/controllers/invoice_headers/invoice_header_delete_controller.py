from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ...repositories.invoice_headers.invoice_header_repository import InvoiceHeaderRepository

@method_decorator(csrf_exempt, name='dispatch')
class InvoiceHeaderDeleteController(View):

    def delete(self, request, invoice_header_id):
        
        repository = InvoiceHeaderRepository()
        deleted_record = repository.delete(invoice_header_id)

        if deleted_record:
            return JsonResponse({
                'success': True,
                'message': 'InvoiceHeader deleted successfully',
                'data': None 
            }, status=200)
        else:
            return JsonResponse({
                'success': False,
                'message': 'InvoiceHeader not found'
            }, status=404)