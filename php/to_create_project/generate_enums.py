import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_enums(full_path):
    create_dev(full_path)
    create_exclude_table(full_path)
    create_role(full_path)
    create_user(full_path)
    create_user_status(full_path)
    create_ability_groups(full_path)
    create_ability_suffix(full_path)
    create_api_setup(full_path)
    create_setting_paginate(full_path)




def create_dev(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Enums", "Dev")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "EnumDefaultCompany.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Enums\\Dev;

class EnumDefaultCompany
{

    /**
     * User Admin
     */
    const MY_COMPANY_ID = 1;
    const MY_COMPANY_DOMAIN = 'site.com';
    const PASSWORD = 'Site2024';


    /**
     * Admin
     */
    const ADMIN_NAME = 'Admin';
    const ADMIN_EMAIL = 'webmaster@site.com';


    /**
     * Manager
     */
    const MANAGER_NAME = 'Manager';
    const MANAGER_EMAIL = 'manager@site.com';


    /**
     * User
     */
    const USER_NAME = 'User';
    const USER_EMAIL = 'user@site.com';

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_exclude_table(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Enums", "Dev")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "EnumExcludeTable.php")

    # Contenido por defecto
    content = r"""<?php

namespace App\Enums\Dev;

enum EnumExcludeTable
{

    const EXCLUDE_TABLE = [
        'migrations',
        'failed_jobs',
        'jobs',
        'job_batches',
        'cache',
        'cache_locks',
        'password_resets',
        'personal_access_tokens',
        'password_reset_tokens',
        'sessions',
    ];


}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_role(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Enums", "Roles")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "EnumRole.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Enums\\Roles;

class EnumRole
{
    const ADMIN = 'admin';
    const MANAGER = 'manager';
    const USER = 'user';
    const ERP = 'erp'; // role API connect

    //Description
    const ADMIN_DESCRIPTION = 'Admin';
    const MANAGER_DESCRIPTION = 'Manager';
    const USER_DESCRIPTION = 'User';
    const ERP_DESCRIPTION = 'Erp'; // role API connect
    

    // ID's
    const ADMIN_ID = 1;
    const MANAGER_ID = 2;
    const USER_ID = 3;
    const ERP_ID = 4;

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_user(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Enums", "Users")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "EnumUser.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Enums\\Users;

enum EnumUser
{

    const WEBMASTER_EMAIL = 'webmaster@base.com';
    const WEBMASTER_PASSWORD = 'Base2024';
    
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_user_status(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Enums", "UserStatuses")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "EnumUserStatus.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Enums\\UserStatuses;

class EnumUserStatus
{
    const STATUS_ACTIVE_ID = 1;
    const STATUS_INACTIVE_ID = 2;

    const STATUS_ACTIVE_NAME = 'Active';
    const STATUS_INACTIVE_NAME = 'Inactive';
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_ability_groups(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Enums")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "EnumAbilityGroups.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Enums;

class EnumAbilityGroups
{

    /************************************************************************
     ************************************************************************
     ****
     * -----  RECUERDA ------
     *
     * Importante!!!! si se cambia los valores de este fichero, luego se tiene
     * que ejecutar el siguiente script en el test para ACTUALIZAR la BD:
     *
     * public function __invoke()
     * {
     *      (new BatchAbilityAndGroupRepository())->createAbilities(); // este
     * }
     *
     *
     *************************************************************************
     *************************************************************************
     */



    /**
     * Role Manager
     */
    const ABILITIES_GROUP_BY_MANAGER = [
        [
            'name' => 'ability_groups',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],
        [
            'name' => 'ability_user',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],
        [
            'name' => 'users',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],
        [
            'name' => 'user_statuses',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],
        [
            'name' => 'role_user',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],

        //TODO agregar los demás

    ];




    /**
     * Role MANGER
     */
    const ABILITIES_GROUP_BY_USER = [
        [
            'name' => 'ability_groups',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],
        [
            'name' => 'ability_user',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],
        [
            'name' => 'users',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],
        [
            'name' => 'user_statuses',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],
        [
            'name' => 'role_user',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],

        //TODO agregar los demás

    ];





    /**
     * Role ERP
     */
    const ABILITIES_GROUP_BY_ERP = [
        [
            'name' => 'ability_groups',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],
        [
            'name' => 'ability_user',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],
        [
            'name' => 'users',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],
        [
            'name' => 'user_statuses',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],
        [
            'name' => 'role_user',
            'abilities' => [
                EnumAbilitySuffix::LIST,
                EnumAbilitySuffix::SHOW,
                EnumAbilitySuffix::STORE,
                EnumAbilitySuffix::UPDATE,
                EnumAbilitySuffix::DESTROY,
            ],
        ],

        //TODO agregar los demás

    ];

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_ability_suffix(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Enums")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "EnumAbilitySuffix.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Enums;

abstract class EnumAbilitySuffix
{

    /**
     * Suffix for ability name
     */
    const ALL = ':all';
    const LIST = ':list';
    const STORE = ':store';
    const UPDATE = ':update';
    const DESTROY = ':destroy';
    const SHOW = ':show';
    
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_api_setup(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Enums")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "EnumApiSetup.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Enums;

abstract class EnumApiSetup
{

    const API_VERSION = 'v1/';

    const API_NAME = 'api/';

    const QUERY_LIMIT = 2000;



    const API_DRIVER = 'driver-app/';

    const API_OFFICE = 'office/';

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_setting_paginate(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Enums")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "EnumSettingPaginate.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Enums;

abstract class EnumSettingPaginate
{

    const PER_PAGE = '10';

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)




