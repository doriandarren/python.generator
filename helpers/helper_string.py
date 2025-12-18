import re
import inflect

p = inflect.engine()

def convert_word(word):
    """
    Convierte una palabra o frase a su forma singular y plural,
    eliminando guiones bajos al inicio y al final y formateando
    el resultado en PascalCase (cada palabra con mayúscula).

    Args:
        word (str): La palabra o frase a convertir.

    Returns:
        dict: Un diccionario con las formas singular y plural en PascalCase.
    """
    # Limpiar guiones bajos al inicio y al final
    clean_word = word.strip('_')

    # Separar por guiones bajos internos
    words = clean_word.split('_')
    last_word = words[-1]  # Tomar la última palabra para pluralizar o singularizar

    # Verificar si la última palabra está en plural
    singular_last = p.singular_noun(last_word)

    if singular_last:
        # Si estaba en plural, convertir a singular
        singular_form_list = words[:-1] + [singular_last]
        plural_form_list = words  # La palabra original es plural
    else:
        # Si estaba en singular, convertir a plural
        plural_last = p.plural(last_word)
        singular_form_list = words  # La palabra original es singular
        plural_form_list = words[:-1] + [plural_last]

    # Convertir a PascalCase (cada palabra con la primera letra en mayúscula)
    singular_form = ''.join(word.capitalize() for word in singular_form_list)
    plural_form = ''.join(word.capitalize() for word in plural_form_list)

    return {
        "singular": singular_form,
        "plural": plural_form
    }




def normalize_project_name(project_name: str) -> str:
    """
    Normaliza el nombre del proyecto para usarlo como identificador seguro.
    
    Ejemplos:
    - prices.avanazaoil.eu -> prices_avanazaoil_eu
    - app-1 -> app_1
    - App-1 -> app_1
    """
    if not project_name:
        return ""

    # 1) minúsculas
    name = project_name.lower()

    # 2) reemplazar cualquier cosa que no sea letra o número por _
    name = re.sub(r"[^a-z0-9]+", "_", name)

    # 3) eliminar _ repetidos
    name = re.sub(r"_+", "_", name)

    # 4) quitar _ al inicio o final
    return name.strip("_")












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
    print(convert_word("customer_plates_authorizations"))