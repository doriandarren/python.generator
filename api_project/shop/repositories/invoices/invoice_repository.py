from shop.models.invoice import Invoice


class InvoiceRepository:

    def list(self):

        invoices = Invoice.objects.all()


        data = [
            {
                'invoice_number': invoice.invoice_number,
                'date': invoice.date,
                'total_amount': invoice.total_amount
            } for invoice in invoices
        ]

        return data

        # Este es un array de ejemplo con dos registros
        # return [
        #     {'id': 1, 'name': 'Invoice 1', 'total': 100},
        #     {'id': 2, 'name': 'Invoice 2', 'total': 200}
        # ]

