import os

def create_urls_structure(base_path):
    # Crear la carpeta 'urls' si no existe
    urls_path = os.path.join(base_path, 'urls')
    if not os.path.exists(urls_path):
        os.makedirs(urls_path)
        print(f"Carpeta 'urls' creada en: {urls_path}")

    # Crear el archivo '__init__.py' en la carpeta 'urls' para que sea un módulo de Python
    init_file = os.path.join(urls_path, '__init__.py')
    if not os.path.exists(init_file):
        with open(init_file, 'w') as f:
            f.write('# Este archivo convierte a la carpeta en un módulo de Python')
            print(f"Archivo '__init__.py' creado en: {init_file}")

    return urls_path

def create_url_file(base_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, namespace, app_name):
    # Crear la estructura de carpetas para las URLs
    urls_path = create_urls_structure(base_path)

    # Nombre del archivo de URLs (usando plural_name_snake)
    url_file_path = os.path.join(urls_path, f'url_{plural_name_snake}.py')

    # Contenido del archivo de URLs utilizando el namespace, app_name y los controladores
    url_content = f"""
from django.urls import path
from {namespace}.{app_name}.controllers.{plural_name_snake}.{singular_name_snake}_list_controller import {singular_name}ListController
from {namespace}.{app_name}.controllers.{plural_name_snake}.{singular_name_snake}_show_controller import {singular_name}ShowController
from {namespace}.{app_name}.controllers.{plural_name_snake}.{singular_name_snake}_store_controller import {singular_name}StoreController
from {namespace}.{app_name}.controllers.{plural_name_snake}.{singular_name_snake}_update_controller import {singular_name}UpdateController
from {namespace}.{app_name}.controllers.{plural_name_snake}.{singular_name_snake}_delete_controller import {singular_name}DeleteController

urlpatterns = [
    path('list/', {singular_name}ListController.as_view(), name='{singular_name_kebab}-list'),
    path('show/<int:{singular_name_kebab}_id>/', {singular_name}ShowController.as_view(), name='{singular_name_kebab}-show'),
    path('store/', {singular_name}StoreController.as_view(), name='{singular_name_kebab}-store'),
    path('update/<int:{singular_name_kebab}_id>/', {singular_name}UpdateController.as_view(), name='{singular_name_kebab}-update'),
    path('delete/<int:{singular_name_kebab}_id>/', {singular_name}DeleteController.as_view(), name='{singular_name_kebab}-delete'),
]
"""

    # Escribir el archivo de URLs
    try:
        with open(url_file_path, 'w') as url_file:
            url_file.write(url_content.strip())
            print(f"Archivo 'url_{plural_name_snake}.py' creado exitosamente en: {url_file_path}")
    except Exception as e:
        print(f"Error al crear el archivo de URLs 'url_{plural_name_snake}.py': {e}")
