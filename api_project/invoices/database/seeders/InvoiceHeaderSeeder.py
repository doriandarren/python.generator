from faker import Faker
from api_project.models.invoice_headers.invoice_header import InvoiceHeader

def create_fake_invoice_header():
    fake = Faker()

    for _ in range(10):  # Generar 10 registros falsos
        InvoiceHeader.objects.create(
            name=fake.company(),
            amount=fake.pydecimal(left_digits=5, right_digits=2, positive=True)(),
            description=fake.text(),
        )
    print("10 registros falsos de InvoiceHeader creados con éxito.")