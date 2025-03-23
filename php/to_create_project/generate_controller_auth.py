import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_controller_auth(full_path):
    create_auth_login(full_path)
    create_auth_logout(full_path)
    create_auth_register(full_path)
    create_auth_user(full_path)



def create_auth_login(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "Auth")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AuthLoginController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\API\\Auth;

use App\\Enums\\Roles\\EnumRole;
use App\\Http\\Controllers\\Controller;
use App\\Utilities\\Messages\\MessageChannel;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Support\\Facades\\Validator;


class AuthLoginController extends Controller
{
    /**
     *
     * @bodyParam email string required Must be a valid email address. Example: satterfield.buddy@example.org
     * @bodyParam password string required
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function __invoke(Request $request): JsonResponse
    {

        $validator = Validator::make($request->all(), [
            'email' => 'required|string|email',
            'password' => 'required|string',
        ]);

        if($validator->fails()){
            return $this->respondWithError('Error', $validator->errors());
        }
        

        //Response 200 but with error
        $credentials = request(['email','password']);
        if(!Auth::attempt($credentials))
        {
            return $this->respondHttpUnauthorized();
        }


        $user = Auth::user();
        // Delete Tokens
        //$user->tokens()->delete();


        if(count($user->roles) == 0){
            MessageChannel::send('Error Authentication ERP - User Id: (' . $user->id .') Usuario: ' . $user->name, 'Error Auth');
            return $this->respondWithError('User without role', ['e' => 'User without role']);
        }


        // Validate user role
        if($user->roles[0]->name == EnumRole::ADMIN){

            $token = $user->createToken('auth_token')->plainTextToken;
            $userTemp = $user;
            //$userTemp->abilities = $user->abilities;

            return $this->respondWithToken('Login successfully - Admin', $token);

        }else{

            $arr = [];
            foreach ($user->abilities as $ability) {
                $arr[] = $ability->name;
            }
            $user->employee;
            $token = $user->createToken('auth_token', $arr)->plainTextToken;


            return $this->respondWithToken('Login successfully', $token);

        }

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



def create_auth_logout(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "Auth")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AuthLogoutController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\API\\Auth;

use App\\Http\\Controllers\\Controller;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;

class AuthLogoutController extends Controller
{
    /**
     * @param Request $request
     * @return JsonResponse
     */
    public function __invoke(Request $request): JsonResponse
    {

        $user = $request->user();
        $request->user()->tokens()->delete();

        return $this->respondWithData("Successfully logged out");

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



def create_auth_register(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "Auth")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AuthRegisterController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\API\\Auth;

use App\\Enums\\UserStatuses\\EnumUserStatus;
use App\\Http\\Controllers\\Controller;
use App\\Models\\User;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;

class AuthRegisterController extends Controller
{
    /**
     * @param Request $request
     * @return JsonResponse
     */
    public function __invoke(Request $request): JsonResponse
    {

        $request->validate([
            'name' => 'required|string',
            'email'=>'required|string|unique:users',
            'password'=>'required|string',
            'c_password' => 'required|same:password'
        ]);

        $user = new User([
            'name'  => $request->name,
            'email' => $request->email,
            'password' => bcrypt($request->password),
            'user_status_id' => EnumUserStatus::STATUS_ACTIVE_ID
        ]);


        if($user->save()){
            $tokenResult = $user->createToken('Personal Access Token');
            $token = $tokenResult->plainTextToken;
            return $this->respondWithToken('Successfully created user!', $token);
        }
        else{
            return $this->respondWithError('Provide proper details', 'Provide proper details');
        }

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




def create_auth_user(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "Auth")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AuthUserController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers\\API\\Auth;

use App\\Http\\Controllers\\Controller;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Http\\Request;
use stdClass;

class AuthUserController extends Controller
{
    /**
     * @param Request $request
     * @return JsonResponse
     */
    public function __invoke(Request $request): JsonResponse
    {
        $data = new stdClass();
        $data->user = $request->user();
        //$data->user->abilities = $request->user()->abilities;
        $data->user->roles = $request->user()->roles;

        if($this->isAdmin($request->user()->roles)){

            return $this->respondWithData("User current", $data->user);

        }else{

            return $this->respondWithData("User current", $data->user);
        }

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