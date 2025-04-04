import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command


def generate_test_controller(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Http", "Controllers", "Dev")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "TestController.php")

    # Contenido por defecto
    content = r"""<?php

namespace App\Http\Controllers\Dev;

use App\Enums\EnumAbilityGroups;
use App\Enums\Roles\EnumRole;
use App\Enums\UserStatuses\EnumUserStatus;
use App\Http\Controllers\Controller;
use App\Models\Abilities\Ability;
use App\Models\AbilityGroups\AbilityGroup;
use App\Models\Roles\Role;
use App\Models\User;
use App\Models\UserStatuses\UserStatus;
use App\Repositories\BatchProcesses\Abilities\BatchAbilityAndGroupRepository;
use App\Repositories\BatchProcesses\Abilities\BatchReloadDatabaseAbilitiesRepository;
use App\Utilities\Exls\Exports\Example\ExampleExport;
use App\Utilities\Helpers\HelperFile;
use App\Utilities\Helpers\HelperMail;
use App\Utilities\Messages\MessageChannel;
use DateTime;
use Illuminate\Http\Response;
use Knp\Snappy\Pdf;
use Maatwebsite\Excel\Facades\Excel;
use setasign\Fpdi\Fpdi;
use stdClass;

class TestController extends Controller
{


    public function __invokeDISCORR()
    {
        MessageChannel::send('Hola Mundo!!!!', 'Titulo');
    }


    /**
     * Read Products
     */
    public function __invokeEEEWWWW()
    {

        $helper = new HelperFile();


        //$handle = $helper->openFileToRead(public_path('files') . '/tarifas_dispositivos_globalfleet.csv');
        $handle = $helper->openFileToRead(public_path('files') . '/e.csv');

        $arrayData = array();

        $i = 0;

        while (!feof($handle)) {
            $arrayData[$i] = fgets($handle);
            $i++;
        }


        $i = 0;
        while ($i < count($arrayData)) {

            $line = explode(";", $arrayData[$i]);

            if($line[1] != '') {

                echo $description = $line[0] . ' ';
                echo "<br>";

            }

            $i++;
        }

    }







    /*******************************************
     * ONLY VERSIONS BASE
     ******************************************/


    /**
     * Snappy
     */
    public function __invoke()
    {
        $snappy = new Pdf();

        //$snappy->setBinary('/usr/local/bin/wkhtmltopdf');
        $snappy->setBinary(base_path() . '/vendor/h4cc/wkhtmltopdf-amd64/bin/wkhtmltopdf-amd64');


        $html = '<h1>Bill</h1><p>You owe me money, dude.</p>';
        $snappy->generateFromHtml($html, base_path('public') . '/files/test.pdf');


        return new Response(
            $snappy->getOutputFromHtml($html),
            200,
            array(
                'Content-Type'          => 'application/pdf',
                'Content-Disposition'   => 'attachment; filename="file.pdf"'
            )
        );


    }













    /**
     * Laravel Excel
     */
    public function __invokeEXCEL()
    {
        /**
         * IMPORTANTE!!! -> Si todo va bien el archivo estara en storage/app/private/exampleExport.xlsx
         */
         
        // Data Fake replace by Collection
        $arrData = [];
        $data = new stdClass();

        $data->invoice_date = "2024-01-01";
        $data->invoice_number = "ES019098";
        $data->card_code = "98M986h";
        $data->card = "00019";
        $data->plate = "9898KDF";

        $arrData[] = $data;


        Excel::store(new ExampleExport($arrData), 'exampleExport.xlsx');

        //dd(public_path('files') );

        //return (new ExampleExport())->store( public_path('files') . '/exampleExport.xlsx');

        //dd("pasa");

    }




    /**
     * PDF Snappy
     */
    public function __invokeSnappy()
    {
        $snappy = new Pdf();

        //$snappy->setBinary('/usr/local/bin/wkhtmltopdf');
        $snappy->setBinary(base_path() . '/vendor/h4cc/wkhtmltopdf-amd64/bin/wkhtmltopdf-amd64');


        $html = '<h1>Bill</h1><p>You owe me money, dude.</p>';
        $snappy->generateFromHtml($html, base_path('public') . '/files/test.pdf');


        return new Response(
            $snappy->getOutputFromHtml($html),
            200,
            array(
                'Content-Type'          => 'application/pdf',
                'Content-Disposition'   => 'attachment; filename="file.pdf"'
            )
        );
    }






    /**
     * PDF Merge
     */
    public function __invokeFPDI()
    {


        //dd(public_path('files/example/test.pdf'));

        $pdf = new Fpdi();

        // Definir los archivos PDF que deseas combinar
        $files = [
            public_path('files/example/pdf1.pdf'),
            public_path('files/example/pdf2.pdf'),
        ];


        // Iterar sobre cada archivo PDF
        foreach ($files as $file) {
            $pageCount = $pdf->setSourceFile($file); // Cargar el archivo PDF
            for ($pageNo = 1; $pageNo <= $pageCount; $pageNo++) {
                $pdf->AddPage(); // Añadir una nueva página en el documento de salida
                $tplId = $pdf->importPage($pageNo); // Importar la página
                $pdf->useTemplate($tplId); // Colocar la página importada en la página creada
            }
        }

        // Definir el nombre del archivo de salida
        $outputPath = public_path('files/example/merged.pdf');
        $pdf->Output('F', $outputPath); // Guardar el archivo combinado

        //return response()->download($outputPath); // Descargar o mostrar el PDF combinado

        dd("Pasa OKKK");
    }







    /*********************************************************
     *
     * GENERATE ABILITIES OF THE EnumAbilityGroups
     *
     *********************************************************/

    /**
     * 1.- No borrar sirve para actualizar las Abilities de la DB
     *
     * 2.- Recarga las abilidades de los usuarios
     *
     * @return void
     */
    public function __invokeABBB()
    {

        // No borrar sirve para actualizar las Abilities de la DB
        (new BatchAbilityAndGroupRepository())->createAbilities();


        // Recarga las abilidades de los usuarios
        (new BatchReloadDatabaseAbilitiesRepository())->__invoke();

        echo "OK Bash Abilities";

    }

    /**
     * *******************************************************
     */






    /*******************************
     * Create User
     */

    public function __invokeCREATEUSER()
    {


        // No borrar sirve para actualizar las Abilities de la DB
        (new \App\Repositories\BatchProcesses\Abilities\BatchAbilityAndGroupRepository())->createAbilities();


        // Recarga las abilidades de los usuarios
        (new \App\Repositories\BatchProcesses\Abilities\BatchReloadDatabaseAbilitiesRepository())->__invoke();

        echo "OK Bash Abilities <br>";



        $name = 'Eugeni';
        $email = 'eugeni@transportuarios.com';
        $password = 'j4p5hwtf';

        // MANAGER
        $this->createUser($name,$email, $password, EnumRole::MANAGER);


        echo "Usuario creado: " . $email;

    }



    /**
     * @param $name
     * @param $email
     * @param $password
     * @param $roleName
     * @return void
     */
    private function createUser($name, $email, $password, $roleName): void
    {

        $userActiveId = UserStatus::where('name', EnumUserStatus::STATUS_ACTIVE_NAME)->first()->id;

        $user = User::where('email', $email)->first();

        if (!$user) {

            $user = User::factory()->create([
                'name' => $name,
                'email' => $email,
                'email_verified_at' => now(),
                'password' => bcrypt($password), // password
                'remember_token' => NULL,
                'user_status_id' => $userActiveId,
            ]);

            $this->createRoleUser($user, $roleName);

            $this->createAbilities($user, $roleName);

        }

    }


    private function createRoleUser($user, $roleName)
    {

        $user = User::find($user->id);

        if($roleName == EnumRole::ADMIN){
            $role = Role::where('name', EnumRole::ADMIN)->first();
            $user->assignRole($role);
        }


        if($roleName == EnumRole::MANAGER){
            $role = Role::where('name', EnumRole::MANAGER)->first();
            $user->assignRole($role);

        }


        if($roleName == EnumRole::ERP){
            $role = Role::where('name', EnumRole::ERP)->first();
            $user->assignRole($role);

        }

    }


    /**********************
     * Create All Abilities
     **********************/
    private function createAbilities($user, $roleName): void
    {


        if($roleName == EnumRole::ADMIN){
            $ability = Ability::where('name', '*')->first();
            $user->allowTo($ability);
        }


        if($roleName == EnumRole::MANAGER){

            $this->createAbilityByRol($user, EnumAbilityGroups::ABILITIES_GROUP_BY_MANAGER);

        }

        if($roleName == EnumRole::ERP){

            $this->createAbilityByRol($user, EnumAbilityGroups::ABILITIES_GROUP_BY_ERP);

        }

    }


    private function createAbilityByRol($user, $groupsArr)
    {

        $groupsToAssign = json_decode(json_encode($groupsArr, true));


        foreach ($groupsToAssign as $groupToAssign) {

            $abilityGroupDB = AbilityGroup::with(['abilities'])->where('name', $groupToAssign->name)->first();

            if(isset($abilityGroupDB->abilities)){

                foreach ($abilityGroupDB->abilities as $abilityDB) {

                    $flag = $this->isAbility($abilityDB->name, $groupToAssign->name, $groupToAssign->abilities);

                    if($flag){
                        $abilityActive = Ability::where('id', $abilityDB->id)->first();
                        $user->allowTo($abilityActive);
                    }

                }

            }else{
                dd("Error de esta tabla: " . $groupToAssign->name . " es: " . $abilityGroupDB);
            }

        }

    }


    private function isAbility($nameDB, $nameAssign, $abilities): bool
    {
        foreach ($abilities as $ability) {
            if($nameDB == ($nameAssign . $ability)){
                return true;
            }
        }
        return false;
    }



    /**
     * END Create User
     *******************************/
     
     
     
     
     
     /*********************************************************
     *
     * GENERATE ABILITIES OF THE EnumAbilityGroups
     *
     *********************************************************/

    // Crear para abstract class UserPermissions
    public function __invokeAAAASSSSS(Request $request)
    {

        $excludeTable = [
            'migrations',
            'failed_jobs',
            'password_resets',
            'personal_access_tokens',
        ];



        $connections = [
            'api',
        ];


        $arrModule = [];


        foreach ($connections as $connection_name) {

            $connection = config("database.connections.{$connection_name}");
            $database = 'Tables_in_' . $connection['database'];
            $tables = DB::connection($connection_name)->select('SHOW TABLES');

            foreach ($tables as $k => $v) {

                $tableName = $v->{$database};

                if(!in_array($tableName, $excludeTable)){

                    $modules = $this->createConstModulePrintScreen($tableName);

                    foreach ($modules as $module) {
                        $arrModule[] = $module;
                    }

                }

            }
        }


        echo "/**<br>";
        echo "* @return string[]<br>";
        echo "*/<br>";
        echo 'public static function getModules(): array<br>';
        echo '{<br>';
        echo 'return [<br>';

        foreach ($arrModule as $module) {
            echo 'self::' . $module . ',<br>';
        }

        echo '];<br>';
        echo '}<br>';


    }

    private function createConstModulePrintScreen($tableName)
    {

        //echo $tableName . "<br>";


        //$module = 'MODULE_' . strtoupper($tableName);
        $list = 'MODULE_' . strtoupper($tableName) . '_LIST';
        $store = 'MODULE_' . strtoupper($tableName) . '_STORE';
        $show = 'MODULE_' . strtoupper($tableName) . '_SHOW';
        $update = 'MODULE_' . strtoupper($tableName) . '_UPDATE';
        $destroy = 'MODULE_' . strtoupper($tableName) . '_DESTROY';


        echo '// ' . ucfirst($tableName) . "<br>";
        //echo 'const ' . $module . ' = \'' . $tableName . '\';' . "<br>";
        echo 'const ' . $list . ' = \'' . $tableName . '\' . EnumAbilitySuffix::LIST;' . "<br>";
        echo 'const ' . $store .' = \'' . $tableName . '\' . EnumAbilitySuffix::STORE;' . "<br>";
        echo 'const ' . $show . ' = \'' . $tableName . '\' . EnumAbilitySuffix::SHOW;' . "<br>";
        echo 'const ' . $update . ' = \'' . $tableName . '\' . EnumAbilitySuffix::UPDATE;' . "<br>";
        echo 'const ' . $destroy . ' = \'' . $tableName . '\' . EnumAbilitySuffix::DESTROY;' . "<br><br><br>";

        //return [$module, $list, $store, $show, $update, $destroy];
        return [$list, $store, $show, $update, $destroy];

    }


    /**
     * *******************************************************
     */
     
     
     

}

"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
