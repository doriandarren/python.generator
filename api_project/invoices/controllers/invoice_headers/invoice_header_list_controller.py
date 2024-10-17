from api_project.shared.base_controller import BaseController
from api_project.invoices.repositories.invoice_headers.invoice_header_repository import InvoiceHeaderRepository
from rest_framework.views import APIView

class InvoiceHeaderListController(BaseController, APIView):

    def get(self, request):
        repository = InvoiceHeaderRepository()
        data = repository.list()
        return self.respond_with_data('InvoiceHeaders list', data)