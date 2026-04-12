## Python Generator

## Script para iniciar el proyecto

```sh

python3 -m venv .venv
source .venv/bin/activate 
pip install --upgrade pip
pip install -r requirements.txt

Crear raíz del proyecto: 
- Archivo .env
- Carpeta logs
- Carpeta media


python3 manage.py check                         # Comprobar dependencias
python3 manage.py makemigrations                # Migraciones
python3 manage.py migrate                       # Aplicar migraciones
python3 manage.py collectstatic --noinput       # Recopilar archivos estáticos
python3 manage.py seed_user                     # Crear superuser
python3 manage.py seed_default                  # Crear Prompts
python3 manage.py runserver                     # Ejecutar servidor
python3 manage.py runserver 0.0.0.0:8000        # Ejecutar servidor
```

## Crear entorno virtual

```sh
## Entorno virtual MacOs
- python3 -m venv .venv
- source .venv/bin/activate                     # Activar entorno
- deactive                                      # Desactivar entorno

## Entorno virtual Windows
- python3.exe -m venv venv                      # Windows
- .\venv\bin\activate                           # Windows
- python3.exe -m pip install --upgrade pip      # Windows
- deactivate                                    # Desactivar

## Actualizar
pip install --upgrade pip


## Instala los requerimientos:
pip list
pip freeze > requirements.txt                  # Crear archivo requerimientos
pip install -r requirements.txt                # Instalar requerimientos


## Instalar paquetes
pip freeze                                     # Ver Paquetes instalados
pip install requests                           # Conexion API
pip install schedule                           # CronJobs


## Si no funciona VSCode:
( Cmd + Shift + P ) -> luego "Python: Select Interpreter" elegir ".venv/bin/python"

```

## Django

```sh
pip install django

django-admin shell                                      # Shell de django

## BY PROJECT
django-admin startproject nombre_proyecto               # Crear PROJECT
django-admin startproject nombre_proyecto .             # Crear PROJECT - No crea carpeta duplicada

## BY APP
python3 manage.py startapp nombre_app                   # Crear app
python3 manage.py startapp companies apps/companies

python manage.py migrate


## Crear el superuser
python3 manage.py seed_user                             # Seeder
python3 manage.py createsuperuser                       # Consola Crear superuser



python3 manage.py runserver                             # Levantar el servidor
python3 manage.py runserver 8001

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
