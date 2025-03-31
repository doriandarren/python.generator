import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command



def update_bootstrap_app_php(full_path):
    update_abilities(full_path)



def update_abilities(full_path):
    """
    Actualiza el archivo
    """
    main_jsx_path = os.path.join(full_path, "bootstrap", "app.php")

    # Verificar si el archivo existe
    if not os.path.exists(main_jsx_path):
        print_message(f"Error: {main_jsx_path} no existe.", CYAN)
        return

    try:

        # Leer el contenido del archivo
        with open(main_jsx_path, "r") as f:
            content = f.read()


        # Uses
        content = content.replace(
            r"""<?php

""",
            r"""<?php

use Laravel\Sanctum\Http\Middleware\CheckAbilities;
use Laravel\Sanctum\Http\Middleware\CheckForAnyAbility;
use Illuminate\Http\Request;
use App\Utilities\Messages\MessageChannel;
use App\Exceptions\HandlerResponse;
use Symfony\Component\HttpKernel\Exception\AccessDeniedHttpException;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;
use Symfony\Component\HttpKernel\Exception\MethodNotAllowedHttpException;
use Illuminate\Database\QueryException;
"""
        )




        # Abilities
        content = content.replace(
            r"""->withMiddleware(function (Middleware $middleware) {
        //
    })""",
            r"""->withMiddleware(function (Middleware $middleware) {
        $middleware->alias([
            'abilities' => CheckAbilities::class,
            'ability' => CheckForAnyAbility::class,
        ]);
    })"""
        )




        # Exceptions
        content = content.replace(
            r"""->withMiddleware(function (Middleware $middleware) {""",
            r"""->withExceptions(function (Exceptions $exceptions) {
        // BadMethodCallException
        $exceptions->render(function (BadMethodCallException $e, Request $request) {
            if ($request->is('api/*')) {
                $msg = $e->getMessage() . ' File: ' . $e->getFile() . ' Line: ' . $e->getLine();
                MessageChannel::send($msg, 'Error BadMethodCallException', true);
                return HandlerResponse::respondWithError('Error Bad method call', 500, [[
                    'e' => $e->getMessage(),
                ]]);
            }
            return null;
        });

        // ErrorException
        $exceptions->render(function (ErrorException $e, Request $request) {
            if ($request->is('api/*')) {
                $msg = $e->getMessage() . ' File: ' . $e->getFile() . ' Line: ' . $e->getLine();
                MessageChannel::send($msg, 'Error ErrorException', true);
                return HandlerResponse::respondWithError('Error exception', 500, [[
                    'e' => $e->getMessage(),
                ]]);
            }
            return null;
        });

        // QueryException
        $exceptions->render(function (QueryException $e, Request $request) {
            if ($request->is('api/*')) {
                MessageChannel::send($e->getMessage(), 'Error QueryException', true);
                return HandlerResponse::respondWithError('Error Query Exception', 500, [[
                    'e' => $e->getMessage()
                ]]);
            }
            return null;
        });

        // NotFoundHttpException
        $exceptions->render(function (NotFoundHttpException $e, Request $request) {
            if ($request->is('api/*')) {
                $msg = $e->getMessage() ?: 'Error Not found';
                MessageChannel::send($msg, 'Error NotFoundHttpException', true);
                return HandlerResponse::respondWithError('Error Not found', 404, [[
                    'e' => $msg
                ]]);
            }
            return null;
        });

        // AccessDeniedHttpException
        $exceptions->render(function (AccessDeniedHttpException $e, Request $request) {
            if ($request->is('api/*')) {
                MessageChannel::send($e->getMessage(), 'Error AccessDeniedHttpException', true);
                return HandlerResponse::respondWithError('Error Access denied', 403, [[
                    'e' => $e->getMessage()
                ]]);
            }
            return null;
        });

        // MethodNotAllowedHttpException
        $exceptions->render(function (MethodNotAllowedHttpException $e, Request $request) {
            if ($request->is('api/*')) {
                $msg = $e->getMessage() ?: 'Error Method not allowed';
                MessageChannel::send($msg, 'Error MethodNotAllowedHttpException', true);
                return HandlerResponse::respondWithError('Error Method not allowed', 405, [[
                    'e' => $msg
                ]]);
            }
            return null;
        });
"""
        )



        # Escribir el contenido actualizado
        with open(main_jsx_path, "w") as f:
            f.write(content)

        print_message("boostrap/app.php Actulizado correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {main_jsx_path}: {e}", CYAN)




