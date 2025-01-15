import os
from .utils import print_message, GREEN, CYAN


def generate_styles(full_path, file_name="globals.css", content=None):
    """
    Genera un archivo CSS en la carpeta src/styles.

    Args:
        full_path (str): Ruta completa del proyecto.
        file_name (str): Nombre del archivo a generar (por defecto, 'globals.css').
        content (str): Contenido inicial del archivo CSS (opcional).
    """
    styles_path = os.path.join(full_path, "src", "styles")

    # Crear la carpeta src/styles si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, file_name)

    # Contenido por defecto
    if content is None:
        content = """\
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

    body {
        @apply bg-gray-100 text-gray-800;
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

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
