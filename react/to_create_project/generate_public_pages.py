import os

def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta creada: {path}")



def generate_pages(project_path):
    generate_home_page(project_path)



def generate_home_page(project_path):
    """
    Genera el archivo HomePage.jsx dentro de la carpeta modules/public/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "public", "pages")
    file_path = os.path.join(pages_dir, "HomePage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido del archivo HomePage.jsx
    home_page_content = """export const HomePage = () => {
    return (
        <>
            <div className=\"bg-blue-500 text-white text-center p-4 rounded-3xl\">
                <h1 className=\"text-slate-950 text-4xl font-bold\">Hello World!</h1>
            </div>
        </>
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