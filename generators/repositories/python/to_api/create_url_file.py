import os


def create_urls_structure(base_path):
    # Ruta completa para la carpeta 'urls'
    urls_path = os.path.join(base_path, 'urls')

    # Verificar si la carpeta 'urls' ya existe, si no, crearla y agregar __init__.py
    if not os.path.exists(urls_path):
        try:
            os.makedirs(urls_path)
            print(f"Carpeta 'urls' creada exitosamente en: {urls_path}")

            # Crear un archivo '__init__.py' dentro de la carpeta 'urls'
            init_file_path = os.path.join(urls_path, '__init__.py')
            with open(init_file_path, 'w') as init_file:
                init_file.write('# Este archivo convierte a la carpeta urls en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file_path}")

        except Exception as e:
            print(f"Error al crear la carpeta 'urls' o el archivo '__init__.py': {e}")
    else:
        print(f"La carpeta 'urls' ya existe en: {urls_path}")

        # Verificar si '__init__.py' existe en la carpeta 'urls', si no, crearlo
        init_file_path = os.path.join(urls_path, '__init__.py')
        if not os.path.exists(init_file_path):
            with open(init_file_path, 'w') as init_file:
                init_file.write('# Este archivo convierte a la carpeta urls en un módulo de Python')
                print(f"Archivo '__init__.py' creado en: {init_file_path}")
        else:
            print(f"El archivo '__init__.py' ya existe en: {init_file_path}")

    return urls_path


def create_url_file(base_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake,
                    plural_name_snake):
    # Crear la estructura de URLs
    urls_path = create_urls_structure(base_path)

    # Ruta completa para el archivo de URLs que queremos crear (ejemplo: 'url_invoices.py')
    url_file_path = os.path.join(urls_path, f'url_{plural_name_kebab}.py')

    # Contenido base del archivo de URLs
    controller_imports = f"""
from django.urls import path
from controllers.{plural_name_snake}.{singular_name_snake}_list_controller import {singular_name}ListController
from controllers.{plural_name_snake}.{singular_name_snake}_show_controller import {singular_name}ShowController
from controllers.{plural_name_snake}.{singular_name_snake}_store_controller import {singular_name}StoreController
from controllers.{plural_name_snake}.{singular_name_snake}_update_controller import {singular_name}UpdateController
from controllers.{plural_name_snake}.{singular_name_snake}_delete_controller import {singular_name}DeleteController
"""

    urlpatterns = f"""
urlpatterns = [
    # List route (GET)
    path('{plural_name_kebab}/list/', {singular_name}ListController.as_view(), name='{plural_name_kebab}-list'),

    # Show route (GET)
    path('{plural_name_kebab}/show/<int:{singular_name_kebab}_id>/', {singular_name}ShowController.as_view(), name='{plural_name_kebab}-show'),

    # Store route (POST)
    path('{plural_name_kebab}/store/', {singular_name}StoreController.as_view(), name='{plural_name_kebab}-store'),

    # Update route (PUT)
    path('{plural_name_kebab}/update/<int:{singular_name_kebab}_id>/', {singular_name}UpdateController.as_view(), name='{plural_name_kebab}-update'),

    # Delete route (DELETE)
    path('{plural_name_kebab}/delete/<int:{singular_name_kebab}_id>/', {singular_name}DeleteController.as_view(), name='{plural_name_kebab}-delete'),
]
"""

    url_content = controller_imports + urlpatterns

    # Escribir el archivo de URLs
    try:
        with open(url_file_path, 'w') as url_file:
            url_file.write(url_content.strip())
            print(f"Archivo 'url_{plural_name_kebab}.py' creado exitosamente en: {url_file_path}")
    except Exception as e:
        print(f"Error al crear el archivo 'url_{plural_name_kebab}.py': {e}")
