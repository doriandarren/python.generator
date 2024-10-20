# string_helpers.py

def pluralize(word):
    """
    Pluraliza una palabra en inglés siguiendo reglas básicas.
    """
    if word.endswith('y') and word[-2] not in 'aeiou':
        return word[:-1] + 'ies'
    elif word.endswith(('s', 'x', 'z', 'sh', 'ch')):
        return word + 'es'
    else:
        return word + 's'

def get_plural(column_name):
    """
    Detecta si la columna contiene '_id', elimina el '_id' y devuelve su plural.
    """
    # Eliminar el '_id' si existe
    singular_word = column_name.replace('_id', '')

    # Pluralizar la palabra resultante
    return pluralize(singular_word)