import os
import shutil
from helpers.helper_print import print_message, GREEN, CYAN


def generate_public(full_path):
    generate_index(full_path)
    generate_logo_img(full_path)
    generate_logo_ico(full_path)







def generate_index(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "public")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "index.html")

    # Contenido por defecto
    content = r"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project - API</title>

    <link rel="icon" type="image/png" href="brand/images/company_logos/logo.ico" />

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.bunny.net">
    <link href="https://fonts.bunny.net/css?family=instrument-sans:400,500,600" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />

    <!-- Styles / Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>

</head>

<body class="bg-[#e6e6e6] min-h-screen flex flex-col justify-between">
    <div class="flex flex-1 items-center justify-center px-4 animate__animated animate__zoomIn">
        <img
            src="brand/images/company_logos/logo.png"
            alt="logo"
            class="max-w-[40%] w-full h-auto mx-auto"
        />
    </div>
    <footer class="w-full text-md text-left text-black px-8 mb-5 animate__animated animate__slideInLeft">
        ©<span id="year"></span> Project.es - Developed by <strong>SplytinDevelopers</strong>.
    </footer>
    <script>
        document.getElementById("year").textContent = new Date().getFullYear();
    </script>
</body>

</html>
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)




def generate_logo_img(full_path):
    """Copia una imagen al proyecto."""
    static_folder = os.path.join(full_path, 'public', 'images', 'company_logos')  # o 'assets', según prefieras

    # Crear la carpeta destino si no existe
    if not os.path.exists(static_folder):
        os.makedirs(static_folder)

    # Copiar la imagen
    shutil.copy(
        '/Users/dorian/PythonProjects/python.generator/node/resources/logo.png',
        static_folder
    )
    print_message(f"Imagen .IMG copiada a {static_folder}.", GREEN)



def generate_logo_ico(full_path):
    """Copia una imagen al proyecto."""
    static_folder = os.path.join(full_path, 'public', 'images', 'company_logos')  # o 'assets', según prefieras

    # Crear la carpeta destino si no existe
    if not os.path.exists(static_folder):
        os.makedirs(static_folder)

    # Copiar la imagen
    shutil.copy(
        '/Users/dorian/PythonProjects/python.generator/node/resources/logo.ico',
        static_folder
    )
    print_message(f"Imagen .ICO copiada a {static_folder}.", GREEN)