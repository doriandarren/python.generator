import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_seeder_abilities(full_path):
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
    file_path = os.path.join(styles_path, "AbilitySeeder.php")

    # Contenido por defecto
    content = """<?php

namespace Database\\Seeders;

use App\\Enums\\EnumAbilitySuffix;
use App\\Models\\Abilities\\Ability;
use App\\Models\\AbilityGroups\\AbilityGroup;
use Illuminate\\Database\\Seeder;
use Illuminate\\Support\\Facades\\DB;
use App\\Enums\\Dev\\EnumExcludeTable;

class AbilitySeeder extends Seeder
{

	/**
	* Run the database seeds.
	*
	* @return void
	*/
	public function run()
	{
        $this->createAbilities();
	}


    private function createAbilities()
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

        if(!AbilityGroup::where('name', $name)->exists()){
            $abilityGroup = AbilityGroup::factory()->create([
                'name' => $name,
            ]);
            return $abilityGroup;
        }

        return null;
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
