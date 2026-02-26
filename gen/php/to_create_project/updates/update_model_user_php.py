import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command



def update_model_user(full_path):
    update_use(full_path)
    update_last_line(full_path)



def update_use(full_path):
    """
    Actualiza el archivo
    """
    main_jsx_path = os.path.join(full_path, "app", "Models", "User.php")

    # Verificar si el archivo existe
    if not os.path.exists(main_jsx_path):
        print_message(f"Error: {main_jsx_path} no existe.", CYAN)
        return

    try:

        # Leer el contenido del archivo
        with open(main_jsx_path, "r") as f:
            content = f.read()


        # Use Relations & HasApiTokens
        content = content.replace(
            "use Illuminate\\Notifications\\Notifiable;",
            """use Illuminate\\Notifications\\Notifiable;
use App\\Models\\Abilities\\Ability;
use App\\Models\\AbilityUsers\\AbilityUser;
use App\\Models\\Roles\\Role;
use App\\Models\\RoleUsers\\RoleUser;
use App\\Models\\UserStatuses\\UserStatus;
use Illuminate\\Database\\Eloquent\\Model;
use Illuminate\\Database\\Eloquent\\Relations\\BelongsTo;
use Illuminate\\Database\\Eloquent\\Relations\\BelongsToMany;
use Laravel\\Sanctum\\HasApiTokens;"""
        )




        ## add HasApiTokens
        content = content.replace(
            "use HasFactory, Notifiable;",
            "use HasApiTokens, HasFactory, Notifiable;"
        )



        # Escribir el contenido actualizado
        with open(main_jsx_path, "w") as f:
            f.write(content)

        print_message("use User Models correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {main_jsx_path}: {e}", CYAN)







def update_last_line(full_path):
    """
    Inserta contenido justo antes del cierre final de la clase User
    """
    user_model_path = os.path.join(full_path, "app", "Models", "User.php")

    if not os.path.exists(user_model_path):
        print_message(f"Error: {user_model_path} no existe.", CYAN)
        return

    try:
        with open(user_model_path, "r") as f:
            lines = f.readlines()

        # Buscar la última línea que contiene solo '}'
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].strip() == '}':
                # Insertar contenido justo antes de esa línea
                lines.insert(i, """
    
    /*********************
    * Relations
    ********************/
     
    /**
     * @return BelongsTo
     */
    public function status(): BelongsTo
    {
        return $this->belongsTo(UserStatus::class, 'user_status_id', 'id');
    }


    /**
     * @return BelongsToMany
     */
    public function roles(): BelongsToMany
    {
        return $this->belongsToMany(Role::class)->withTimestamps();
    }



    /**
     * @return BelongsToMany
     */
    public function abilities(): BelongsToMany
    {
        return $this->belongsToMany(Ability::class)->withTimestamps();
    }


    /*********************
     * Method implements
     ********************/

    /**
     * @param $ability
     * @return Model
     */
    public function allowTo($ability): Model
    {
        $abilityDuplicated = AbilityUser::where('user_id', $this->id)
            ->where('ability_id', $ability->id)
            ->first();

        if($abilityDuplicated){
            return $abilityDuplicated;
        }

        return $this->abilities()->save($ability);
    }


    /**
     * @param $role
     * @return Model
     */
    public function assignRole($role): Model
    {
        $roleDuplicated = RoleUser::where('user_id', $this->id)
            ->where('role_id', $role->id)
            ->first();

        if($roleDuplicated){
            return $roleDuplicated;
        }

        return $this->roles()->save($role);
    }
    
""")
                break

        with open(user_model_path, "w") as f:
            f.writelines(lines)

        print_message("Contenido insertado justo antes del cierre final de la clase.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {user_model_path}: {e}", CYAN)
