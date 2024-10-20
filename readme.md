## Python Generator - Django

- Django 5.1


### Crear un entorno virtual

```sh
// Crear
python3 -m venv venv

// Activar
source venv/bin/activate

```


### Instalar Django

```sh

pip install --upgrade pip
pip install django

django-admin --version

```



### Instalación adicional

```sh
// Mysql
pip install mysqlclient


```



### Crear Proyecto en Django

```sh

django-admin startproject api_project   // Crea el proyecto
cd api_project                          // cambia directorio
python manage.py startapp generators    // crea la estructura

```


### Migrations

```sh

// Crear superuser
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver 8001


Para models

python manage.py makemigrations shop
// Y luego para aplicar
python manage.py migrate

python manage.py showmigrations
python manage.py makemigrations
python manage.py migrate


```

### Extensions - URLs

```sh

pip install django-extensions

// Agregar:
INSTALLED_APPS = [
  ...
  'django_extensions', ## Extensions -> python manage.py show_urls
  ...
]
python manage.py show_urls.     // muestras las routes

```

### Extensions - Quitar Slash al final de las routes

```sh

// settings.py add:
APPEND_SLASH = False

```


### Extensions - Faker

```sh

pip install faker

 python manage.py shell < invoices/database/seeders/InvoiceHeaderSeeder.py


```







