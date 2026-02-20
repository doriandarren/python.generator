import inflect

_p = inflect.engine()

def table_to_classes(table_snake: str) -> tuple[str, str]:
    """
    Recibe:  efidata_customers
    Devuelve: (singular_class, plural_class)
             ("EfidataCustomer", "EfidataCustomers")
    Reglas:
      - PascalCase uniendo por "_"
      - Singulariza SOLO la última palabra
    """
    parts = [p for p in table_snake.strip().split("_") if p]

    if not parts:
        return ("Unknown", "Unknowns")

    # Plural class: EfidataCustomers
    plural_class = "".join(p.capitalize() for p in parts)

    # Singular class: singulariza solo la última parte
    last = parts[-1]
    singular_last = _p.singular_noun(last)  # si era plural devuelve singular; si ya era singular -> False
    singular_last = singular_last if singular_last else last

    singular_parts = parts[:-1] + [singular_last]
    singular_class = "".join(p.capitalize() for p in singular_parts)

    return singular_class, plural_class
