from django.urls import path
from api_project.invoices.controllers.invoice_headers.invoice_header_list_controller import InvoiceHeaderListController
from api_project.invoices.controllers.invoice_headers.invoice_header_show_controller import InvoiceHeaderShowController
from api_project.invoices.controllers.invoice_headers.invoice_header_store_controller import InvoiceHeaderStoreController
from api_project.invoices.controllers.invoice_headers.invoice_header_update_controller import InvoiceHeaderUpdateController
from api_project.invoices.controllers.invoice_headers.invoice_header_delete_controller import InvoiceHeaderDeleteController

urlpatterns = [
    path('list/', InvoiceHeaderListController.as_view(), name='invoice-header-list'),
    path('show/<int:invoice-header_id>/', InvoiceHeaderShowController.as_view(), name='invoice-header-show'),
    path('store/', InvoiceHeaderStoreController.as_view(), name='invoice-header-store'),
    path('update/<int:invoice-header_id>/', InvoiceHeaderUpdateController.as_view(), name='invoice-header-update'),
    path('delete/<int:invoice-header_id>/', InvoiceHeaderDeleteController.as_view(), name='invoice-header-delete'),
]