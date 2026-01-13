import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_readme(full_path, project_name):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path)
    file_path = os.path.join(folder_path, "readme.md")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''## {project_name}


## Ejecutar

```sh
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py createsuperuser

```

## Crear entorno virtual

```sh
## Entorno virtual MacOs
- python3 -m venv .venv
- source .venv/bin/activate                     # Activar entorno
- deactive                                      # Desactivar entorno

## Entorno virtual Windows
- py -m venv .venv                              # Windows
- .\.venv\Scripts\\activate                     # Windows
- py -m pip install --upgrade pip               # Windows
- deactivate                                    # Desactivar
- py -m pip xxx                                 # Usar este comando para intrucciones

## Actualizar
pip3 install --upgrade pip


## Instala los requerimientos:
pip3 freeze > requirements.txt                  # Crear archivo requerimientos -> Respaldo / Export
pip3 install -r requirements.txt                # Instalar requerimientos Restore / Import

## Si No se tiene el archivo: requirements.txt
pip install pipreqs                             # Install
pipreqs . --force                               # Ejecutar


## Instalar paquetes
pip3 freeze                                     # Ver Paquetes instalados
py -m pip freeze                                # Para Windows
pip3 install requests                           # Conexion API
pip3 install schedule                           # CronJobs


## Si no funciona VSCode:
( Cmd + Shift + P ) -> luego "Python: Select Interpreter" elegir ".venv/bin/python"
```

# Docker

```sh

## levantar con Docker:
docker compose up -d

## Opcional:
docker compose down -v                          ## Borra la BD
docker compose up -d                            ## Se levanta de nuevo

```


## Django

```sh

## BY PROJECT
django-admin startproject nombre_proyecto       # Crear PROJECT
django-admin startproject nombre_proyecto .     # Crear PROJECT - No crea carpeta duplicada

## BY APP
python3 manage.py startapp nombre_app           # Crear app

python manage.py migrate

python3 manage.py runserver                     # Levantar el servidor
python3 manage.py runserver 8001

```

# CronJobs

```sh
python3 manage.py crontab add                   ## Agregar los jobs instalados
python3 manage.py crontab show                  ## Ver los jobs instalados
python3 manage.py crontab remove                ## Quitar todos los jobs de django-crontab
```

'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)