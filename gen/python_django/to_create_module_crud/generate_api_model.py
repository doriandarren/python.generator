import os
from gen.python_django.helpers.helper_file import helper_append_content
from helpers.helper_print import print_message, GREEN, CYAN


def get_str_field(columns):
    priority_fields = ["title", "name", "description"]

    for field in priority_fields:
        for column in columns:
            if column["name"] == field:
                return f"self.{field}"

    return "self.id"


def map_column_type(column):
    column_type = column.get("type")

    if column.get("is_fk"):
        related_table = column.get("related_table", "")
        related_model = column.get("related_model", "")
        field_name = column["name"].replace("_id", "")
        return field_name, f'models.ForeignKey("{related_model}", on_delete=models.CASCADE)'

    if column_type == "string":
        return column["name"], "models.CharField(max_length=255)"
    elif column_type == "integer":
        return column["name"], "models.IntegerField()"
    elif column_type == "text":
        return column["name"], "models.TextField()"
    elif column_type == "boolean":
        return column["name"], "models.BooleanField(default=False)"
    elif column_type == "float":
        return column["name"], "models.FloatField()"
    elif column_type == "date":
        return column["name"], "models.DateField()"
    elif column_type == "datetime":
        return column["name"], "models.DateTimeField()"

    return column["name"], "models.CharField(max_length=255)"



def generate_api_model(
        full_path,
        project_name,
        singular_name,
        plural_name,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        singular_first_camel,
        plural_first_camel,
        columns,
    ):
    """
    Genera el archivo
    """
    
    fields = []
    
    for column in columns:
        field_name, field_definition = map_column_type(column)
        fields.append(f"    {field_name} = {field_definition}")
    
    fields_str = "\n".join(fields)
    
    return_str_field = get_str_field(columns)
    
    
    print_message(f"Creating model {singular_name}", GREEN)
    
    

    str = f"""class {singular_name}(models.Model):
{fields_str if fields else "    pass"}

    class Meta:
        verbose_name = "{singular_name}"
        verbose_name_plural = "{plural_name}"

    def __str__(self):
        return str({return_str_field})
    """
    
    helper_append_content(
        full_path, 
        f"apps/{plural_name_snake}/models.py", 
        str
    )
