import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command



def generate_batch_processes(full_path):
    create_ability_and_group(full_path)
    create_reload_database(full_path)



def create_ability_and_group(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Repositories", "BatchProcesses", "Abilities")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "BatchAbilityAndGroupRepository.php")

    # Contenido por defecto
    content = r"""<?php

namespace App\Repositories\BatchProcesses\Abilities;

use App\Enums\Dev\EnumExcludeTable;
use App\Enums\EnumAbilitySuffix;
use App\Models\Abilities\Ability;
use App\Models\AbilityGroups\AbilityGroup;
use Illuminate\Support\Facades\DB;


class BatchAbilityAndGroupRepository
{

    public function createAbilities()
    {

        $excludeTable = EnumExcludeTable::EXCLUDE_TABLE;

        $connections = [
            'api',
        ];

        //$arrModule = [];



        if(!AbilityGroup::where('name', 'All')->exists()){
            AbilityGroup::factory()->create([
                'name' => 'All',
            ]);
        }


        if(!Ability::where('name', '*')->exists()){
            Ability::factory()->create([
                'name' => '*',
                'label' => 'All',
                'ability_group_id' => 1,
            ]);
        }



        foreach ($connections as $connection_name) {

            $connection = config("database.connections.{$connection_name}");
            $database = 'Tables_in_' . $connection['database'];
            $tables = DB::connection($connection_name)->select('SHOW TABLES');

            foreach ($tables as $k => $v) {

                $tableName = $v->{$database};

                if(!in_array($tableName, $excludeTable)){

                    $abilityGroup = $this->createAbilityGroups($tableName);

                    $this->createModuleAbilities($tableName, $abilityGroup->id);

                }

            }

        }



        /**
         * Manuals
         */
//        $abilityGroup = $this->createAbilityGroups('action_task_camera_image');
//        $this->createModuleAbilities('action_task_camera_image', $abilityGroup->id);
//
//        $abilityGroup = $this->createAbilityGroups('action_stage_camera_image');
//        $this->createModuleAbilities('action_stage_camera_image', $abilityGroup->id);

    }


    private function createModuleAbilities($tableName, $abilityGroupId)
    {

        if(!Ability::where('name', $tableName.EnumAbilitySuffix::LIST)->exists()){
            Ability::factory()->create([
                'name' => $tableName.EnumAbilitySuffix::LIST,
                'label' => 'Lista modulo',
                'ability_group_id' => $abilityGroupId,
            ]);
        }

        if(!Ability::where('name', $tableName.EnumAbilitySuffix::STORE)->exists()){
            Ability::factory()->create([
                'name' => $tableName.EnumAbilitySuffix::STORE,
                'label' => 'Crea modulo',
                'ability_group_id' => $abilityGroupId,
            ]);
        }
        if(!Ability::where('name', $tableName.EnumAbilitySuffix::SHOW)->exists()){
            Ability::factory()->create([
                'name' => $tableName.EnumAbilitySuffix::SHOW,
                'label' => 'Ver modulo',
                'ability_group_id' => $abilityGroupId,
            ]);
        }
        if(!Ability::where('name', $tableName.EnumAbilitySuffix::UPDATE)->exists()){
            Ability::factory()->create([
                'name' => $tableName.EnumAbilitySuffix::UPDATE,
                'label' => 'Edita modulo',
                'ability_group_id' => $abilityGroupId,
            ]);
        }
        if(!Ability::where('name', $tableName.EnumAbilitySuffix::DESTROY)->exists()){
            Ability::factory()->create([
                'name' => $tableName.EnumAbilitySuffix::DESTROY,
                'label' => 'Elimina modulo',
                'ability_group_id' => $abilityGroupId,
            ]);
        }

    }


    private function createAbilityGroups($name)
    {

        $group = AbilityGroup::where('name', $name)->first();

        if(!$group){
            $abilityGroup = AbilityGroup::factory()->create([
                'name' => $name,
            ]);
            return $abilityGroup;
        }else{
            return $group;
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



def create_reload_database(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Repositories", "BatchProcesses", "Abilities")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "BatchReloadDatabaseAbilitiesRepository.php")

    # Contenido por defecto
    content = r"""<?php

namespace App\Repositories\BatchProcesses\Abilities;

use App\Enums\EnumAbilityGroups;
use App\Enums\Roles\EnumRole;
use App\Models\Abilities\Ability;
use App\Models\AbilityGroups\AbilityGroup;
use App\Models\AbilityUsers\AbilityUser;
use App\Models\User;
use App\Repositories\AbilityUsers\AbilityUserRepository;


class BatchReloadDatabaseAbilitiesRepository
{

    public function __invoke()
    {

        ini_set('memory_limit', '-1');

        $users = User::all();

        //$users = User::where('id', '>', 1)->get();

        foreach ($users as $user) {

            if(count($user->roles) > 1){
                echo "Error. El usuario: " . $user->name . " Tiene más de un rol. Tiene roles: " . count($user->roles);
                break;
            }


            if(!$user->abilities){
                dd($user);
            }



            //echo "EL usuario ($user->id): " . $user->email . "<br>";
            $roleId = 0;

            foreach ($user->roles as $i => $role) {
                if($i == 0){
                    if($role->pivot->role_id != EnumRole::ADMIN_ID){
                        $roleId = $role->pivot->role_id;
                        //echo "Role: " . $roleId . "<br>";
                    }
                }
            }


            $arrAbilities = [];

            if($roleId == EnumRole::MANAGER_ID){
                $arrAbilities = EnumAbilityGroups::ABILITIES_GROUP_BY_MANAGER;
            }
//            else if($roleId == EnumRole::TRAFFIC_CHIEF_ID){
//                $arrAbilities = EnumAbilityGroups::ABILITIES_GROUP_BY_TRAFFIC_CHIEF;
//            }else if($roleId == EnumRole::TRAFFIC_MANAGER_ID){
//                $arrAbilities = EnumAbilityGroups::ABILITIES_GROUP_BY_TRAFFIC_MANAGER;
//            }else if($roleId == EnumRole::DRIVER_ID){
//                $arrAbilities = EnumAbilityGroups::ABILITIES_GROUP_BY_DRIVER;
//            }else if($roleId == EnumRole::ERP_ID){
//                $arrAbilities = EnumAbilityGroups::ABILITIES_GROUP_BY_ERP;
//            }



            if(count($arrAbilities) > 0){

                $this->findGroup($user, $roleId, $arrAbilities);

            }



        }


    }




    private function findGroup($user, $roleId, $arrAbilities)
    {

        foreach ($arrAbilities as $arrAbility) {

            $arrEnabled = [];
            $arrDisabled = [];

            //echo "HABILIDAD: " . $arrAbility["name"] . "<br>";

            //Abilities DB
            $abilityGroupDB = AbilityGroup::where('name', $arrAbility["name"])->first();

            //dd($abilityGroupDB->abilities);


            //Abilities Arr
//            echo "Abilities ARR: <br>";
//            foreach ($arrAbility["abilities"] as $ability) {
//
//                echo $arrAbility["name"] . $ability;
//                echo "<br>";
//
//            }
//
//            echo "<br>";
//
//            echo "Abilities DB: <br>";
//            foreach ($abilityGroupDB->abilities as $abilityDB) {
//                echo $abilityDB->name;
//                echo "<br>";
//            }
//
//
//            echo "<br> .--------. <br>";



            //Busco las enabled
            foreach ($arrAbility["abilities"] as $ability) {

                $nameAbilityArr = $arrAbility["name"] . $ability;
                //echo "<br>";

                foreach ($abilityGroupDB->abilities as $abilityDB) {

                    if($nameAbilityArr === $abilityDB->name){
                        $arrEnabled[] = $abilityDB->name;
                    }
                }


            }



            //Buscar las disabled:
            foreach ($abilityGroupDB->abilities as $abilityDB) {

                $flag = FALSE;

                foreach ($arrEnabled as $item) {
                    if($abilityDB->name == $item){
                        $flag = true;
                    }
                }

                if(!$flag){
                    $arrDisabled[] = $abilityDB->name;
                }

            }


            $this->updateUserAbilities($user, $arrEnabled, $arrDisabled);

//            print_r($arrEnabled);
//            print_r($arrDisabled);

            //dd("wait");


        }



        //dd("Pasaa");

    }



    private function updateUserAbilities($user, $arrEnabled, $arrDisabled)
    {

        //dd($arrEnabled);

        foreach ($arrEnabled as $enable) {

            $abilityFind = Ability::where('name', $enable)->first();

            $flag = false;

            foreach ($user->abilities as $ability) {

                if($ability->id == $abilityFind->id){
                    //echo "Existe : ". $abilityFind->name;
                    $flag = true;
                }

            }

            //Crea sino existe
            if(!$flag){
                $rep = new AbilityUserRepository();
                $abilityUserObj = $rep->setAbilityUser($user->id, $abilityFind->id);
                $rep->store($abilityUserObj);
            }

        }


        foreach ($arrDisabled as $disabled) {

            foreach ($user->abilities as $ability) {

                if($ability->name == $disabled){

                    $abilityUser = AbilityUser::where('user_id', $user->id)
                        ->where('ability_id', $ability->id)
                        ->first();
                    $abilityUser->delete();

                }
            }

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
