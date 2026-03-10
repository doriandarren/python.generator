import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command_debug


def generate_app(full_path, plural_name_snake, venv_python, manage_py_path=None):
    install_app(full_path, plural_name_snake, venv_python)


def install_app(full_path, plural_name_snake, venv_python):
    print_message("Instalando app...", CYAN)

    apps_path = os.path.join(full_path, "apps")
    os.makedirs(apps_path, exist_ok=True)

    apps_init_path = os.path.join(apps_path, "__init__.py")
    if not os.path.exists(apps_init_path):
        with open(apps_init_path, "w", encoding="utf-8") as file:
            file.write("")

    app_path = os.path.join(apps_path, plural_name_snake)

    command = f'"{venv_python}" -m django startapp {plural_name_snake} "{app_path}"'
    run_command_debug(command, cwd=full_path)

    apps_py_path = os.path.join(app_path, "apps.py")
    if os.path.exists(apps_py_path):
        with open(apps_py_path, "r", encoding="utf-8") as file:
            content = file.read()

        content = content.replace(
            f"name = '{plural_name_snake}'",
            f"name = 'apps.{plural_name_snake}'"
        )

        with open(apps_py_path, "w", encoding="utf-8") as file:
            file.write(content)

    print_message("App instalada correctamente.", GREEN)

