import os
import subprocess
from .utils import print_message, GREEN, CYAN



def run_command(command, cwd=None):
    """Ejecuta un comando en la terminal."""
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print_message(f"Error ejecutando el comando: {command}", CYAN)
        raise e


def create_project(full_path):
    """Crea el proyecto React con Vite."""
    print_message("Creando el proyecto React con Vite...", CYAN)
    project_dir = os.path.dirname(full_path)
    project_name = os.path.basename(full_path)

    # Verificar si el directorio base existe
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
        print_message(f"Directorio base {project_dir} creado.", GREEN)

    run_command(f"npm create vite@latest {project_name} -- --template react", cwd=project_dir)


def install_dependencies(full_path):
    """Instala las dependencias del proyecto."""
    print_message("Instalando dependencias...", CYAN)
    run_command("npm install", cwd=full_path)


def setup_react_router(full_path):
    """Instala React Router."""
    print_message("Instalando React Router...", CYAN)
    run_command("npm install react-router-dom", cwd=full_path)
    print_message("React Router instalado correctamente.", GREEN)


def setup_tailwind(full_path):
    """Instala y configura Tailwind CSS."""
    print_message("Instalando Tailwind CSS...", CYAN)
    run_command("npm install -D tailwindcss postcss autoprefixer", cwd=full_path)
    run_command("npx tailwindcss init -p", cwd=full_path)

    # Configurar tailwind.config.js
    tailwind_config = """\
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}", // Asegúrate de incluir las extensiones que uses
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Lato', 'sans-serif'], // Usar Lato como fuente sans
      },
      colors: {
        primary: '#4f9da6',
        'primary-dark': '#35757d',
        'primary-light': '#7dbdc8',
        secondary: '#78c800',
        'secondary-dark': '#569300',
        'secondary-light': '#a4e542',
        accent: '#ff8c42',
        'accent-dark': '#cc702f',
        'accent-light': '#ffa866',
        neutral: '#eaeaea',
        'neutral-dark': '#bfbfbf',
        'neutral-light': '#f7f7f7',
        navbar: '#222831',
        background: '#f8fafc',
        error: '#f44336',
        success: '#4caf50',
      },
    },
  },
  plugins: [],
}
"""
    with open(os.path.join(full_path, "tailwind.config.js"), "w") as f:
        f.write(tailwind_config)
    print_message("Tailwind CSS configurado correctamente.", GREEN)



def setup_app_jsx(full_path):
    """Reemplaza el contenido de src/App.jsx."""
    app_jsx_content = """import { AppRoutes } from './modules/public/routes/AppRoutes';

export const App = () => {
  return (
    <>
      <PublicRoutes />
    </>
  );
}
"""
    with open(os.path.join(full_path, "src", "App.jsx"), "w") as f:
        f.write(app_jsx_content)
    print_message("App.jsx configurado correctamente.", GREEN)


def update_main_jsx(full_path):
    """
    Actualiza el archivo src/main.jsx:
    1. Reemplaza la línea de importación de App.
    2. Envuelve el contenido de `<StrictMode>` con `<BrowserRouter>`.
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
            "import './index.css'",
            "import './styles/globals.css'"
        )

        # Reemplazos
        content = content.replace(
            "import App from './App.jsx'",
            "import {App} from './App.jsx'\nimport { BrowserRouter } from 'react-router-dom'"
        )



        # Actualizar el bloque de renderizado
        content = content.replace(
            """createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)""",
            "createRoot(document.getElementById('root')).render(\n  <BrowserRouter>\n    <StrictMode>\n      <App />\n    </StrictMode>\n  </BrowserRouter>\n)"
        )

        # Escribir el contenido actualizado
        with open(main_jsx_path, "w") as f:
            f.write(content)

        print_message("main.jsx configurado correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {main_jsx_path}: {e}", CYAN)





def delete_app_and_index_css(full_path):
    """
    Elimina los archivos src/App.css y src/index.css si existen.
    """
    files_to_delete = ["src/App.css", "src/index.css"]

    for file in files_to_delete:
        file_path = os.path.join(full_path, file)
        if os.path.exists(file_path):
            os.remove(file_path)
            print_message(f"{file} eliminado correctamente.", GREEN)
        else:
            print_message(f"{file} no existe, no es necesario eliminarlo.", CYAN)