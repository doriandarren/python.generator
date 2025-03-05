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


const initialState = {
    status: 'checking', // 'checking', 'not-authenticated', 'authenticated' 
    token: null,
    email: null,
    displayName: null,
    photoURL: null,
    errorMessage: null,
}



export const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        login: (state, {payload}) => {
            state.status = 'authenticated';
            state.token = payload.token;
            state.email = payload.email;
            state.displayName = payload.displayName;
            state.photoURL = payload.photoURL;
            state.errorMessage = null;

            // Guardar en `localStorage` para que persista
            localStorage.setItem("token_portuarios", payload.token);

        },
        logout: (state, payload) => {
            state.status = 'not-authenticated';
            state.token = null;
            state.email = null;
            state.displayName = null;
            state.photoURL = null;
            state.errorMessage = payload?.errorMessage;
            
            // Eliminar de `localStorage`
            localStorage.removeItem("token_portuarios");
        },
        setErrorMessage: (state, action) => {
            state.errorMessage = action.payload;
        },
        checkingCredentials: (state) => {
            state.status = 'checking';
        }
    }
});


// Action creators are generated for each case reducer function
export const { login, logout, checkingCredentials, setErrorMessage } = authSlice.actions;
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
    app_routes_content = """import { authApi } from "../../modules/auth/api/authApi";
import { checkingCredentials, login, logout, setErrorMessage } from "./authSlice";


export const checkingAuthentication = () => {
    return async( dispatch ) => {
        dispatch( checkingCredentials() );
    }
}


export const startLoginWithEmailPassword = ({ email, password }) => {
    
    return async( dispatch ) => {

        dispatch( checkingCredentials() );

        try {

            const { token, errors } = await authApi('auth/login', 'POST', {email, password});

            if (!token) {
                console.log(errors);
                dispatch( setErrorMessage(errors[0].e) );
                return;
            }

            const userResponse = await authApi('auth/user', 'GET', null, token);
            const { email: emailApi, name: nameApi } = userResponse.data;


            const user = {
                status: 'authenticated',
                token: token,
                email: emailApi,
                displayName: nameApi,
                photoURL: '',
                errorMessage: null,
            }

            dispatch(login(user));


        } catch (error) {
            console.log(error);
        }
        
    }

}



export const startLogout = () => {
    return async( dispatch ) => {
        dispatch( logout() );
    }
}



export const startRestoreSession = () => {
    return async(dispatch) => {
        
        dispatch(checkingCredentials());

        const token = localStorage.getItem("token_portuarios");

        if (!token) {
            dispatch(logout());
            return;
        }


        try {

            const userResponse = await authApi('auth/user', 'GET', null, token);


            const { email: emailApi, name: nameApi } = userResponse.data;


            const user = {
                status: 'authenticated',
                token: token,
                email: emailApi,
                displayName: nameApi,
                photoURL: '',
                errorMessage: null,
            }

            dispatch(login(user));

            //console.log(userResponse.data);



        } catch (error) {
            console.error("Error al restaurar sesión:", error);
            dispatch(logout());
        }



    }
}
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(app_routes_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")



