import os
from helpers.helper_print import print_message, GREEN, CYAN




def generate_module_auth(full_path):
    create_controller(full_path)





def create_controller(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "controllers", "auth")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "authLoginController.php")

    # Contenido por defecto
    content = r"""import { response } from "express";
import bcrypt from 'bcryptjs';
import User from "../../models/User.js";
import { generateJWT } from "../../helpers/jwt/generate-jwt.js";


export const authLoginController = async(req, res = response) => {
    
    const { email, password } = req.body; 

    try {

        const user = await User.findOne({ where: { email } });

        if(!user){
            return res.status(400).json({
                message: 'Usuario / Password no son correctos - email'
            });
        }

        const validPassword = await bcrypt.compare(password, user.password);

        if( !validPassword ){
            return res.status(400).json({
                message: 'Usuario / Password no son correctos - password'
            });
        }

        const token = await generateJWT(user.id);


        res.json({
            token,
            user,
        })
        
    } catch (error) {
        res.status(500).json({
            message: 'Error. Contacte con el Administador'
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





