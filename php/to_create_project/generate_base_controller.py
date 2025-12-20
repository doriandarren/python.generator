import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command




def generate_base_controller(full_path):
    create_file_controller(full_path)
    create_file_base_controller(full_path)




def create_file_controller(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "Controller.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers;

use Illuminate\\Foundation\\Auth\\Access\\AuthorizesRequests;
use Illuminate\\Foundation\\Validation\\ValidatesRequests;

class Controller extends BaseController
{
    use AuthorizesRequests, ValidatesRequests;
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)







def create_file_base_controller(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "BaseController.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Http\\Controllers;

use App\\Enums\\Roles\\EnumRole;
use Illuminate\\Http\\JsonResponse;
use Illuminate\\Routing\\Controller as IluBaseController;



class BaseController extends IluBaseController
{

    private $message;
    private $code;
    

    public function getMessage()
    {
        return $this->message;
    }

    public function setMessage(string $message)
    {
        $this->message = $message;
    }

    public function getCode()
    {
        return $this->code;
    }

    public function setCode(int $code)
    {
        $this->code = $code;
    }

    /**
     * Respond Base
     * @param $data
     * @param array $headers
     * @return JsonResponse
     */
    public function respond($data, $headers = []){
        return response()->json($data, $this->getCode());
    }

    /**
     * Respond Base with ERROR
     * @param string $message
     * @param null $errors
     * @param int $code
     * @return JsonResponse
     */
    public function respondWithError(string $message='', $errors = null, $code = 422): JsonResponse
    {
        $this->setCode($code);
        return $this->respond([
            'message' => $message,
            'data' => null,
            'errors' => [ $errors ],
            'success' => FALSE,
            'status_code' => $this->getCode(),
        ]);
    }

    /*************************************
     *  RESPONSE 200
     *************************************/

    /**
     * Respond 200
     * @param null $message
     * @param null $data
     * @param bool $success
     * @return JsonResponse
     */
    public function respondWithData($message = null, $data = null, $success = true): JsonResponse
    {
        $this->setCode(200);
        return $this->respond([
            'data' => $data,
            'message' => $message,
            'success' => $success,
            'status_code' => 200
        ]);
    }


    /**
     * Respond with Token
     * @param $message
     * @param $token
     * @return JsonResponse
     */
    public function respondWithToken($message, $token): JsonResponse
    {
        $this->setCode(201);
        return $this->respond([
            'message' => $message,
            'token' => $token,
            'token_type' => 'Bearer',
            //'user' => $user,
            'success' => TRUE,
            'status_code' => 201
        ]);
    }


    /**
     * Respond with Token
     * @param $message
     * @param $user
     * @param $token
     * @return JsonResponse
     */
    public function respondWithTokenWithUser($message, $user, $token): JsonResponse
    {
        $this->setCode(201);
        return $this->respond([
            'message' => $message,
            'token' => $token,
            'token_type' => 'Bearer',
            'user' => $user,
            'success' => TRUE,
            'status_code' => 201
        ]);
    }


    /**
     * Respond with Token
     * @param $message
     * @param $user
     * @param $token
     * @return JsonResponse
     */
    public function respondWithTokenByApp($message, $user, $token): JsonResponse
    {
        $this->setCode(201);
        return $this->respond([
            'message' => $message,
            'token' => $token,
            'token_type' => 'Bearer',
            'user' => $user,
            'success' => TRUE,
            'status_code' => 201
        ]);
    }


    /*************************************
     *  RESPONSE 400
     *************************************/

    //The 400
    public function respondHttpBadRequest($message = 'Bad Request'){
        $this->setCode(400);
        return $this->respondWithError($message, ['e' => $message]);
    }

    // Response 401
    public function respondHttpUnauthorized($message = 'Unauthorized'){
        $this->setCode(401);
        return $this->respondWithError($message, ['e' => $message]);
    }

    // Response 409
    public function respondHttpConflict($message = 'Data Conflict'){
        $this->setCode(409);
        return $this->respondWithError($message, ['e' => $message]);
    }

    // Response 422
    public function respondUnprocessableEntity($message = 'Unprocessable Entity')
    {
        $this->setCode(422);
        return $this->respondWithError($message, ['e' => $message]);
    }


    /**
     * Response validate to FORM
     * Validation To Use:
     *
     * $validation =  Validator::make(
     * $request->all(),
     * [
     * 'name' => 'required',
     * 'email' => 'required',
     * ],
     * [
     * 'required' => [
     * 'error_code' => 'E001',
     * 'error_description' => 'Parameter :attribute is required'
     * ]
     * ]);
     *
     * if ($validation->fails()) {
     * return $this->respondWithValidation($validation->errors());
     * }
     *
     * @param $errors
     * @return JsonResponse
     */
    public function respondWithValidation($errors)
    {

        $errorCodes = [];
        $errorDescriptions = [];

        foreach(json_decode($errors) as $key => $error){
            if(count($errors) > 3){
                $errorCodes[] = $error[0]->error_code;
                $errorDescriptions[] = $error[0]->error_description;
            }else{
                $errorCodes = $error[0]->error_code;
                $errorDescriptions = $error[0]->error_description;
            }
        }

        $this->setCode(200);
        return $this->respond([
            'success' => false,
            'message' => '',
            'error_code' => $errorCodes,
            'error_description' => $errorDescriptions,
            'status_code' => 200,
        ]);
    }



    /**
     * Role Admin
     * @param $roles
     * @return bool
     */
    protected function isAdmin($roles): bool
    {
        foreach ($roles as $role) {
            if($role->name == EnumRole::ADMIN){
                return true;
            }
        }
        return false;
    }


    /**
     * Role Manager
     * @param $roles
     * @return bool
     */
    protected function isManager($roles): bool
    {
        foreach ($roles as $role) {

            if($role->name == EnumRole::MANAGER){
                return true;
            }

//            if($role->name == EnumRole::TRAFFIC_CHIEF){
//                return true;
//            }

            if($role->name == EnumRole::ERP){
                return true;
            }
        }
        return false;
    }




    /**
     * Role Staff
     * @param $roles
     * @return bool
     */
    protected function isUser($roles): bool
    {
        foreach ($roles as $role) {

            if($role->name == EnumRole::USER){
                return true;
            }

        }
        return false;
    }


//    /**
//     * Role Driver
//     * @param $roles
//     * @return bool
//     */
//    protected function isDriver($roles): bool
//    {
//        foreach ($roles as $role) {
//
//            if($role->name == EnumRole::DRIVER){
//                return true;
//            }
//
//        }
//        return false;
//    }

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
