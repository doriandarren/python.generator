def parse_columns_input(input_columns: str):
    """
    Convierte un string tipo:
    'customer_id:fk name:string amount:float description has_active:boolean'
    en una lista de diccionarios bien formados.
    """

    allowed_types = {"string", "integer", "float", "decimal", "boolean", "fk", "date", "datetime", "email", "timestamp"}

    columns = []

    for token in input_columns.split():
        parts = token.split(":")

        name = parts[0].strip()
        col_type = parts[1].strip() if len(parts) > 1 else "string"

        if col_type not in allowed_types:
            raise ValueError(f"Tipo de columna no soportado: '{col_type}' en '{token}'")

        col = {
            "name": name,
            "type": col_type,
            "is_fk": col_type == "fk",
        }

        # Si es FK, inferimos la tabla relacionada por defecto
        if col["is_fk"]:
            base = name
            if base.endswith("_id"):
                base = base[:-3]  # quitar '_id'
            col["related_table"] = base + "s"  # muy estilo Laravel

        columns.append(col)

    return columns
