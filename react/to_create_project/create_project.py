import os
import subprocess
from utils import print_message, GREEN, CYAN


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
    extend: {},
  },
  plugins: [],
}
"""
    with open(os.path.join(full_path, "tailwind.config.js"), "w") as f:
        f.write(tailwind_config)
    print_message("Tailwind CSS configurado correctamente.", GREEN)


def setup_index_css(full_path):
    """Reemplaza el contenido del archivo src/index.css."""
    index_css_content = """\
@tailwind base;
@tailwind components;
@tailwind utilities;
"""
    with open(os.path.join(full_path, "src", "index.css"), "w") as f:
        f.write(index_css_content)
    print_message("index.css configurado correctamente.", GREEN)


def setup_app_jsx(full_path):
    """Reemplaza el contenido de src/App.jsx."""
    app_jsx_content = """\
export const App = () => {
  return (
    <>
      <div className="bg-blue-500 text-white text-center p-4">
        <h1 className="text-4xl font-bold">Hello, Tailwind CSS!</h1>
      </div>
    </>
  )
}
"""
    with open(os.path.join(full_path, "src", "App.jsx"), "w") as f:
        f.write(app_jsx_content)
    print_message("App.jsx configurado correctamente.", GREEN)


def update_main_jsx(full_path):
    """Actualiza la línea de importación en src/main.jsx."""
    main_jsx_path = os.path.join(full_path, "src", "main.jsx")
    with open(main_jsx_path, "r") as f:
        content = f.read()
    content = content.replace("import App from './App.jsx'", "import {App} from './App.jsx'")
    with open(main_jsx_path, "w") as f:
        f.write(content)
    print_message("main.jsx configurado correctamente.", GREEN)


def delete_app_css(full_path):
    """Elimina src/App.css si existe."""
    app_css_path = os.path.join(full_path, "src", "App.css")
    if os.path.exists(app_css_path):
        os.remove(app_css_path)
        print_message("src/App.css eliminado correctamente.", GREEN)
    else:
        print_message("src/App.css no existe, no es necesario eliminarlo.", CYAN)
