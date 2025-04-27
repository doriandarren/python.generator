import os
from helpers.helper_print import print_message, GREEN, CYAN




def generate_helpers(full_path):
    create_controller(full_path)
    create_safe_json(full_path)
    create_jwt(full_path)
    create_repositories(full_path)


def create_controller(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "helpers", "controllers")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "baseController.js")

    # Contenido por defecto
    content = r"""import { safeJson } from "./safeJson.js";


export class BaseController {

  constructor(res) {
    this.res = res;
    this.statusCode = 200;
  }

  // Setter y getter del código HTTP
  setCode(code) {
    this.statusCode = code;
  }

  getCode() {
    return this.statusCode;
  }

  // Método base que devuelve el JSON con el código correcto
  respond(payload) {
    const safePayload = safeJson(payload);
    return this.res.status(this.getCode()).json(safePayload);
  }

  // 200 OK
  respondWithData(data = null, message = null, success = true) {
    this.setCode(200);
    return this.respond({
      data,
      message,
      errors: null,
      success,
      status_code: this.getCode(),
    });
  }

  // 422 o cualquier error
  respondWithError(message = "", errors = null, code = 422) {
    this.setCode(code);
    return this.respond({
      errors: errors ? [errors] : null,
      data: null,
      message,
      success: false,
      status_code: this.getCode(),
    });
  }

  // 400 Bad Request
  respondHttpBadRequest(message = "Bad Request") {
    this.setCode(400);
    return this.respondWithError({ e: message }, message, this.getCode());
  }

  // 401 Unauthorized
  respondHttpUnauthorized(message = "Unauthorized") {
    this.setCode(401);
    return this.respondWithError({ e: message }, message, this.getCode());
  }

  // 403 Forbidden
  respondHttpForbidden(message = "Forbidden") {
    this.setCode(403);
    return this.respondWithError({ e: message }, message, this.getCode());
  }

  // 404 Not Found
  respondHttpNotFound(message = "Resource Not Found") {
    this.setCode(404);
    return this.respondWithError({ e: message }, message, this.getCode());
  }

  // 409 Conflict
  respondHttpConflict(message = "Data Conflict") {
    this.setCode(409);
    return this.respondWithError({ e: message }, message, this.getCode());
  }

  // 422 Unprocessable Entity
  respondUnprocessableEntity(message = "Unprocessable Entity") {
    this.setCode(422);
    return this.respondWithError({ e: message }, message, this.getCode());
  }

  // 500 Internal Server Error
  respondHttpInternalError(message = "Internal Server Error") {
    this.setCode(500);
    return this.respondWithError({ e: message }, message, this.getCode());
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


def create_safe_json(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "helpers", "controllers")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "safeJson.js")

    # Contenido por defecto
    content = r"""// src/shared/safeJson.js

export function safeJson(data) {
  const seen = new WeakSet();

  return JSON.parse(
    JSON.stringify(data, (key, value) => {
      if (typeof value === "object" && value !== null) {
        if (seen.has(value)) return "[Circular]";
        seen.add(value);
      }
      return value;
    })
  );
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_jwt(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "helpers", "jwt")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "generateJWT.js")

    # Contenido por defecto
    content = r"""import jwt from 'jsonwebtoken';

export const generateJWT = (uid = '') => {
    
    return new Promise((resolve, reject) => {

        const payload = { uid };

        jwt.sign( payload, process.env.SECRETORPRIVATEKEY, {
            expiresIn: '4h'
        }, (err, token) => {
            if( err ){
                console.log( err );
                reject('No se pudo generar el token');
            }else{
                resolve( token );
            }    
        });

    })

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_repositories(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "helpers", "repositories")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "baseRepository.js")

    # Contenido por defecto
    content = r"""
export class BaseRepository {

    constructor(){
        this.LATEST = ['createdAt', 'DESC'];
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
