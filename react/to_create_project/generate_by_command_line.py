import os
from .utils import print_message, GREEN, CYAN, run_command



def generate_by_command_line(full_path):
    # Crear proyecto y configurar
    create_project(full_path)
    install_dependencies(full_path)
    setup_react_router(full_path)
    setup_classname(full_path)
    setup_headlessui(full_path)  ## Estilos UI
    setup_heroicons(full_path)  ## Icons
    setup_clsx(full_path)  ## utilidad para construir cadenas de clases condicionalmente
    setup_framer_motion(full_path)  ## utilidad para construir cadenas de clases condicionalmente
    setup_app_jsx(full_path)
    update_main_jsx(full_path)
    delete_app_and_index_css(full_path)




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
    run_command("npm install react-router", cwd=full_path)
    print_message("React Router instalado correctamente.", GREEN)



def setup_classname(full_path):
    """Instala ClassNames."""
    print_message("Instalando ClassNames...", CYAN)
    run_command("npm install classnames", cwd=full_path)
    print_message("ClassNames instalado correctamente.", GREEN)


def setup_headlessui(full_path):
    """Instala Headlessui."""
    print_message("Instalando Headlessui...", CYAN)
    run_command("npm install @headlessui/react", cwd=full_path)
    print_message("Headlessui instalado correctamente.", GREEN)


def setup_heroicons(full_path):
    """Instala Heroicons."""
    print_message("Instalando Heroicons...", CYAN)
    run_command("npm install @heroicons/react", cwd=full_path)
    print_message("Heroicons instalado correctamente.", GREEN)

def setup_clsx(full_path):
    """Instala Clsx."""
    print_message("Instalando Clsx...", CYAN)
    run_command("npm install clsx", cwd=full_path)
    print_message("Clsx instalado correctamente.", GREEN)


def setup_framer_motion(full_path):
    """Instala FramerMotion."""
    print_message("Instalando FramerMotion...", CYAN)
    run_command("npm install framer-motion", cwd=full_path)
    print_message("React FramerMotion instalado correctamente.", GREEN)


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
            "import { App } from \'./App.jsx\';\nimport { BrowserRouter } from \'react-router\';\nimport { Provider } from \'react-redux\';\nimport { store } from \'./store\';"
        )

        # Reemplazos
        ## "import './styles/globals.css';\nimport './styles/normalize.css';\nimport './styles/styles.css';" --> Para Tailwind
        ## "import './styles/normalize.css';\nimport './styles/style.css';"  ---> Para SASS
        content = content.replace(
            "import './index.css'",
            "import './styles/globals.css';\nimport './styles/normalize.css';\nimport './styles/styles.css';"
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