import os
from helpers.helper_print import print_message, GREEN, CYAN




def generate_middleware(full_path):
    create_attach_base_controller(full_path)
    create_validate_fields(full_path)
    create_validate_roles(full_path)




def create_attach_base_controller(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "middleware")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "attachBaseController.js")

    # Contenido por defecto
    content = r"""import { BaseController } from "../helpers/controllers/baseController.js";

export const attachBaseController = (req, res, next) => {
    res.handler = new BaseController(res);
    next();
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)




def create_validate_fields(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "middleware")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "validateFields.js")

    # Contenido por defecto
    content = r"""import { validationResult } from "express-validator";

export const validateFields = ( req, res, next ) => {
    const errors = validationResult(req);
    if(!errors.isEmpty()){
        return res.status(400).json(errors);
    }

    next();
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)



def create_validate_roles(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "middleware")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "validateRoles.js")

    # Contenido por defecto
    content = r"""import { response } from "express";


export const isAdminRole = (req, res = response, next ) => {
    

    if ( !req.user ){
        return res.status(500).json({
            msg: 'Se requie verificar el role sin validar el token primero'
        });
    }

    const { role, name } = req.user;

    if( role !== 'ADMIN_ROLE'){
        return res.status(401).json({
            msg: `${ name } no es admintrador - No se puede procesar`
        });
    }


    next();

}



export const hasRole = ( ...roles ) => {

    return (req, res = response, next) => {

        if ( !req.user ){
            return res.status(500).json({
                msg: 'Se requie verificar el role sin validar el token primero'
            });
        }
        

        if ( !roles.includes( req.user.role ) ){
            return res.status(401).json({
                msg: `El servicio require uno de estos roles ${ roles }`
            });
        }
        
        next();
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
