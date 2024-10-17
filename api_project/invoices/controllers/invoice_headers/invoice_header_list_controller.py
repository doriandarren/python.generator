from rest_framework.views import APIView
from shared.base_controller import BaseController
from repositories.invoice_headers.invoice_header_repository import InvoiceHeaderRepository

class InvoiceHeaderListController(BaseController, APIView):

    def get(self, request):
        repository = InvoiceHeaderRepository()
        data = repository.list()
        return self.respond_with_data('InvoiceHeaders list', data)