import os
from .utils import print_message, GREEN, CYAN, run_command



def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta creada: {path}")


def generate_react_router(project_path):
    setup_react_router(project_path)
    setup_app_jsx(project_path)
    update_main_jsx(project_path)
    generate_app_router(project_path)





def setup_react_router(full_path):
    """Instala React Router."""
    print_message("Instalando React Router...", CYAN)
    run_command("npm install react-router", cwd=full_path)
    print_message("React Router instalado correctamente.", GREEN)





def setup_app_jsx(full_path):
    """Reemplaza el contenido de src/App.jsx."""
    app_jsx_content = """import { AppRouter } from './router/AppRouter';

export const App = () => {
  return (
    <>
        <AppRouter />
    </>
  );
}
"""
    with open(os.path.join(full_path, "src", "App.jsx"), "w") as f:
        f.write(app_jsx_content)
    print_message("App.jsx configurado correctamente.", GREEN)





def update_main_jsx(full_path):
    """
    Actualiza el archivo src/main.jsx
    """
    main_jsx_path = os.path.join(full_path, "src", "main.jsx")

    # Verificar si el archivo existe
    if not os.path.exists(main_jsx_path):
        print_message(f"Error: {main_jsx_path} no existe.", CYAN)
        return

    try:

        # Leer el contenido del archivo
        with open(main_jsx_path, "r") as f:
            content = f.read()


        # Reemplazos
        content = content.replace(
            "import App from './App.jsx'",
            "import { App } from \'./App.jsx\';\nimport { BrowserRouter } from \'react-router\';\nimport { Provider } from \'react-redux\';\nimport { store } from \'./store\';\nimport 'animate.css';"
        )


        # Reemplazos
        content = content.replace(
            "<App />",
            """<Provider store={store}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>"""
        )


        ## "createRoot(document.getElementById('root')).render(\n  <BrowserRouter>\n    <StrictMode>\n      <App />\n    </StrictMode>\n  </BrowserRouter>\n)"

        # Escribir el contenido actualizado
        with open(main_jsx_path, "w") as f:
            f.write(content)

        print_message("main.jsx configurado correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {main_jsx_path}: {e}", CYAN)




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
    app_routes_content = """import { Route, Routes } from "react-router";
import { AuthRoutes } from "../modules/auth/routes/AuthRoutes";
import { DashboardRoutes } from "../modules/dashboard/routes/DashboardRoutes";
import { PublicRoutes } from "../modules/public/routes/PublicRoutes";


export const AppRouter = () => {
  return (
    <Routes>
    
      {/* Routes Public */}
      <Route path="/*" element={ <PublicRoutes /> } />
      
      {/* Login y Register */}
      <Route path="auth/*" element={ <AuthRoutes /> } />


      {/* Routes Private */}
      <Route path="/admin/*" element={ <DashboardRoutes /> } />
      
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

