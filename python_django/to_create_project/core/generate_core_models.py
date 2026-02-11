import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_core_models(full_path):
    create_file_init(full_path)
    create_file_models(full_path)
    


def create_file_models(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "core", "models")
    file_path = os.path.join(folder_path, "models.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created"
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated"
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]

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
    folder_path = os.path.join(full_path, "core", "hmodelss")
    file_path = os.path.join(folder_path, "__init__.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f''''''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)