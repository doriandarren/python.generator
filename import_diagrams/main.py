from helpers.helper_print import print_header, input_with_validation
from import_diagrams.to_generate.generate_tables_columns import generate_tables_columns
from import_diagrams.to_list.list_diagrams import list_diagrams

EXCLUDED_COLUMNS = {"id", "created_at", "updated_at", "deleted_at"}




if __name__ == '__main__':

    print_header("IMPORT DIAGRAMS")


    generator_type = input_with_validation("[1]Listar - [2]Generar: ")

    if generator_type.lower() == '1':
        list_diagrams("Truckwash.drawio.xml", EXCLUDED_COLUMNS)
    elif generator_type.lower() == '2':
        generate_tables_columns("Truckwash.drawio.xml", EXCLUDED_COLUMNS)


    print("✅ Bye...")


## /Users/dorian/PhpstormProjects81/docker-laravel-84/projects/api.truckwashvilamalla.eu/

## /Users/dorian/ReactProjects/office.truckwashvilamalla.eu/

## dorian.gonzalez@globaltank.eu