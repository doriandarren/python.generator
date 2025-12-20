from helpers.helper_print import input_with_validation
from php.to_project.batch_processes.generate_batch_processes import generate_batch_processes
from php.to_project.dev.generate_execute_controller import generate_execute_controller
from php.to_project.dev.generate_route_test import generate_route_test
from php.to_project.dev.generate_test_controller import generate_test_controller
from php.to_project.excel.generate_maatwebsite_excel import generate_maatwebsite_excel
from php.to_project.exceptions.generate_exception_handler import generate_exception_handler
from php.to_project.exceptions.generate_exception_handler_response import generate_exception_handler_response
from php.to_project.fpdf_merge.generate_fpdf_merge import generate_fpdf_merge
from php.to_project.generate_base_controller import generate_base_controller
from php.to_project.generate_by_command_line import generate_by_command_line
from php.to_project.auth.generate_module_auth import generate_module_auth
from php.to_project.generate_enums import generate_enums
from php.to_project.images.generate_company_logos import generate_company_logos
from php.to_project.scripts.generate_shared_postman_collections import generate_shared_postman_collections
from php.to_project.shared.generate_shared import generate_shared
from php.to_project.snappy.generate_snappy import generate_snappy
from php.to_project.updates.update_app_php import update_app_php
from php.to_project.updates.update_bootstrap_app_php import update_bootstrap_app_php
from php.to_project.updates.update_gitignore import update_gitignore
from php.to_project.updates.update_model_user_php import update_model_user
from php.to_project.updates.update_readme import update_readme
from php.to_project.updates.update_route_api_php import update_route_api_php
from php.to_project.updates.update_welcome_blade import update_welcome_blade
from php.to_project.utilities.generate_utilities import generate_utilities


def start_project_php():
    # Ruta predeterminada
    default_path = "/Users/dorian/PhpstormProjects81"

    project_name = input_with_validation("Nombre del proyecto: ", None)
    project_path = input(f"Ruta para crear el proyecto (por defecto: {default_path}): ").strip()

    # Si no se introduce una ruta, usar la predeterminada
    if not project_path:
        project_path = default_path

    # Combinar la ruta y el nombre del proyecto
    full_path = f"{project_path}/{project_name}"


    # Crear el proyecto
    generate_by_command_line(full_path)

    # Crear Snappy
    generate_snappy(full_path)
    
    # Crear FPDF Merge
    generate_fpdf_merge(full_path)

    # Crear Excel
    generate_maatwebsite_excel(full_path)

    # Enums
    generate_enums(full_path)


    # Crear batch
    generate_batch_processes(full_path)


    # Controller & Base Controller
    generate_base_controller(full_path)


    # Controllers
    generate_module_auth(full_path)


    # Shared
    generate_shared(full_path)


    # Utilities
    generate_utilities(full_path)


    # Updates
    update_model_user(full_path)
    update_app_php(full_path)
    update_bootstrap_app_php(full_path)
    update_readme(full_path)
    update_gitignore(full_path)


    # Dev
    generate_execute_controller(full_path)
    generate_test_controller(full_path)
    generate_route_test(full_path)


    # Logos
    generate_company_logos(full_path)


    # Welcome
    update_welcome_blade(full_path)


    # Postaman
    generate_shared_postman_collections(full_path) ## TODO Pending


    # Exceptions
    ## generate_exception_handler(full_path)
    ## generate_exception_handler_response(full_path)


    # route api
    update_route_api_php(full_path)