import os


def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta creada: {path}")



def generate_module_dashboard(project_path):
    generate_routes(project_path)
    generate_dashboard_page(project_path)
    generate_team_page(project_path)

    generate_api_file(project_path)




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
import { TeamPage } from "../pages/TeamPage";


export const DashboardRoutes = () => {
  return (
    <Routes>
      
      <Route path="/dashboard" element={ <DashboardPage /> } />
      <Route path="/team" element={ <TeamPage /> } />

      <Route path="/*" element={ <Navigate to="/auth/dashboard" /> } />
      
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


def generate_dashboard_page(project_path):
    """
    Genera el archivo jsx dentro de la carpeta modules/dashboard/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "dashboard", "pages")
    file_path = os.path.join(pages_dir, "DashboardPage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    home_page_content = """import { SessionLayout } from "../../../layouts/private/SessionLayout";

export const DashboardPage = () => {

  return (
    <SessionLayout>
      <h1>Dashboard</h1>
      <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sunt, similique, ea soluta voluptatibus reprehenderit suscipit doloremque id magni voluptatum esse atque sequi, illum at consectetur impedit maiores neque! Obcaecati, assumenda.</p>
    </SessionLayout>
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


def generate_team_page(project_path):
    """
    Genera el archivo jsx dentro de la carpeta modules/dashboard/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "dashboard", "pages")
    file_path = os.path.join(pages_dir, "TeamPage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    home_page_content = """import { SessionLayout } from "../../../layouts/private/SessionLayout";

export const TeamPage = () => {

  return (
    <SessionLayout>
      <h1>Team</h1>
      <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sunt, similique, ea soluta voluptatibus reprehenderit suscipit.</p>
    </SessionLayout>
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


def generate_api_file(project_path):
    """
    Genera el archivo.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "auth", "api")
    file_path = os.path.join(pages_dir, "dashboardApi.js")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    content = """const API_URL = import.meta.env.VITE_API_URL;

export const fetchData = async (endpoint, method = "GET", body = null, token = null) => {
  const headers = {
    "Content-Type": "application/json",
  };

  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  try {
    const response = await fetch(`${API_URL}${endpoint}`, {
      method,
      headers,
      body: body ? JSON.stringify(body) : null,
    });

    if (!response.ok) {
      throw new Error(`Error ${response.status}: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error("Error en la petición:", error);
    throw error;
  }
};
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")

