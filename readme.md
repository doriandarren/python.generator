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

## Libraries

```sh

pip3 install questionary                 # Console / Terminal
pip3 install colorama                    # Console / Terminal
pip3 install requests                           # Conexion API
pip3 install schedule
pip3 install inflect


pip install pymysql                                       ## Desinstalar cualquier error reintalar
pip install sqlalchemy psycopg2-binary alembic python-dotenv


pip uninstall mysql-connector-python    ## Desinstalar cualquier error reintalar


python -m pip install -U pip setuptools wheel
python -m pip install Cython

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

## Prompt

```sh

Para que entiendas el conexto que necesito. Tengo una carpeta en la raíz del proyecto por ejemplo: apps/AiTextGenerationPrompt/api. Con estas carpetas: router.py, serializers.py y views.py

router.py:

from rest_framework.routers import DefaultRouter
from apps.ai_text_generation_prompts.api.views import AiTextGenerationPromptApiViewSet

# example
router_ai_text_generation_prompt = DefaultRouter()

# examples
router_ai_text_generation_prompt.register(
    prefix='ai_text_generation_prompts',
    basename='ai_text_generation_prompts',
    viewset=AiTextGenerationPromptApiViewSet
)


serializers.py:

from rest_framework.serializers import ModelSerializer
from apps.ai_text_generation_prompts.models import AiTextGenerationPrompt


class aiTextGenerationPromptSerializer(ModelSerializer):

    class Meta:
        model = AiTextGenerationPrompt
        ## fields = "__all__"
        fields = ['id', 'system_role','system_message','user_role','user_message','is_processed']

views.py:

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend

from apps.ai_text_generation_prompts.api.serializers import AiTextGenerationPromptSerializer
from apps.ai_text_generation_prompts.models import AiTextGenerationPrompt


class AiTextGenerationPromptApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AiTextGenerationPromptSerializer
    queryset = AiTextGenerationPrompt.objects.all()

```
