
class InvoiceRepository:

    def list(self):
        # Este es un array de ejemplo con dos registros
        return [
            {'id': 1, 'name': 'Invoice 1', 'total': 100},
            {'id': 2, 'name': 'Invoice 2', 'total': 200}
        ]