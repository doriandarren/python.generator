import re
import html
import xml.etree.ElementTree as ET

from import_diagrams.helpers.helper_table_naming import table_to_classes

_TAG_RE = re.compile(r"<[^>]+>")

def _clean_value(v: str) -> str:
    if not v:
        return ""

    # decode html entities (&nbsp;, &amp;...)
    v = html.unescape(v)

    # remove html tags
    v = _TAG_RE.sub("", v)

    # normalize spaces/newlines
    v = v.replace("\xa0", " ").replace("\n", " ").strip()

    # collapse multiple spaces
    v = re.sub(r"\s+", " ", v)

    return v


def list_diagrams(xml_path, excluded_columns, selected_filename=None):
    if selected_filename:
        print(f"✔ 📂 Selecciona un archivo para importar: {selected_filename}")

    tree = ET.parse(xml_path)
    root = tree.getroot()

    excluded = {c.lower() for c in excluded_columns}
    tables = {}

    # 1) Tablas (swimlane)
    for cell in root.iter("mxCell"):
        style = cell.attrib.get("style", "")
        if "swimlane" in style:
            table_id = cell.attrib.get("id")
            table_name = _clean_value(cell.attrib.get("value", "unknown_table"))
            if table_id:
                tables[table_id] = {"name": table_name, "columns": []}

    # 2) Columnas
    for cell in root.iter("mxCell"):
        parent_id = cell.attrib.get("parent")
        value = _clean_value(cell.attrib.get("value"))

        if not value or parent_id not in tables:
            continue

        style = cell.attrib.get("style", "")
        if "swimlane" in style:
            continue

        if value.lower() in excluded:
            continue

        tables[parent_id]["columns"].append(value)

    # 3) Output con tu formato
    for table in tables.values():
        table_name = table["name"]
        singular_class, plural_class = table_to_classes(table_name)

        print(f"📄 Table: {table_name} - {singular_class} - {plural_class}")
        cols = table["columns"]
        print("Columns:", " ".join(cols) if cols else "(none)")
        print()
