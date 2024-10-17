from shared.base_controller import BaseController
from repositories.invoiceheaders.invoiceheader_repository import InvoiceHeaderRepository

class InvoiceHeaderListController(BaseController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.repository = InvoiceHeaderRepository()

    def get(self, request):
        data = self.repository.list()
        return self.respond_with_data('InvoiceHeaders list', data)