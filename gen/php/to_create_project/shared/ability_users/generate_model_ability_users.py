import os
from gen.helpers.helper_print import print_message, GREEN, CYAN




def generate_model_ability_users(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Models", "AbilityUsers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "AbilityUser.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Models\\AbilityUsers;

use App\\Models\\Abilities\\Ability;
use App\\Models\\User;
use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;
use Illuminate\\Database\\Eloquent\\Relations\\BelongsTo;

class AbilityUser extends Model
{

    use HasFactory;

    //use SoftDeletes;

    protected $connection = 'api';
    protected $table = 'ability_user';

    /***********************
     * RELATIONS
     ***********************/

    /**
     * @return BelongsTo
     */
    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class, 'user_id', 'id');
    }



    /**
     * @return BelongsTo
     */
    public function ability(): BelongsTo
    {
        return $this->belongsTo(Ability::class, 'ability_id', 'id');
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



