## helpers/helper_file.py
import os


## ---------------------------------------
## ---- Replace CONTENT
## ---------------------------------------

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


##############
## Use by call
##############
def helper_replace_block(full_path, relative_path, var_name, new_block):
    """
    Lee el archivo, reemplaza el bloque y lo guarda.
    """
    file_path = get_file_path(full_path, relative_path)
    content = read_file(file_path)

    updated, replaced = replace_python_assignment_block(content, var_name, new_block)
    if replaced:
        write_file(file_path, updated)

    return replaced





## ---------------------------------------
## ---- Add IMPORTS
## ---------------------------------------

def ensure_import_in_content(content: str, import_line: str):
    """
    Asegura que exista una línea de import, si no está, la inserta.
    Preferiblemente después del primer bloque de imports.
    """
    # Ya existe
    if import_line in content:
        return content, False

    lines = content.splitlines(True)  # conserva \n

    # Insertar después de los imports iniciales
    insert_at = 0
    for i, line in enumerate(lines):
        # saltar shebang, encoding y líneas vacías
        if line.startswith("#!") or "coding" in line or line.strip() == "":
            continue

        # si es un import, seguimos avanzando
        if line.startswith("import ") or line.startswith("from "):
            insert_at = i + 1
            continue

        # primera línea que ya no es import => paramos
        break

    lines.insert(insert_at, import_line + "\n")
    return "".join(lines), True


##############
## Use by call
##############
def helper_add_import(full_path, relative_path, import_line):
    file_path = get_file_path(full_path, relative_path)
    content = read_file(file_path)

    updated, changed = ensure_import_in_content(content, import_line)
    if changed:
        write_file(file_path, updated)

    return changed





## ---------------------------------------
## ---- Append content at end of file
## ---------------------------------------

##############
## Use by call
##############
def helper_append_content(full_path, relative_path, content_to_append: str, add_newline=True, end_line=None):
    """
    Añade una línea/bloque al archivo SOLO si no existe ya.

    - end_line=None -> escribe al final del archivo
    - end_line=3 -> inserta en la línea 3 (línea 3 humana, 1-based)
    """
    file_path = get_file_path(full_path, relative_path)

    # Si el archivo no existe, lo creamos
    if not os.path.exists(file_path):
        write_file(file_path, content_to_append + ("\n" if add_newline else ""))
        return True

    content = read_file(file_path)

    # Si ya existe, no hacer nada
    if content_to_append.strip() in content:
        return False

    # Caso 1: si end_line es None -> al final
    if end_line is None:
        final_content = content

        # Asegurar salto de línea antes
        if add_newline and final_content and not final_content.endswith("\n"):
            final_content += "\n"

        final_content += content_to_append

        # Asegurar salto de línea después
        if add_newline and not final_content.endswith("\n"):
            final_content += "\n"

        write_file(file_path, final_content)
        return True

    # Caso 2: insertar en una línea específica
    lines = content.splitlines(True)  # mantiene \n

    # end_line es 1-based -> convertir a índice 0-based
    insert_index = max(0, int(end_line) - 1)

    # Si la línea es mayor que el archivo, insertamos al final
    if insert_index > len(lines):
        insert_index = len(lines)

    text_to_insert = content_to_append

    if add_newline and not text_to_insert.endswith("\n"):
        text_to_insert += "\n"

    lines.insert(insert_index, text_to_insert)

    write_file(file_path, "".join(lines))
    return True





## ---------------------------------------
## ---- Append content at end of file
## ---------------------------------------

def helper_update_list(full_path, relative_path, var_name: str, item_line: str):
    """
    Agrega un elemento dentro de un bloque tipo lista:
        VAR_NAME = [
            ...
        ]

    - var_name: Ej. "INSTALLED_APPS"
    - item_line: Ej. "'rest_framework',"  (puede venir sin coma, se la pone)
    - Solo lo añade si NO existe ya.
    """
    file_path = get_file_path(full_path, relative_path)
    content = read_file(file_path)

    found = find_python_assignment_block(content, var_name)
    if not found:
        return False

    start, end, block_text = found

    # ✅ Validar que el bloque sea una LISTA
    eq = block_text.find("=")
    if eq == -1:
        return False

    # Buscar el primer delimitador tras '='
    i = eq + 1
    while i < len(block_text) and block_text[i] not in "{[(":
        i += 1
    if i >= len(block_text) or block_text[i] != "[":
        # No es una lista
        return False

    # ✅ Normalizar comparaciones: ' y "
    normalized_block = block_text.replace('"', "'")

    # item para comparar SIN coma final
    normalized_item_check = item_line.replace('"', "'").strip()
    if normalized_item_check.endswith(","):
        normalized_item_check = normalized_item_check[:-1].strip()

    # Si ya existe, no añadir
    if normalized_item_check in normalized_block:
        return False

    # Buscar el cierre de la lista
    close_idx = block_text.rfind("]")
    if close_idx == -1:
        return False

    # Detectar indentación del contenido interno
    lines = block_text.splitlines(True)
    indent = "    "  # default
    for ln in lines[1:]:
        stripped = ln.strip()
        if stripped and stripped not in ["]", "],"]:
            indent = ln[:len(ln) - len(ln.lstrip())]
            break

    # Asegurar coma final
    new_line = item_line.strip()
    if not new_line.endswith(","):
        new_line += ","

    # Insertar antes del cierre
    before = block_text[:close_idx].rstrip()
    after = block_text[close_idx:]  # incluye el ]

    if not before.endswith("\n"):
        before += "\n"

    updated_block = before + f"{indent}{new_line}\n" + after.lstrip("\n")

    # Guardar reemplazo
    updated_content = content[:start] + updated_block + content[end:]
    write_file(file_path, updated_content)

    return True





## ---------------------------------------
## ---- Update line
## ---------------------------------------
def helper_update_line(full_path, relative_path, old_line: str, new_line: str):
    """
    Busca una línea exacta dentro del archivo y la reemplaza por otra (puede ser bloque).
    
    - old_line: texto exacto a buscar (sin \n)
    - new_line: reemplazo (puede tener \n)
    """
    file_path = get_file_path(full_path, relative_path)

    if not os.path.exists(file_path):
        return False

    content = read_file(file_path)
    lines = content.splitlines(True)  # mantiene \n

    replaced = False

    for i, line in enumerate(lines):
        # comparo sin salto de línea
        if line.rstrip("\n") == old_line:
            # new_line puede ser multilinea
            replacement = new_line
            if not replacement.endswith("\n"):
                replacement += "\n"

            lines[i] = replacement
            replaced = True
            break

    if replaced:
        write_file(file_path, "".join(lines))

    return replaced
