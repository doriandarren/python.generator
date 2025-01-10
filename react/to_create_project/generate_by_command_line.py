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
        primary: '#0096b2', // cian
        'primary-dark': '#007a91', // cian oscuro
        'primary-light': '#00b4d6', // cian claro
        secondary: '#ff6347', // tomate
        'secondary-dark': '#cc4f3a', // tomate oscuro
        'secondary-light': '#ff7f6e', // tomate claro
        accent: '#ffc107', // ámbar
        'accent-dark': '#cc9a06', // ámbar oscuro
        'accent-light': '#ffca28', // ámbar claro
        neutral: '#f5f5f5', // gris claro
        'neutral-dark': '#e0e0e0', // gris
        'neutral-light': '#fafafa', // gris más claro
        navbar: '#111827', //Navbar
      },
    },
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
/*
|--------------------------------------------------------------------------
| Font
|--------------------------------------------------------------------------
|
*/ 
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap');


/*
|--------------------------------------------------------------------------
| Tailwind Directives
|--------------------------------------------------------------------------
|
| Import TailwindCSS directives and swipe out at build-time with all of
| the styles it generates based on your configured design system.
|
*/ 
@tailwind base;
@tailwind components;
@tailwind utilities;


/*
|--------------------------------------------------------------------------
| Tailwind Layer
|--------------------------------------------------------------------------
|
| Import layer components.
|
*/
@layer components {
    .btn{
        @apply py-2 px-4 font-semibold rounded-lg shadow-md;
    }
    
    .btn-primary {
        @apply py-2 px-4 pl-4 bg-primary text-white font-semibold rounded-lg shadow-sm hover:bg-primary-dark hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-primary focus:ring-opacity-75;
    }

    .btn-secondary {
        @apply py-2 px-4 pl-4 bg-secondary text-white font-semibold rounded-lg shadow-sm hover:bg-secondary-dark hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-secondary focus:ring-opacity-75;
    }

    .btn-danger {
        @apply py-2 px-4 pl-4 bg-red-500 text-white font-semibold rounded-lg shadow-sm hover:bg-red-700 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-red-400 focus:ring-opacity-75;
    }

    .form-control{
        @apply w-full h-10 px-3 text-base placeholder-gray-600 border rounded-lg focus:outline;
    }

    .text-danger{
        @apply text-red-600;
    }

    .border-danger{
        @apply  border border-red-500 rounded-lg;
    }

    .card{
        @apply border rounded-md shadow-sm p-5;
    }

    h1{
        @apply text-3xl text-primary mt-5;
    }

    h2{
        @apply text-2xl text-primary mt-5;
    }

    h3{
        @apply text-xl text-primary mt-5;
    }

    p{
        @apply text-justify mt-5;
    }
    
}
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


# def update_main_jsx(full_path):
#     """Actualiza la línea de importación en src/main.jsx."""
#     main_jsx_path = os.path.join(full_path, "src", "main.jsx")
#     with open(main_jsx_path, "r") as f:
#         content = f.read()
#     content = content.replace("import App from './App.jsx'", "import {App} from './App.jsx'")
#     with open(main_jsx_path, "w") as f:
#         f.write(content)
#     print_message("main.jsx configurado correctamente.", GREEN)


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




def delete_app_css(full_path):
    """Elimina src/App.css si existe."""
    app_css_path = os.path.join(full_path, "src", "App.css")
    if os.path.exists(app_css_path):
        os.remove(app_css_path)
        print_message("src/App.css eliminado correctamente.", GREEN)
    else:
        print_message("src/App.css no existe, no es necesario eliminarlo.", CYAN)
