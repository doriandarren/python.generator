import xml.etree.ElementTree as ET
from helpers.helper_print import capitalize_camel_case
from helpers.helper_string import convert_word



def list_diagrams(xml_path, excluded_columns):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    tables = {}

    for cell in root.iter('mxCell'):
        style = cell.attrib.get('style', '')
        if 'swimlane' in style:
            table_id = cell.attrib['id']
            table_name = cell.attrib.get('value', 'unknown_table')
            tables[table_id] = {
                'name': table_name,
                'columns': []
            }

    for cell in root.iter('mxCell'):
        parent_id = cell.attrib.get('parent')
        value = cell.attrib.get('value')
        if parent_id in tables and value:
            if 'swimlane' not in cell.attrib.get('style', '') and value not in excluded_columns:
                tables[parent_id]['columns'].append(value)

    for table in tables.values():
        # print(f"📦 Tabla: {table['name']}")
        # for column in table['columns']:
        #     print(f"  - 🧩 {column}")
        # print()



        # plural_name = capitalize_camel_case(table['name']) # e.g., InvoiceLines
        # singular_name = convert_word(plural_name)  # e.g., invoice_line
        # singular_name = capitalize_camel_case(singular_name['singular']) # e.g., InvoiceLine


        # Format custom:
        print(f"require base_path('routes/API/{ table['name'] }.php'); ")
        print()
