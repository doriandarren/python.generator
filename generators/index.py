# generator/index.py

from repositories.to_api.create_models import create_model, generate_model_file
import os

if __name__ == "__main__":
    # Obtener la ruta base automáticamente a partir de la ubicación del archivo index.py
    base_path = os.path.dirname(os.path.dirname(__file__))  # Navegar un nivel hacia arriba desde la ubicación de 'index.py'
    ruta = os.path.join(base_path, 'invoices')  # Usar 'invoices' como ejemplo, cambia a la carpeta que necesites

    # Definir el nombre singular y plural de la tabla
    singular_name = 'Invoice'
    plural_name = 'Invoices'



    # Verificar si la ruta proporcionada es válida
    if os.path.isdir(ruta):
        create_model(ruta)
        models_path = os.path.join(ruta, 'models')
        generate_model_file(models_path, singular_name, plural_name)
    else:
        print("La ruta proporcionada no es válida o no existe. Por favor, verifica y vuelve a intentarlo.")
