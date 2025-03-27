from php.to_api.start_module import start_module
from php.to_create_project.start_project import start_project
from helpers.helper_print import input_with_validation, print_header




if __name__ == "__main__":

    print_header("PHP")

    namespace = input_with_validation("¿Que quieres crear? ([P]royecto / [M]ódulo): ")

    if namespace.lower() == 'p':
        start_project()
    if namespace.lower() == 'm':
        start_module()

    print("Bye...")













