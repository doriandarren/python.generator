import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command
from gen.python_django.helpers.helper_file import helper_update_line, helper_update_list





def generate_api_doc(full_path, project_name_format, app_name, venv_python):
    """
    Genera el archivo
    """
    install_django(full_path, venv_python)
    update_settings(full_path, app_name)
    update_urls(full_path, project_name_format, app_name)
    
    

def install_django(full_path, venv_python):
    print_message("Instalando drf-yasg...", CYAN)
    run_command(f'"{venv_python}" -m pip install -U drf-yasg', cwd=full_path)
    print_message("drf-yasg instalado correctamente.", GREEN)
    

def update_settings(full_path, app_name):
    # helper_update_list(
    #     full_path, 
    #     f"{app_name}/settings.py", 
    #     "INSTALLED_APPS", 
    #     f"'django.contrib.staticfiles',       # required for serving swagger ui's css/js files"
    # )
    
    helper_update_list(
        full_path, 
        f"{app_name}/settings.py", 
        "INSTALLED_APPS", 
        f"'drf_yasg',                         # required for serving swagger")
    




def update_urls(full_path, project_name_format, app_name):
    
    str = f"from django.urls import path, include\n## Docs \nfrom django.urls import re_path\nfrom rest_framework import permissions\nfrom drf_yasg.views import get_schema_view\nfrom drf_yasg import openapi"
    
    str += f"""\n\nschema_view = get_schema_view(
   openapi.Info(
      title="{project_name_format.upper()} - API",
      default_version='v1',
      description="Documentation API {project_name_format.upper()}",
      terms_of_service="https://api.{project_name_format}.com/policies/terms/",
      contact=openapi.Contact(email="webmaster@{project_name_format}.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
    """
    
    # Update from
    helper_update_line(
        full_path,
        f"{app_name}/urls.py",
        f"from django.urls import path",
        str
    )
    
    
    
    # Update urlpatterns
    helper_update_list(
        full_path,
        f"{app_name}/urls.py",
        "urlpatterns = [",
        f"    # Docs"
    )
    
    helper_update_list(
        full_path,
        f"{app_name}/urls.py",
        "urlpatterns = [",
        f"    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),"
    )
    
    helper_update_list(
        full_path,
        f"{app_name}/urls.py",
        "urlpatterns = [",
        f"    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),"
    )
    
    helper_update_list(
        full_path,
        f"{app_name}/urls.py",
        "urlpatterns = [",
        f"    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),"
    )
    
    
