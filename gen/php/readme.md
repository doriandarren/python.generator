


## Funcion por si acaso de PHP 
Carga desde php/main.py

```sh

def load():

    # Namespace
    # namespace = "INVOICES"
    # namespace = "API"
    namespace = "ERP"


    # Ruta del proyecto
    # ruta = "/Users/dorian/PhpstormProjects81/php84/api.splytin.com/"
    # ruta = "/Users/dorian/PhpstormProjects81/portuarios.globalfleet.es/"
    ruta = "/Users/dorian/PhpstormProjects81/harineras-api.globalfleet.es/"


    # Definir tabla
    ##singular_name = 'AgendaUnloading'
    singular_name = 'Device'
    plural_name = 'Devices'

    columns = [
        {"name": "company_id"},
        {"name": "vehicle_id"},
        {"name": "box_id"},
        {"name": "unit_id"},
        {"name": "model"},
        {"name": "model_ver"},
        {"name": "installed"},
        {"name": "imei"},
        {"name": "serial"},
        {"name": "phone"},
    ]

    generate(namespace, ruta, singular_name, plural_name, columns)


```


