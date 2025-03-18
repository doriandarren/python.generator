from react.to_create_module.generate_module_standard import generate_module_standard
from react.utils.utils import print_message, GREEN, CYAN
from react.to_create_project.generate_components import generate_components
from react.to_create_project.generate_react_router import generate_react_router
from react.to_create_project.generate_images import generate_images
from to_create_project.generate_by_command_line import generate_by_command_line
from to_create_project.generate_project_structure import generate_project_structure
from to_create_project.generate_styles import generate_styles
from to_create_project.generate_public_layouts import generate_public_layouts
from to_create_project.generate_private_layouts import generate_private_layouts
from to_create_project.generate_module_public import generate_module_public
from to_create_project.generate_module_dashboard import generate_module_dashboard
from to_create_project.generate_module_auth import generate_module_auth
from to_create_project.generate_redux import generate_redux
from to_create_project.generate_helpers import generate_helpers
from to_create_project.generate_translate import generate_translate
from to_create_project.generate_env import generate_env
from to_create_project.generate_gitignore import generate_gitignore
from to_create_project.generate_readme import generate_readme
from to_create_project.generate_index_html import generate_index_html
from to_create_project.generate_folder_api import generate_folder_api
from to_create_project.generate_module_teams import generate_module_teams
from to_create_project.generate_module_profile import generate_module_profile


# Función para manejar input con validación y valores por defecto
def input_with_validation(prompt, default_value=None):
    while True:  # Bucle para solicitar una entrada válida
        if default_value:  # Si hay un valor por defecto, se muestra
            user_input = input(f"{prompt} [{default_value}]: ").strip()
            if user_input:  # Si el usuario escribe algo, lo retorna
                return user_input
            return default_value  # Si presiona Enter, usa el valor por defecto
        else:  # Si no hay un valor por defecto
            user_input = input(f"{prompt}").strip()
            if user_input:  # Si el usuario escribe algo, lo retorna
                return user_input
            print("La entrada no puede estar en blanco. Por favor, inténtalo de nuevo.")


def start_project():
    # Ruta predeterminada
    default_path = "/Users/dorian/ReactProjects"

    project_name = input("Introduce el nombre del proyecto React: ")
    project_path = input(f"Introduce la ruta donde deseas crear el proyecto (por defecto: {default_path}): ").strip()

    # Si no se introduce una ruta, usar la predeterminada
    if not project_path:
        project_path = default_path

    # Combinar la ruta y el nombre del proyecto
    full_path = f"{project_path}/{project_name}"


    generate_by_command_line(full_path)

    generate_project_structure(full_path)

    generate_styles(full_path)
    generate_images(full_path)



    ## Layouts
    generate_public_layouts(full_path)
    generate_private_layouts(full_path)



    ## generate Public
    generate_module_public(full_path)

    ## React Router
    generate_react_router(full_path)


    generate_components(full_path)


    # Dashboard
    generate_module_dashboard(full_path)

    # Auth
    generate_module_auth(full_path)

    ## Profile
    generate_module_profile(full_path)

    # Teams
    generate_module_teams(full_path)


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






    # Mensaje final
    print_message(f"¡Proyecto React creado exitosamente en {full_path}!", GREEN)
    print_message(f"Para empezar: cd {full_path} && npm run dev", CYAN)





def start_module():

    project_path = "/Users/dorian/ReactProjects/"

    folder_project = input_with_validation("Carpeta Proyecto: ")
    singular_name = input_with_validation("Nombre singular (AgendaUnloading): ", None)
    plural_name = input_with_validation("Nombre plural (AgendaUnloadings): ", None)
    input_columns = input_with_validation("Columnas: ", None)

    columns = [{"name": column} for column in input_columns.split()]
    project_path = project_path + folder_project + "/"

    generate_module_standard(project_path, singular_name, plural_name, columns)






if __name__ == "__main__":

    print("**********************  REACT   **********************")
    namespace = input_with_validation("¿Que quieres crear? ([P]royecto / [M]ódulo): ")

    if namespace.lower() == 'p':
        start_project()
    if namespace.lower() == 'm':
        start_module()

    print("Bye...")



# portuarios-office.globalfleet.es
# AgendaUnloading / AgendaUnloadings : transporeon_code name msoft_code
# AgendaUpload / AgendaUploads : transporeon_code name msoft_code
# Service / Services : description service_code
# Item / Items : description transporeon_item_id msoft_item_id
# Tow / Tows : transporeon_plate msoft_plate