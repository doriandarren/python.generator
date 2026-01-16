import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command
from python_django.helpers.helper_file import helper_append_content, helper_update_list

def generate_cron(full_path, project_name_format, app_name, venv_python):
    """
    Genera el archivo
    """
    install_cron(full_path, venv_python)
    update_settings(full_path, project_name_format, app_name)
    create_file_init(full_path)
    create_core_cron(full_path)



def install_cron(full_path, venv_python):
    print_message("Instalando django-crontab...", CYAN)
    run_command(f'"{venv_python}" -m pip install django-crontab', cwd=full_path)
    print_message("django-crontab instalado correctamente.", GREEN)
    

    
def update_settings(full_path, project_name_format, app_name):
    
    helper_update_list(
        full_path, 
        f"{app_name}/settings.py", 
        "INSTALLED_APPS", 
        f"'django_crontab',                   # required for cronjobs"
    )    
    
    
    str = f"""\n# CronJobs
CRONJOBS = [
    ("*/1 * * * *", "core.cron.hello_cron"),                      # cada minuto (para probar)
]
    """
    
    helper_append_content(
        full_path, 
        f"{app_name}/settings.py", 
        str
    )
    
    

def create_core_cron(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "core", "cron")
    file_path = os.path.join(folder_path, "cron.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''from django.utils import timezone

def hello_cron():
    print(f"[CRON] hello_cron ejecutado: {{timezone.now()}}")
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)




def create_file_init(full_path):
    """
    Genera el archivo init
    """
    folder_path = os.path.join(full_path, "core", "cron")
    file_path = os.path.join(folder_path, "__init__.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f''''''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

