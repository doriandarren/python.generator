from django.urls import path
from api_project.invoices.controllers.invoice_headers.invoice_header_list_controller import InvoiceHeaderListController

urlpatterns = [
    path('list/', InvoiceHeaderListController.as_view(), name='invoice-header-list'),
]