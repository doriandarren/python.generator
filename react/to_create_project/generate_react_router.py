import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command



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
    generate_private_route(project_path)
    generate_public_route(project_path)





def setup_react_router(full_path):
    """Instala React Router."""
    print_message("Instalando React Router...", CYAN)
    run_command("npm install react-router-dom", cwd=full_path)
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
            "import { App } from \'./App.jsx\';\nimport { BrowserRouter } from \'react-router-dom\';\nimport { Provider } from \'react-redux\';\nimport { store } from \'./store\';\nimport 'animate.css';"
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

    # Contenido del archivo
    content = r"""import { Navigate, Route, Routes } from "react-router-dom";
import { AuthRoutes } from "../modules/auth/routes/AuthRoutes";
import { DashboardRoutes } from "../modules/dashboard/routes/DashboardRoutes";
import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import { startRestoreSession } from "../store/auth/thunks";
import { PublicRoute } from "./PublicRoute";
import { PrivateRoute } from "./PrivateRoute";
import { PreloaderMain } from "../components/Preloader/PreloaderMain";
import { ProfileRoutes } from "../modules/profiles/routes/ProfileRoutes";
//******* Routes Fake **********
import { TeamRoutes } from "../modules/teams/routes/TeamRoutes";
import { SystemRoutes } from "../modules/systems/routes/SystemRoutes";
import { QuoteRoutes } from "../modules/quotes/routes/QuoteRoutes";

export const AppRouter = () => {
  const dispatch = useDispatch();
  const { status } = useSelector((state) => state.auth);
  const isAuthenticated = status === "authenticated";
  const [checkingAuth, setCheckingAuth] = useState(true);

  useEffect(() => {
    dispatch(startRestoreSession()).finally(() => {
      setCheckingAuth(false);
    });
  }, [dispatch]);

  if (checkingAuth) {
    return <PreloaderMain />;
  }

  return (
    <Routes>
      {/* Public Routes */}
      <Route path="/auth/*" element={<PublicRoute isAuthenticated={isAuthenticated} />}>
        <Route path="*" element={<AuthRoutes />} />
      </Route>

      {/* Private Routes */}
      <Route path="/admin/*" element={<PrivateRoute isAuthenticated={isAuthenticated} />}>
        <Route path="dashboard/*" element={<DashboardRoutes />} />
        <Route path="profiles/*" element={<ProfileRoutes />} />
        //******* Routes Fake **********
        <Route path="teams/*" element={<TeamRoutes />} />
        <Route path="systems/*" element={<SystemRoutes />} />
        <Route path="quotes/*" element={<QuoteRoutes />} />
      </Route>

      {/* Global Redirection */}
      <Route path="/" element={<Navigate to={isAuthenticated ? "/admin/dashboard" : "/auth/login"} />} />
    </Routes>
  );
};
"""

    
    
    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")


def generate_private_route(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "router")
    file_path = os.path.join(routes_dir, "PrivateRoute.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo
    content = r"""// router/PrivateRoute.jsx
import { Navigate, Outlet, useLocation } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { getAllowedPathsByRoles } from '../helpers/helperAllowedPaths.js';

export const PrivateRoute = ({ isAuthenticated }) => {
  // hooks SIEMPRE arriba
  const location = useLocation();
  const { roles } = useSelector((state) => state.auth);

  // 1) auth
  if (!isAuthenticated) {
    return <Navigate to="/auth/login" replace />;
  }

  // 2) autorización por rol
  const allowedPaths = getAllowedPathsByRoles(roles);

  // full access si allowed contiene "/admin"
  const hasFullAccess = allowedPaths.has("/admin");

  // ¿la ruta actual empieza por alguna base permitida?
  const isAllowed =
    hasFullAccess || [...allowedPaths].some(base => location.pathname.startsWith(base));

  if (!isAllowed) {
    // opcional: log rápido
    // console.warn('Bloqueado por rol', { path: location.pathname, allowed: [...allowedPaths] });
    return <Navigate to="/admin/dashboard" replace />;
  }

  return <Outlet />;
};
"""


    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")



def generate_public_route(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "router")
    file_path = os.path.join(routes_dir, "PublicRoute.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo
    content = """import { Navigate, Outlet } from 'react-router-dom';

export const PublicRoute = ({ isAuthenticated }) => {
  return !isAuthenticated ? <Outlet /> : <Navigate to="/admin/dashboard" />;
};
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")

