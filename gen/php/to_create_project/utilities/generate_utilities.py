from gen.php.to_create_project.utilities.excel.generate_excel import generate_excel
from gen.php.to_create_project.utilities.helpers.generate_helpers import generate_helpers
from gen.php.to_create_project.utilities.messages.generate_messages import generate_messages


def generate_utilities(full_path):
    generate_excel(full_path)
    generate_helpers(full_path)
    generate_messages(full_path)



