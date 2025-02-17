import os
from .utils import print_message, GREEN, CYAN, run_command



def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta creada: {path}")



def generate_redux(project_path):
    redux_install(project_path)
    create_file_storejs(project_path)
    create_barrel_file_storejs(project_path)

    create_file_auth_slice(project_path)
    create_barrel_file_slice(project_path)


    create_file_thunks_auth(project_path)



def redux_install(full_path):
    """Instala las dependencias del proyecto."""
    print_message("Instalando redux...", CYAN)
    run_command("npm install @reduxjs/toolkit react-redux", cwd=full_path)




def create_file_storejs(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "store")
    file_path = os.path.join(routes_dir, "store.js")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo
    app_routes_content = """import { configureStore } from "@reduxjs/toolkit";
import { authSlice } from "./auth";


export const store = configureStore({
    reducer: {
        auth: authSlice.reducer,
    },
}); 
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(app_routes_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")



def create_barrel_file_storejs(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "store")
    file_path = os.path.join(routes_dir, "index.js")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo
    app_routes_content = """export * from \'./store\';"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(app_routes_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")




def create_file_auth_slice(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "store", "auth")
    file_path = os.path.join(routes_dir, "authSlice.js")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo
    app_routes_content = """import { createSlice } from '@reduxjs/toolkit';

export const authSlice = createSlice({
    name: 'auth',
    initialState: {
        status: 'not-authenticated', // 'checking', 'not-authenticated', 'authenticated' 
        uid: null,
        email: null,
        displayName: null,
        photoURL: null,
        errorMessage: null,
    },
    reducers: {
        login: (state, action) => {

        },
        logout: (state, payload) => {

        },
        checkingCredentials: (state) => {

        }
    }
});


// Action creators are generated for each case reducer function
export const { login, logout, checkingCredentials } = authSlice.actions;
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(app_routes_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")



def create_barrel_file_slice(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "store", "auth")
    file_path = os.path.join(routes_dir, "index.js")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo
    app_routes_content = """export * from \'./authSlice\';
export * from \'./thunks\';"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(app_routes_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")




def create_file_thunks_auth(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "store", "auth")
    file_path = os.path.join(routes_dir, "thunks.js")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo
    app_routes_content = """
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(app_routes_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")



