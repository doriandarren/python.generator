from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ...repositories.invoice_headers.invoice_header_repository import InvoiceHeaderRepository
import json

@method_decorator(csrf_exempt, name='dispatch')
class InvoiceHeaderUpdateController(View):

    def put(self, request, invoice_header_id):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            }, status=400)

        repository = InvoiceHeaderRepository()
        updated_record = repository.update(invoice_header_id, data)

        if updated_record:
            return JsonResponse({
                'success': True,
                'message': 'InvoiceHeader updated successfully',
                'data': updated_record
            }, status=200)
        else:
            return JsonResponse({
                'success': False,
                'message': 'InvoiceHeader not found'
            }, status=404)