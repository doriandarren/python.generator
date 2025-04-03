import os
from helpers.helper_print import create_folder




def create_routes(project_path, singular_name, plural_name_snake):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", plural_name_snake, "routes")
    file_path = os.path.join(routes_dir, f"{singular_name}Routes.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo jsx
    content = f"""import {{ Route, Routes }} from "react-router";
import {{ {singular_name}Page, {singular_name}CreatePage, {singular_name}EditPage }} from "../pages";

export const {singular_name}Routes = () => {{
  return (
    <Routes>

      <Route path="/" element={{<{singular_name}Page />}} />
      <Route path="create" element={{<{singular_name}CreatePage />}} />
      <Route path="edit/:id" element={{<{singular_name}EditPage />}} />

    </Routes>
  )
}}
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")
