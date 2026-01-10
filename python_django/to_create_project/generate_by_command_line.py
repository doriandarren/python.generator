import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command



def generate_by_command_line(full_path, project_name):
    create_folder(full_path)
    
    

def create_folder(full_path):
    project_path = os.path.join(full_path)
    os.makedirs(project_path, exist_ok=True)






