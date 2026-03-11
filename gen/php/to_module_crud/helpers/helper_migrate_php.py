

def php_column_line(col: dict) -> str:
    """
    Traduce tu tipo interno a Blueprint de Laravel.
    Tipos soportados:
    - string
    - integer
    - float
    - decimal
    - boolean
    - fk
    """

    name = col["name"]
    t = (col.get("type") or "string").lower()

    # Foreign key (solo si viene marcado)
    if col.get("is_fk") or t == "fk":
        return f"                $table->unsignedBigInteger('{name}');\n"

    if t == "string":
        return f"                $table->string('{name}')->nullable();\n"

    if t == "integer":
        return f"                $table->integer('{name}')->nullable();\n"

    if t == "float":
        return f"                $table->float('{name}')->nullable();\n"

    if t == "decimal":
        return f"                $table->decimal('{name}', 13, 2)->nullable();\n"

    if t == "boolean":
        return f"                $table->boolean('{name}')->nullable();\n"
    
    if t == "date":
        return f"                $table->date('{name}')->nullable();\n"
    
    if t == "datetime":
        return f"                $table->datetime('{name}')->nullable();\n"
    
    if t == "time":
        return f"                $table->time('{name}')->nullable();\n"
    
    if t == "timestamp":
        return f"                $table->timestamp('{name}')->nullable();\n"

    # Fallback seguro
    return f"                $table->string('{name}')->nullable();\n"
