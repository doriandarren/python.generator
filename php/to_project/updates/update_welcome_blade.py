import os
from helpers.helper_print import print_message, GREEN, CYAN



def update_welcome_blade(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "resources", "views")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "welcome.blade.php")

    # Contenido por defecto
    content = r"""<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>{{ env('APP_NAME') }}</title>

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
                src="{{ asset('brand/images/company_logos/logo.svg') }}"
                alt="logo"
                class="max-w-[70%] w-full h-auto mx-auto"
            />
        </div>
        <footer class="w-full text-md text-left text-black px-8 mb-5 animate__animated animate__slideInLeft">
            ©<span id="year"></span> GlobalFleet.es - Developed by <strong>GlobalDevelopers</strong>.
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

