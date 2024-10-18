from django.urls import path
from ..controllers.invoice_headers.invoice_header_list_controller import InvoiceHeaderListController
from ..controllers.invoice_headers.invoice_header_show_controller import InvoiceHeaderShowController

urlpatterns = [
    path('list/', InvoiceHeaderListController.as_view(), name='invoice-header-list'),
    path('show/<int:invoice_header_id>/', InvoiceHeaderShowController.as_view(), name='invoice-header-show'),
]