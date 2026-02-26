import os
from gen.helpers.helper_menu import pause
from gen.helpers.helper_print import RED, dd, print_message, GREEN, CYAN, input_with_validation
from gen.react.to_create_project.components.generate_components import generate_components
from gen.react.to_create_project.generate_modules import generate_modules
from gen.react.to_create_project.generate_react_router import generate_react_router
from gen.react.to_create_project.generate_images import generate_images
from gen.react.to_create_project.generate_by_command_line import generate_by_command_line
from gen.react.to_create_project.generate_styles import generate_styles
from gen.react.to_create_project.generate_public_layouts import generate_public_layouts
from gen.react.to_create_project.generate_private_layouts import generate_private_layouts
from gen.react.to_create_project.generate_module_public import generate_module_public
from gen.react.to_create_project.generate_module_dashboard import generate_module_dashboard
from gen.react.to_create_project.generate_module_auth import generate_module_auth
from gen.react.to_create_project.generate_redux import generate_redux
from gen.react.to_create_project.file_helpers.generate_helpers import generate_helpers
from gen.react.to_create_project.generate_translate import generate_translate
from gen.react.to_create_project.generate_env import generate_env
from gen.react.to_create_project.generate_gitignore import generate_gitignore
from gen.react.to_create_project.generate_readme import generate_readme
from gen.react.to_create_project.generate_index_html import generate_index_html
from gen.react.to_create_project.generate_folder_api import generate_folder_api
from gen.react.to_create_project.generate_module_profile import generate_module_profile
from gen.react.to_create_project.role_permissions.generate_helper_allowed_paths import generate_helper_allowed_paths
from gen.react.to_create_project.role_permissions.generate_helper_build_accessible_nav import generate_generate_helper_build_accessible_nav
from gen.react.to_create_project.role_permissions.generate_helper_role_menu_access import generate_helper_role_menu_access



def start_project_react():
    
    # Defaults
    default_path = "/Users/dorian/ReactProjects"
    default_name = "app1.com"

    # Inputs
    project_name = input_with_validation(
        f"Nombre del proyecto",
        default_name
    )
    project_path = input_with_validation(
        f"Ruta del proyecto",
        default_path
    )

    # Join Full Path
    full_path = f"{project_path}/{project_name}"
    
    

    generate_by_command_line(full_path)
    generate_styles(full_path) 
    generate_images(full_path) 


    ## Layouts
    generate_private_layouts(full_path)
    generate_public_layouts(full_path)


    ## generate Public
    generate_module_public(full_path)

    ## React Router
    generate_react_router(full_path)

    generate_components(full_path)

    # Dashboard
    generate_module_dashboard(full_path)

    # Auth
    generate_module_auth(full_path, project_name)

    ## Profile
    generate_module_profile(full_path)

    # Modules
    generate_modules(full_path)

    # Redux
    generate_redux(full_path)

    # Helpers
    generate_helpers(full_path)

    # Translate
    generate_translate(full_path) 

    generate_env(full_path)

    generate_gitignore(full_path)

    generate_readme(full_path)

    ## index.html
    generate_index_html(full_path)

    generate_folder_api(full_path)
    
    ## Roles and Permission
    generate_helper_allowed_paths(full_path)
    generate_generate_helper_build_accessible_nav(full_path)
    generate_helper_role_menu_access(full_path)
    

    # Mensaje final
    print_message(f"¡Proyecto React creado exitosamente en {full_path}!", GREEN)
    print_message(f"Para empezar: cd {full_path} && npm run dev", CYAN)
    


    pause()