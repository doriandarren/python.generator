import os

def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta creada: {path}")


def generate_file_routes(project_path):
    generate_module_public_routes(project_path)




def generate_module_public_routes(project_path):
    """
    Genera el archivo AppRoutes.jsx dentro de la carpeta modules/routes.
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", "auth", "routes")
    file_path = os.path.join(routes_dir, "AppRoutes.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo AppRoutes.jsx
    app_routes_content = """import { Navigate, Route, Routes } from \"react-router-dom\";
import { HomePage } from \"../pages/HomePage\";
import { MainLayout } from \"../../layouts/MainLayout\";

export const App = () => {
  return (
    <>
      <h1>MainApp</h1>
      <hr />
      
      <Routes>
      
        <Route element={<MainLayout />}>
            <Route path=\"/\" element={<HomePage />} />
        </Route>

        {/* <Route path=\"/*\" element={ <LoginPage /> } /> */}
        <Route path=\"/*\" element={ <Navigate to=\"/login\" /> } />
        
      </Routes>
      
    </>
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




def generate_module_auth_routes(project_path):
    """
    Genera el archivo AppRoutes.jsx dentro de la carpeta modules/routes.
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", "auth", "routes")
    file_path = os.path.join(routes_dir, "AppRoutes.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo AppRoutes.jsx
    app_routes_content = """import { Routes, Route } from 'react-router-dom';
import MainLayout from '../../layouts/MainLayout';
import Home from '../../pages/Home';
import About from '../../pages/About';

const AppRoutes = () => {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Route>
    </Routes>
  );
};

export default AppRoutes;
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(app_routes_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")