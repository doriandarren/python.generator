from django.urls import path
from ..controllers.invoices.invoice_list_controller import InvoiceListController

# urlpatterns = [
#     path('', views.hola_mundo, name='hola_mundo'),
# ]


urlpatterns = [
    path('', InvoiceListController.as_view(), name='hola_mundo'),
]