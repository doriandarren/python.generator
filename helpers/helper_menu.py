import os
import questionary
from helpers.helper_print import print_header


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_list(msg, choices):

    str_input = questionary.select(
        msg,
        choices=choices,
        use_indicator=True
    ).ask()

    return str_input



def pause():
    print("\n")
    questionary.text(
        "Presione ENTER para continuar ",
    ).ask()



def menu_checkbox(msg, choices_dict):

    choices = [
        questionary.Choice(title=label, value=value, checked=True)
        for label, value in choices_dict
    ]
    return questionary.checkbox(msg, choices=choices).ask()


