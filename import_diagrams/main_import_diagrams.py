import os
from helpers.helper_menu import clear_screen, menu_list
from helpers.helper_print import print_header
from import_diagrams.to_generate.generate_tables_columns import generate_tables_columns
from import_diagrams.to_list.list_diagrams import list_diagrams
from import_diagrams.helpers.helper_assets_loader import list_xml_assets

EXCLUDED_COLUMNS = {"id", "created_at", "updated_at", "deleted_at"}

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(HERE, "assets")


def main_import_diagrams():
    clear_screen()
    print_header("IMPORT DIAGRAMS")

    opt = menu_list("¿Qué quieres hacer?", [
        {"name": "Listar", "value": "listar"},
        {"name": "Generar", "value": "generar"},
        {"name": "Volver", "value": "volver"},
    ])

    if opt in ("volver", None):
        return

    files = list_xml_assets(ASSETS_DIR)

    if not files:
        print("❌ No hay archivos .drawio.xml en assets/")
        return

    xml_path = menu_list("Selecciona el diagrama:", files)

    if not xml_path:
        return

    if opt == "listar":
        list_diagrams(xml_path, EXCLUDED_COLUMNS)

    elif opt == "generar":
        generate_tables_columns(xml_path, EXCLUDED_COLUMNS)
