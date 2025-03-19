from php.to_api.start_module import start_module
from php.to_create_project.start_project import start_project
from helpers.helper_print import input_with_validation
from colorama import Fore



if __name__ == "__main__":

    print(Fore.GREEN + "****************************************************")
    print(Fore.GREEN + "*******             PHP                    *********")
    print(Fore.GREEN + "****************************************************")

    namespace = input_with_validation("¿Que quieres crear? ([P]royecto / [M]ódulo): ")

    if namespace.lower() == 'p':
        start_project()
    if namespace.lower() == 'm':
        start_module()

    print("Bye...")













