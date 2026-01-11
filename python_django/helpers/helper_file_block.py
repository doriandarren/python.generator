import os


def get_file_path(full_path, relative_path):
    return os.path.join(full_path, relative_path)


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def find_python_assignment_block(content, var_name):
    """
    Encuentra el bloque completo de asignación Python:
      VAR_NAME = { ... }
    Devuelve una tupla: (start_index, end_index, block_text)
    """
    target = var_name
    idx = content.find(target)

    if idx == -1:
        return None

    # Buscar '=' desde var_name hacia delante
    eq = content.find("=", idx)
    if eq == -1:
        return None

    # Buscar el primer delimitador '{' '[' '(' tras '='
    i = eq + 1
    while i < len(content) and content[i] not in "{[(":
        i += 1

    if i >= len(content):
        return None

    open_char = content[i]
    close_char = {"{": "}", "[": "]", "(": ")"}[open_char]

    start = idx  # empezamos desde el nombre de la variable

    level = 0
    j = i
    while j < len(content):
        if content[j] == open_char:
            level += 1
        elif content[j] == close_char:
            level -= 1
            if level == 0:
                end = j + 1
                block_text = content[start:end]
                return start, end, block_text
        j += 1

    return None


def replace_python_assignment_block(content, var_name, new_block):
    """
    Reemplaza un bloque tipo:
      DATABASES = {...}
    por new_block (texto completo).

    new_block debe incluir el nombre de variable:
      DATABASES = {...}
    """
    found = find_python_assignment_block(content, var_name)
    if not found:
        return content, False

    start, end, old_block = found

    # Asegurar salto de línea al final del bloque insertado
    if not new_block.endswith("\n"):
        new_block += "\n"

    updated = content[:start] + new_block + content[end:]
    return updated, True


def replace_block_in_file(full_path, relative_path, var_name, new_block):
    """
    Lee el archivo, reemplaza el bloque y lo guarda.
    """
    file_path = get_file_path(full_path, relative_path)
    content = read_file(file_path)

    updated, replaced = replace_python_assignment_block(content, var_name, new_block)
    if replaced:
        write_file(file_path, updated)

    return replaced
