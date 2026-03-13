import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_dashboard(full_path):
    create_router(full_path)
    create_list_controller(full_path)
    create_repository(full_path)



def create_list_controller(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "Dashboards")
    file_path = os.path.join(folder_path, "DashboardListController.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''<?php

namespace App\Http\Controllers\API\Dashboards;

use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Http\Controllers\Controller;
use App\Repositories\API\Dashboards\DashboardRepository;

class DashboardListController extends Controller
{
    private DashboardRepository $repository;

    public function __construct()
    {
        $this->repository = new DashboardRepository();
    }

    /**
    * @header Authorization Bearer TOKEN
    *
    * @param Request $request
    * @return JsonResponse
    */
    public function __invoke(Request $request): JsonResponse
    {
        $data = [];

        if ($this->isAdmin(Auth::user()->roles)) {
            $data = $this->repository->start();
        } elseif ($this->isManager(Auth::user()->roles)) {
            $data = $this->repository->startByRoleManager();
        } elseif ($this->isUser(Auth::user()->roles)) {
            $data = $this->repository->startByRoleUser();
        }

        return $this->respondWithData('Dashboards list', $data);
    }
}

'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
        
        

        
def create_router(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "routes", "API")
    file_path = os.path.join(folder_path, "dashboards.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''<?php

// use App\Enums\EnumAbilitySuffix;
// use App\Enums\EnumApiSetup;
use App\Http\Controllers\API\Dashboards\DashboardListController;
use Illuminate\Support\Facades\Route;



/**
* Dashboards
*/
Route::group(['prefix' => 'dashboards/'], function () {

	Route::group(['middleware' => 'auth:sanctum'], function() {

		Route::get('list', [DashboardListController::class, '__invoke'])->middleware('abilities:dashboards' . EnumAbilitySuffix::LIST);

	});
});

'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
        
        
        
        
        




        
def create_repository(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Repositories", "API", "Dashboards")
    file_path = os.path.join(folder_path, "DashboardRepository.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''<?php

namespace App\Repositories\API\Dashboards;

// use App\Enums\EnumApiSetup;

class DashboardRepository
{

    // const WITH = [];

    /**
    * List
    */
    public function start()
    {
        // TODO implement
        return [];
    }

    /**
    * List by manager
    */
    public function startByRoleManager()
    {
        // TODO implement
        return [];
    }



    /**
    * List by user
    */
    public function startByRoleUser()
    {
        // TODO implement
        return [];
    }

}

'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

