## Python Generator

## Script para iniciar el proyecto

```sh


## Script para ejecutar el proyecto

```sh
## Crear el entorno - Venv
python3 -m venv .venv
source .venv/bin/activate 
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Crear raíz del proyecto: 
- Archivo .env -> chmod 600 /var/www/vhosts/app1.com/api.app1.com/.env
- Carpeta logs
- Carpeta media


python manage.py check                         # Comprobar dependencias
python manage.py makemigrations                # Migraciones
python manage.py migrate                       # Aplicar migraciones
python manage.py collectstatic --noinput       # Recopilar archivos estáticos
python manage.py seed_user                     # Crear superuser
python manage.py seed_default                  # Crear Prompts
python manage.py runserver                     # Ejecutar servidor
python manage.py runserver 0.0.0.0:8000        # Ejecutar servidor
```

## Crear entorno virtual Venv

```sh
## Instala los requerimientos:
python -m pip freeze > requirements.txt          # Crear archivo requerimientos -> Respaldo / Export
python -m pip install -r requirements.txt        # Instalar requerimientos Restore / Import

## Si no se tiene el archivo: requirements.txt
python -m pip install pipreqs                    # Install
pipreqs . --force                                # Ejecutar

## Instalar paquetes
python -m pip freeze                            # Ver Paquetes instalados

## Si no funciona VSCode:
(Cmd + Shift + P) -> luego "Python: Select Interpreter" elegir ".venv/bin/python"
```



## Django

```sh
pip install django

django-admin shell                                      # Shell de django

## BY PROJECT
django-admin startproject nombre_proyecto               # Crear PROJECT
django-admin startproject nombre_proyecto .             # Crear PROJECT - No crea carpeta duplicada

## BY APP
python manage.py startapp nombre_app                   # Crear app
python manage.py startapp companies apps/companies

python manage.py migrate


## Crear el superuser
python manage.py seed_user                             # Seeder
python manage.py createsuperuser                       # Consola Crear superuser

python manage.py runserver                             # Levantar el servidor
python manage.py runserver 8001

```


## Commands

```sh
python3 manage.py seed_user                     # Crear superuser

python3 manage.py clear_migrations --dry-run     # Muestra las migraciones
python3 manage.py clear_migrations               # Elimina las migraciones

```


## Error: python manage.py makemigrations

```sh

## Error cuando se agrega el created_at al modelo:
opc: 1
>>> timezone.now()

```

## Eliminar Migraciones de Django

```sh
cd ruta/de/tu/proyecto
find ./apps -path "*/migrations/*.py" -not -name "__init__.py"
find ./apps -path "*/migrations/*.pyc"
```



## Libraries

```sh
pip install pdfkit                              # Crear PDF
```




# Celery y django-celery-beat

```sh

# Instalar
brew install redis

# Iniciar el servicio queda siempre
brew services start redis 

# Verificar
redis-cli ping





pip install celery django-celery-beat redis



- Archivo settings.py:

INSTALLED_APPS = [
    # ...
    "django_celery_beat",
]

python3 manage.py migrate


- Crear celery_app/celery.py y copiar: __init__.py y celery.py


- En settings.py:

CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_TIMEZONE = "Europe/Madrid"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"



- Cuando Celery arranca con -A, necesita saber dónde está la app (Manualmente):

celery -A celery_app worker -l info
celery -A celery_app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
python manage.py runserver

- Crear el archivo: start_celery.sh y permisos:
chmod +x start_celery.sh

# Arrancar:
./start_celery.sh

# Logs:
cat logs/django.log
cat logs/celery_worker.log
cat logs/celery_beat.log


```





# En ubuntu desktop: Guniocorn

```sh
python -m pip install gunicorn                              ## Instalar
gunicorn --bind 0.0.0.0:8000 passenger_wsgi:application     ## levantar el servidor


## Reinicar para efectos de cambios
Cuando cambies código:
sudo systemctl restart python-generator
sudo systemctl status python-generator

```

# En ubuntu desktop: Celery y django-celery-beat

```sh

sudo apt update
sudo apt install redis-server


sudo systemctl enable redis-server
sudo systemctl start redis-server

- sudo nano /etc/systemd/system/python-generator-celery.service              # Ver archivo Celery

- sudo nano /etc/systemd/system/python-generator-celery-beat.service         # Ver archivo Celery Beat


sudo systemctl daemon-reload

sudo systemctl start python-generator-celery
sudo systemctl start python-generator-celery-beat

sudo systemctl enable python-generator-celery
sudo systemctl enable python-generator-celery-beat


sudo systemctl restart python-generator-celery
sudo systemctl restart python-generator-celery-beat
```