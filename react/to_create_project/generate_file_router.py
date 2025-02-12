import os

def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta creada: {path}")


def generate_file_router(project_path):
    generate_app_router(project_path)


def generate_app_router(project_path):
    """
    Genera el archivo AppRoute.jsx
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "router")
    file_path = os.path.join(routes_dir, "AppRouter.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo AppRoutes.jsx
    app_routes_content = """import { Navigate, Route, Routes } from "react-router";
import { HomePage } from "../modules/public/pages/HomePage";
import { RegisterPage, LoginPage } from "../modules/auth/pages";


export const AppRouter = () => {
  return (
    <Routes>

      {/* Login y Registro */}
      <Route path="/" element={ <HomePage />} />
      <Route path="auth/login" element={ <LoginPage />} />
      <Route path="auth/register" element={ <RegisterPage />} />


      {/* Routes private */}
      <Route path="/*" element={ <Navigate to="/auth/login" /> } />
      
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





