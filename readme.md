## Python Generator

## Run

```sh
python3 cli.py
```

## Script para ejecutar el proyecto

```sh
python3 manage.py makemigrations                # Migraciones
python3 manage.py migrate                       # Aplicar migraciones
python3 manage.py createsuperuser               # Crear superuser
python3 manage.py runserver                     # Ejecutar servidor
```

## Ejecutar music CRON:

```sh
python3 run.py music

// OR

python -m ai.cronjobs.music.cronjob_music           ## Antiguo

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
pip3 install --upgrade pip


## Instala los requerimientos:
pip3 list
pip3 freeze > requirements.txt                  # Crear archivo requerimientos
pip3 install -r requirements.txt                # Instalar requerimientos


## Instalar paquetes
pip3 freeze                                     # Ver Paquetes instalados
pip3 install requests                           # Conexion API
pip3 install schedule                           # CronJobs


## Si no funciona VSCode:
( Cmd + Shift + P ) -> luego "Python: Select Interpreter" elegir ".venv/bin/python"

```

## Django

```sh
pip3 install django

django-admin shell                                      # Shell de django

## BY PROJECT
django-admin startproject nombre_proyecto               # Crear PROJECT
django-admin startproject nombre_proyecto .             # Crear PROJECT - No crea carpeta duplicada

## BY APP
python3 manage.py startapp nombre_app                   # Crear app
python3 manage.py startapp companies apps/companies

python manage.py migrate


## Crear el superuser
python3 manage.py createsuperuser

python3 manage.py runserver                             # Levantar el servidor
python3 manage.py runserver 8001

```

## Django - django_crontab

```sh
## En settings.py y Tener el archivo core/cron/hello_cron.py:
CRONJOBS = [
    ('*/1 * * * *', 'core.cron.hello_cron'),
]

python manage.py crontab add
python manage.py crontab show

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
