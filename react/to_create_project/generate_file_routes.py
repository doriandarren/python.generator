import os

def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta creada: {path}")


def generate_file_routes(project_path):
    generate_app_route(project_path)
    generate_module_public_routes(project_path)


def generate_app_route(project_path):
    """
    Genera el archivo AppRouter.jsx
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "router")
    file_path = os.path.join(routes_dir, "AppRouter.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo AppRoutes.jsx
    app_routes_content = """import { PublicRoutes } from \"../modules/public/routes/PublicRoutes\";

export const AppRouter = () => {
  return (
    <>
        <PublicRoutes />
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


def generate_module_public_routes(project_path):
    """
    Genera el archivo AppRoutes.jsx dentro de la carpeta modules/routes.
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", "public", "routes")
    file_path = os.path.join(routes_dir, "PublicRoutes.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo AppRoutes.jsx
    app_routes_content = """import { Navigate, Route, Routes } from \"react-router-dom\";
import { HomePage } from \"../pages/HomePage\";
import { AboutPage } from \"../pages/AboutPage\";
import { ContactPage } from \"../pages/ContactPage\";
import { MainLayout } from \"../../../layouts/MainLayout\";

export const PublicRoutes = () => {
  return (
    <>
    
      <Routes>
        
        <Route 
          path=\"/\" 
          element={
            <MainLayout>
              <HomePage />
            </MainLayout>
          } 
        />
        
         <Route 
          path="/about" 
          element={
            <MainLayout>
              <AboutPage />
            </MainLayout>
          } 
        />

        <Route 
          path="/contact" 
          element={
            <MainLayout>
              <ContactPage />
            </MainLayout>
          } 
        />

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