from django.urls import path
from controllers.invoice_headers.invoice_header_list_controller import InvoiceHeaderListController
from controllers.invoice_headers.invoice_header_show_controller import InvoiceHeaderShowController
from controllers.invoice_headers.invoice_header_store_controller import InvoiceHeaderStoreController
from controllers.invoice_headers.invoice_header_update_controller import InvoiceHeaderUpdateController
from controllers.invoice_headers.invoice_header_delete_controller import InvoiceHeaderDeleteController

urlpatterns = [
    # List route (GET)
    path('invoice-headers/list/', InvoiceHeaderListController.as_view(), name='invoice-headers-list'),

    # Show route (GET)
    path('invoice-headers/show/<int:invoice-header_id>/', InvoiceHeaderShowController.as_view(), name='invoice-headers-show'),

    # Store route (POST)
    path('invoice-headers/store/', InvoiceHeaderStoreController.as_view(), name='invoice-headers-store'),

    # Update route (PUT)
    path('invoice-headers/update/<int:invoice-header_id>/', InvoiceHeaderUpdateController.as_view(), name='invoice-headers-update'),

    # Delete route (DELETE)
    path('invoice-headers/delete/<int:invoice-header_id>/', InvoiceHeaderDeleteController.as_view(), name='invoice-headers-delete'),
]