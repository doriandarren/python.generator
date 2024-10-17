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




Carpetas a crear:

core:

controllers
models
repositories
urls
views


