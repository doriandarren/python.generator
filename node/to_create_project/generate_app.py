import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_app(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path,)

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "app.js")

    # Contenido por defecto
    content = r"""//import 'dotenv/config';
import { Server } from './src/server/server.js';
import dotenv from 'dotenv';
import './src/models/initAssociations.js';


dotenv.config();

const server = new Server();

server.listen();
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
