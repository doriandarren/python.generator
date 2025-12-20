## Python Generator

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
pip3 freeze > requirements.txt                  # Crear archivo requerimientos
pip3 install -r requirements.txt                # Instalar requerimientos


## Instalar paquetes
pip3 freeze                                     # Ver Paquetes instalados
pip3 install requests                           # Conexion API
pip3 install schedule                           # CronJobs


## Si no funciona VSCode:
( Cmd + Shift + P ) -> luego "Python: Select Interpreter" elegir ".venv/bin/python"

```

## Run

```sh
python3 cli.py
```

## Libraries

```sh

pip3 install questionary                 # Console / Terminal
pip3 install colorama                    # Console / Terminal
pip3 install requests                           # Conexion API
pip3 install schedule
pip3 install mysql-connector-python
pip3 install inflect

pip uninstall mysql-connector-python    ## Desinstalar cualquier error reintalar

```

## Adicionales

```sh

python -m pip install -U pip setuptools wheel
python -m pip install Cython

```
