import os
from gen.helpers.helper_print import print_message, GREEN, CYAN
from gen.react.to_create_module_crud.standard_module_crud_react import standard_module_crud_react


def generate_modules(full_path):
    """
    Genera el archivo
    """

    # Perfil
    standard_module_crud_react(
        full_path,
        "Profile",
        "Profiles",
        [
            {"name": "name", "type": "STRING", "allowNull": True},
            {"name": "email", "type": "STRING", "allowNull": True},
            {"name": "password", "type": "STRING", "allowNull": True},
            {"name": "image_url", "type": "STRING", "allowNull": True},
        ],
        ["route", "list", "create", "edit", "barrel", "service"],
    )


    # User Status
    standard_module_crud_react(
        full_path,
        "UserStatus",
        "UserStatuses",
        [
            {"name": "name", "type": "STRING", "allowNull": True},
        ],
        ["route", "list", "create", "edit", "barrel", "service"],
    )

    # User
    standard_module_crud_react(
        full_path,
        "User",
        "Users",
        [
            {"name": "user_status_id", "type": "fk", "allowNull": True},
            {"name": "name", "type": "STRING", "allowNull": True},
            {"name": "email", "type": "STRING", "allowNull": True},
            {"name": "password", "type": "STRING", "allowNull": True},
            {"name": "email_verfied_at", "type": "STRING", "allowNull": True},
            {"name": "image_url", "type": "STRING", "allowNull": True},
        ],
        ["route", "list", "create", "edit", "barrel", "service"],
    )

    # Teams
    standard_module_crud_react(
        full_path,
        "Team",
        "Teams",
        [
            {"name": "name", "type": "STRING", "allowNull": True},
            {"name": "description", "type": "STRING", "allowNull": True},
        ],
        ["route", "list", "create", "edit", "barrel", "service"],
    )

    # System
    standard_module_crud_react(
        full_path,
        "System",
        "Systems",
        [
            {"name": "name", "type": "STRING", "allowNull": True},
            {"name": "status", "type": "STRING", "allowNull": True},
            {"name": "version", "type": "STRING", "allowNull": True},
        ],
        ["route", "list", "create", "edit", "barrel", "service"],
    )

    # Quotes
    standard_module_crud_react(
        full_path,
        "Quote",
        "Quotes",
        [
            {"name": "author", "type": "STRING", "allowNull": True},
            {"name": "feedback", "type": "STRING", "allowNull": True},
            {"name": "title", "type": "STRING", "allowNull": True},
        ],
        ["route", "list", "create", "edit", "barrel", "service"],
    )
