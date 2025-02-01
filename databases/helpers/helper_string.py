import inflect

p = inflect.engine()

def convert_word(word):
    """
    Convierte una palabra o frase a su forma singular y plural,
    manejando guiones bajos al inicio y al final.

    Args:
        word (str): La palabra o frase a convertir.

    Returns:
        dict: Un diccionario con las formas singular y plural.
    """
    # Guardar los guiones bajos al inicio y al final
    prefix = ''
    suffix = ''
    if word.startswith('_'):
        prefix = '_'
    if word.endswith('_'):
        suffix = '_'

    # Remover guiones bajos para procesar
    clean_word = word.strip('_')
    words = clean_word.split('_')  # Separar por guiones bajos
    last_word = words[-1]          # Última palabra para singular/plural

    # Verificar si la última palabra está en plural
    singular_last = p.singular_noun(last_word)

    if singular_last:
        # Si estaba en plural, convertir a singular
        singular_form = '_'.join(words[:-1] + [singular_last])
        plural_form = clean_word  # La palabra original es plural
    else:
        # Si estaba en singular, convertir a plural
        plural_last = p.plural(last_word)
        singular_form = clean_word  # La palabra original es singular
        plural_form = '_'.join(words[:-1] + [plural_last])

    # Restaurar los guiones bajos originales
    singular_form = f"{prefix}{singular_form}{suffix}"
    plural_form = f"{prefix}{plural_form}{suffix}"

    return {
        "singular": singular_form,
        "plural": plural_form
    }









## ---------------------------
## Only Test
## ---------------------------
if __name__ == "__main__":
    print(convert_word("_vehicle"))  # {'singular': 'vehicle', 'plural': 'vehicles'}
    print(convert_word("vat_types"))  # {'singular': 'vat_type', 'plural': 'vat_types'}
    print(convert_word("web_contact_form_log"))  # {'singular': 'web_contact_form_log', 'plural': 'web_contact_form_logs'}
    print(convert_word("vehicle"))  # {'singular': 'vehicle', 'plural': 'vehicles'}
    print(convert_word("vat_type"))  # {'singular': 'web_contact_form_log', 'plural': 'web_contact_form_logs'}
    print(convert_word("_station_products_"))  # {'singular': 'web_contact_form_log', 'plural': 'web_contact_form_logs'}
    print(convert_word("_station_product_"))  # {'singular': 'web_contact_form_log', 'plural': 'web_contact_form_logs'}