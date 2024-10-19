from django.urls import path
from ..controllers.invoice_headers.invoice_header_list_controller import InvoiceHeaderListController
from ..controllers.invoice_headers.invoice_header_show_controller import InvoiceHeaderShowController
from ..controllers.invoice_headers.invoice_header_store_controller import InvoiceHeaderStoreController
from ..controllers.invoice_headers.invoice_header_update_controller import InvoiceHeaderUpdateController
from ..controllers.invoice_headers.invoice_header_delete_controller import InvoiceHeaderDeleteController

urlpatterns = [
    path('list', InvoiceHeaderListController.as_view(), name='invoice-header-list'),
    path('show/<int:invoice_header_id>', InvoiceHeaderShowController.as_view(), name='invoice-header-show'),
    path('store', InvoiceHeaderStoreController.as_view(), name='invoice-header-store'),
    path('update/<int:invoice_header_id>', InvoiceHeaderUpdateController.as_view(), name='invoice-header-update'),
    path('delete/<int:invoice_header_id>', InvoiceHeaderDeleteController.as_view(), name='invoice-header-delete'),
]