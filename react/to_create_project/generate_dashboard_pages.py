import os

def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta creada: {path}")



def generate_dashboard_pages(project_path):
    generate_routes(project_path)
    generate_dashboard_index_page(project_path)



def generate_routes(project_path):
    """
    Genera el archivo AppRoutes.jsx dentro de la carpeta modules/routes.
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", "dashboard", "routes")
    file_path = os.path.join(routes_dir, "DashboardRoutes.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo jsx
    app_routes_content = """import { Navigate, Route, Routes } from "react-router";
import { DashboardPage } from "../pages/DashboardPage";

export const DashboardRoutes = () => {
  return (
    <Routes>
      
      <Route path="/" element={ <DashboardPage /> } />

      <Route path="/*" element={ <Navigate to="/" /> } />
      
    </Routes>
  )
}

"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(app_routes_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")




def generate_dashboard_index_page(project_path):
    """
    Genera el archivo jsx dentro de la carpeta modules/dashboard/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "dashboard", "pages")
    file_path = os.path.join(pages_dir, "DashboardPage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    home_page_content = """export const DashboardPage = () => {
  return (
    <div>DashboardPage</div>
  )
}
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(home_page_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")


