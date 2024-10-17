from shared.base_controller import BaseController
from repositories.invoices.invoice_repository import InvoiceRepository

class InvoiceListController(BaseController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = InvoiceRepository()

    def get(self, request):
        data = self.repository.list()
        return self.respond_with_data('Invoices list', data)