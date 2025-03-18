from php.to_api.start_module import start_module
from php.to_create_project.start_project import start_project
from php.utils.utils import input_with_validation




if __name__ == "__main__":

    print("**********************  PHP   **********************")
    namespace = input_with_validation("¿Que quieres crear? ([P]royecto / [M]ódulo): ")

    if namespace.lower() == 'p':
        start_module()
    if namespace.lower() == 'm':
        start_project()

    print("Bye...")













