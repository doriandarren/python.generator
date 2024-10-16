# generator/index.py

from repositories.to_api.create_models import generate_model_file
import os

if __name__ == "__main__":
    # Define la ruta directamente aquí
    base_path = os.path.dirname(os.path.dirname(__file__))  # Navegar un nivel hacia arriba desde la ubicación de 'index.py'
    ruta = os.path.join(base_path, 'api_project/invoices')

    # Definir el nombre singular y plural de la tabla
    singular_name = 'Invoice'
    plural_name = 'Invoices'

    # Definir las columnas de la tabla
    columns = [
        {"name": "name", "type": "CharField(max_length=255)"},
        {"name": "amount", "type": "DecimalField(max_digits=10, decimal_places=2)"},
        {"name": "created_at", "type": "DateTimeField(auto_now_add=True)"},
        {"name": "updated_at", "type": "DateTimeField(auto_now=True)"}
    ]

    # Verificar si la ruta proporcionada es válida
    if os.path.isdir(ruta):
        generate_model_file(ruta, singular_name, plural_name, columns)
    else:
        print("La ruta proporcionada no es válida o no existe. Por favor, verifica y vuelve a intentarlo.")
