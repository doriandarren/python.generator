import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command



def generate_exception_handler(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Exceptions")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "Handler.php")

    # Contenido por defecto
    content = r"""<?php

namespace App\Exceptions;

use App\Utilities\Messages\MessageChannel;
use ErrorException;
use BadMethodCallException;
use Illuminate\Database\QueryException;
use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;
use Symfony\Component\HttpKernel\Exception\AccessDeniedHttpException;
use Symfony\Component\HttpKernel\Exception\MethodNotAllowedHttpException;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;
use Throwable;

class Handler extends ExceptionHandler
{
    /**
     * The list of the inputs that are never flashed to the session on validation exceptions.
     *
     * @var array<int, string>
     */
    protected $dontFlash = [
        'current_password',
        'password',
        'password_confirmation',
    ];

    /**
     * Register the exception handling callbacks for the application.
     */
    public function register(): void
    {
//        $this->reportable(function (Throwable $e) {
//            //
//        });



        //Response for AccessDeniedHttpException to API
        $this->renderable(function (AccessDeniedHttpException $e, $request) {
            if ($request->is('api/*')) {

                MessageChannel::send($e->getMessage(), 'Error AccessDeniedHttpException', true);

                return HandlerResponse::respondWithError($e->getMessage(), $e->getStatusCode());
            }
        });

        $this->renderable(function (MethodNotAllowedHttpException $e, $request) {
            if ($request->is('api/*')) {

                if($e->getMessage() == ''){
                    $message = 'Not Found';
                }else{
                    $message = $e->getMessage();
                }

                $errors = [[
                    'e' => $message
                ]];

                MessageChannel::send($e->getMessage(), 'Error MethodNotAllowedHttpException', true);

                return HandlerResponse::respondWithError('Error', $e->getStatusCode(), $errors);

            }
        });


        $this->renderable(function (NotFoundHttpException $e, $request) {
            if ($request->is('api/*')) {
                if($e->getMessage() == ''){
                    $message = 'Not Found';
                }else{
                    $message = $e->getMessage();
                }

                $errors = [[
                    'e' => $message
                ]];

                MessageChannel::send($e->getMessage(), 'Error NotFoundHttpException', true);

                return HandlerResponse::respondWithError('Error', $e->getStatusCode(), $errors);
            }
        });


        // Descomentar esto luego:
        $this->renderable(function (QueryException $e, $request) {
            if ($request->is('api/*')) {

                //$message = 'QueryException';

                $errors = [[
                    //'e' => $message
                    'e' => $e->getMessage()
                ]];

                MessageChannel::send($e->getMessage(), 'Error QueryException', true);

                return HandlerResponse::respondWithError('Error', 201, $errors);
            }
        });




        // Control error 500
        $this->renderable(function (ErrorException $e, $request) {
            if ($request->is('api/*')) {

                $errors = [[
                    'e' => $e->getMessage() . ' File: ' . $e->getFile() . ' Line: ' . $e->getLine()
                ]];


                MessageChannel::send($e->getMessage() . ' File: ' . $e->getFile() . ' Line: ' . $e->getLine(), 'Error 500', true);

                return HandlerResponse::respondWithError('Error', 500, $errors);
            }
        });


        $this->renderable(function (BadMethodCallException $e, $request) {
            if ($request->is('api/*')) {

                $errors = [[
                    'e' => $e->getMessage() . ' File: ' . $e->getFile() . ' Line: ' . $e->getLine()
                ]];


                MessageChannel::send($e->getMessage() . ' File: ' . $e->getFile() . ' Line: ' . $e->getLine(), 'Error 500', true);

                return HandlerResponse::respondWithError('Error', 500, $errors);
            }
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
