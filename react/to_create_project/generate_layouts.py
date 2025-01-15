import os
from .utils import print_message, GREEN, CYAN

def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print_message(f"Carpeta creada: {path}", GREEN)
    else:
        print_message(f"Carpeta ya existe: {path}", CYAN)

def generate_layouts(project_path):
    """
    Genera el archivo MainLayout.jsx dentro de la carpeta layouts.
    """
    print_message("Generando MainLayout.jsx...", CYAN)

    # Define la ruta del archivo
    layouts_dir = os.path.join(project_path, "src", "layouts")
    file_path = os.path.join(layouts_dir, "MainLayout.jsx")

    # Crear la carpeta layouts si no existe
    create_folder(layouts_dir)

    # Contenido del archivo MainLayout.jsx
    main_layout_content = """export const MainLayout = ({ children }) => {
  return (
    <div className="main-layout">
        <header>
            <h1>My Application</h1>
        </header>
        <main>
            {children}
        </main>
        <footer>
            <p>© 2025 My Application. All rights reserved.</p>
        </footer>
    </div>
  )
}
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(main_layout_content)
        print_message(f"Archivo creado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al crear el archivo {file_path}: {e}", CYAN)
