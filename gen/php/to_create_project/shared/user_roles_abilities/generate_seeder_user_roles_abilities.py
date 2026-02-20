import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_seeder_user_roles_abilities(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "database", "seeders")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "UserRolesAbilitiesSeeder.php")

    # Contenido por defecto
    content = """<?php

namespace Database\\Seeders;


use App\\Enums\\Dev\\EnumDefaultCompany;
use App\\Enums\\EnumAbilityGroups;
use App\\Enums\\Roles\\EnumRole;
use App\\Enums\\UserStatuses\\EnumUserStatus;
use App\\Models\\Abilities\\Ability;
use App\\Models\\Roles\\Role;
use App\\Models\\User;
use App\\Models\\UserStatuses\\UserStatus;
use Illuminate\\Database\\Seeder;



class UserRolesAbilitiesSeeder extends Seeder
{

    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {

        /**
         * Create User
         */
        // ADMIN
        $this->createUser(EnumDefaultCompany::ADMIN_NAME, EnumDefaultCompany::ADMIN_EMAIL, EnumDefaultCompany::PASSWORD,EnumRole::ADMIN);

        /**
         * Create Manager
         */

        $this->createUser(EnumDefaultCompany::MANAGER_NAME, EnumDefaultCompany::MANAGER_EMAIL, EnumDefaultCompany::PASSWORD,EnumRole::MANAGER);

        /**
         * Create User
         */
        $this->createUser(EnumDefaultCompany::USER_NAME, EnumDefaultCompany::USER_EMAIL, EnumDefaultCompany::PASSWORD,EnumRole::USER);



    }


    /**
     * @param $user
     * @param $roleName
     * @return void
     */
    private function createRoleUser($user, $roleName): void
    {
        $user = User::find($user->id);

        $role = Role::where('name', strtolower($roleName))->first();
        $user->assignRole($role);

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

        // Create User
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
        }


        // Crete RoleUser
        $this->createRoleUser($user, $roleName);

        // Create AbilityUser
        $this->createAbilityUser($user, $roleName);

    }



    /**
     * @param $user
     * @param $roleName
     * @return void
     */
    private function createAbilityUser($user, $roleName): void
    {

        /**
         * Add Ability only Admin
         */
        if($roleName == EnumRole::ADMIN){

            $ability = Ability::where('name', '*')->first();
            $user->allowTo($ability);

        }


        if($roleName == EnumRole::MANAGER){

            foreach (EnumAbilityGroups::ABILITIES_GROUP_BY_MANAGER as $abilityRecord) {

                foreach ($abilityRecord["abilities"] as $ability) {

                    $nameAbility =  $abilityRecord["name"] . $ability;
                    //echo $nameAbility . "<br>";

                    $ability = Ability::where('name', $nameAbility)->first();
                    $user->allowTo($ability);

                }

            }

        }


        if($roleName == EnumRole::USER){

            foreach (EnumAbilityGroups::ABILITIES_GROUP_BY_USER as $abilityRecord) {

                foreach ($abilityRecord["abilities"] as $ability) {

                    $nameAbility =  $abilityRecord["name"] . $ability;
                    //echo $nameAbility . "<br>";

                    $ability = Ability::where('name', $nameAbility)->first();
                    $user->allowTo($ability);

                }

            }

        }


        if($roleName == EnumRole::ERP){

            foreach (EnumAbilityGroups::ABILITIES_GROUP_BY_ERP as $abilityRecord) {

                foreach ($abilityRecord["abilities"] as $ability) {

                    $nameAbility =  $abilityRecord["name"] . $ability;
                    //echo $nameAbility . "<br>";

                    $ability = Ability::where('name', $nameAbility)->first();
                    $user->allowTo($ability);

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
