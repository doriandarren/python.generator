import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_server(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "server")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "server.js")

    # Contenido por defecto
    content = r"""import express from 'express';
import cors from 'cors';
import authRoutes from '../routes/authRoutes.js';
import userRoutes from '../routes/userRoutes.js';
import { attachBaseController } from '../middlewares/attachBaseController.js';


export class Server {
    
    constructor() {
        this.app = express();
        this.port = process.env.PORT;
        this.path = {
            auth: '/api/auth',
            users: '/api/users',
        }

        // Midlewares
        this.midlewares();

        // Rutas app
        this.routes();
    }


    midlewares(){

        // Directorio publico
        this.app.use( express.static('public') );

        //Cors
        this.app.use( cors() );

        // Lectura y parseo del body
        this.app.use( express.json() );

        // BaseController
        this.app.use( attachBaseController );

    }


    routes(){
        
        this.app.use( this.path.auth , authRoutes);

        this.app.use( this.path.users , userRoutes);

        //TODO Others routes
        
    }


    listen(){
        this.app.listen( this.port, ()=> {
            console.log(`Servidor ejecutandose en el puerto: ${ this.port }`);
        });
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

