import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_model_ability_groups(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Models", "AbilityGroups")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityGroup.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Models\\AbilityGroups;

use App\\Models\\Abilities\\Ability;
use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;
use Illuminate\\Database\\Eloquent\\Relations\\HasMany;

class AbilityGroup extends Model
{

    use HasFactory;
    //use SoftDeletes;

    protected $connection = 'api';
    protected $table = 'ability_groups';

    /***********************
     * RELATIONS
     ***********************/

    /**
     * @return HasMany
     */
    public function abilities(): HasMany
    {
        return $this->hasMany(Ability::class, 'ability_group_id', 'id');
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




