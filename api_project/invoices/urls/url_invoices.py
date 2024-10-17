from django.urls import path
from controllers.invoices.invoice_list_controller import InvoiceListController
from controllers.invoices.invoice_show_controller import InvoiceShowController
from controllers.invoices.invoice_store_controller import InvoiceStoreController
from controllers.invoices.invoice_update_controller import InvoiceUpdateController
from controllers.invoices.invoice_delete_controller import InvoiceDeleteController

urlpatterns = [
    # List route (GET)
    path('invoices/list/', InvoiceListController.as_view(), name='invoices-list'),

    # Show route (GET)
    path('invoices/show/<int:invoice_id>/', InvoiceShowController.as_view(), name='invoices-show'),

    # Store route (POST)
    path('invoices/store/', InvoiceStoreController.as_view(), name='invoices-store'),

    # Update route (PUT)
    path('invoices/update/<int:invoice_id>/', InvoiceUpdateController.as_view(), name='invoices-update'),

    # Delete route (DELETE)
    path('invoices/delete/<int:invoice_id>/', InvoiceDeleteController.as_view(), name='invoices-delete'),
]