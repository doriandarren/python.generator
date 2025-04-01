import questionary


questions = [

]


def menu():
    language = questionary.select(
        "¿Que quieres crear? ([P]royecto / [M]ódulo): ",
        choices=["Python", "JavaScript", "C++", "Java"]
    ).ask()

    print(f"Elegiste: {language}")

if __name__ == "__main__":
    menu()