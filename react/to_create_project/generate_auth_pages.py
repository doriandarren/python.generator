import os

def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta creada: {path}")



def generate_auth_pages(project_path):
    generate_routes(project_path)
    generate_login_page(project_path)
    generate_register_page(project_path)
    generate_auth_index_page(project_path)





def generate_routes(project_path):
    """
    Genera el archivo AppRoutes.jsx dentro de la carpeta modules/routes.
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", "auth", "routes")
    file_path = os.path.join(routes_dir, "AuthRoutes.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo jsx
    app_routes_content = """import { Navigate, Route, Routes } from "react-router";
import { LoginPage, RegisterPage } from "../pages";

export const AuthRoutes = () => {
  return (
    <Routes>
    
      <Route path="login" element={<LoginPage />} />
      <Route path="register" element={<RegisterPage />} />

      <Route path="/*" element={ <Navigate to="/auth/login" /> } />
    
    </Routes>
    
  );
};
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(app_routes_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")


def generate_login_page(project_path):
    """
    Genera el archivo HomePage.jsx dentro de la carpeta modules/public/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "auth", "pages")
    file_path = os.path.join(pages_dir, "LoginPage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido del archivo HomePage.jsx
    home_page_content = """export const LoginPage = () => {
  return (
    <div>LoginPage</div>
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

def generate_register_page(project_path):
    """
    Genera el archivo HomePage.jsx dentro de la carpeta modules/public/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "auth", "pages")
    file_path = os.path.join(pages_dir, "RegisterPage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido del archivo RegisterPage.jsx
    home_page_content = """export const RegisterPage = () => {
  return (
    <div>RegisterPage</div>
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

def generate_auth_index_page(project_path):
    """
    Genera el archivo HomePage.jsx dentro de la carpeta modules/public/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "auth", "pages")
    file_path = os.path.join(pages_dir, "index.js")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    home_page_content = """export * from \'./LoginPage\';
export * from \'./RegisterPage\';
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(home_page_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")