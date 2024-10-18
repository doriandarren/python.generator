from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ...repositories.invoice_headers.invoice_header_repository import InvoiceHeaderRepository
import json

@method_decorator(csrf_exempt, name='dispatch')  # Excluir CSRF para simplificar
class InvoiceHeaderStoreController(View):

    def post(self, request):
        # Obtener los datos del cuerpo de la solicitud
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data'
            }, status=400)

        repository = InvoiceHeaderRepository()
        new_record = repository.store(data)
        
        return JsonResponse({
            'success': True,
            'message': 'InvoiceHeader created successfully',
            'data': new_record
        }, status=201)