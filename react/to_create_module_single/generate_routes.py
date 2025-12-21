import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_routes(full_path, singular_name, plural_name_snake):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "src", "modules", plural_name_snake, "routes")
    file_path = os.path.join(folder_path, f"{singular_name}Routes.jsx")
    
    os.makedirs(folder_path, exist_ok=True)

    content = f'''import {{ Route, Routes }} from "react-router";
import {{ {singular_name}Page, {singular_name}CreatePage, {singular_name}EditPage }} from "../pages";

export const {singular_name}Routes = () => {{
  return (
    <Routes>

      <Route path="/" element={{<{singular_name}Page />}} />

    </Routes>
  )
}}
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        



