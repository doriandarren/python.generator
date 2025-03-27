import xml.etree.ElementTree as ET
from helpers.helper_print import capitalize_camel_case, input_with_validation
from helpers.helper_string import convert_word
from php.to_api.generator import generate
from react.to_create_module.generate_module_standard import generate_module_standard


def generate_tables_columns(xml_path, excluded_columns):


    php_full_path = input_with_validation("Proyecto [PHP - /Users/dorian/PhpstormProjects81/app-1/ ]","/Users/dorian/PhpstormProjects81/app-1/")
    php_namespace = input_with_validation("Namespace (ERP / API / INVOICES) ", "API")

    react_full_path = input_with_validation("Proyecto [React - /Users/dorian/ReactProjects/app-1/ ]","/Users/dorian/ReactProjects/app-1/")




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
        print(f"📦 Tabla: {table['name']}")
        for column in table['columns']:
            print(f"  - 🧩 {column}")
        print()

        plural_name = capitalize_camel_case(table['name'])         # e.g., InvoiceLines

        singular_name = convert_word(plural_name)  # e.g., invoice_lines

        singular_name = capitalize_camel_case(singular_name['singular'])  # e.g., InvoiceLine

        columns = [{"name": column} for column in table['columns']]

        ## Generate PHP
        generate(php_namespace, php_full_path, singular_name, plural_name, columns)

        ## Generate React
        generate_module_standard(react_full_path, singular_name, plural_name, columns)

