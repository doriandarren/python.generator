import os
from helpers.helper_print import create_folder





def generate_folder_api(full_path):
    create_api_file(full_path)


def create_api_file(project_path):
    """
    Genera el archivo.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "api")
    file_path = os.path.join(pages_dir, "api.js")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    content = """//const API_URL = import.meta.env.VITE_API_URL;
const API_URL = 'https://api.splytin.com/api/v1/';

export const api = async (endpoint, method = "GET", body = null, token = null) => {
  const headers = {
    "Content-Type": "application/json",
  };

  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  try {
    const response = await fetch(`${API_URL}${endpoint}`, {
      method,
      headers,
      body: body ? JSON.stringify(body) : null,
    });

    // if (!response.ok) {
    //   throw new Error(`Error ${response.status}: ${response.statusText}`);
    // }

    return await response.json();
  } catch (error) {
    console.error("Error en la petición:", error);
    throw error;
  }
};
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")



