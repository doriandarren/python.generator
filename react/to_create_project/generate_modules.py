import os
from helpers.helper_print import print_message, GREEN, CYAN
from react.to_create_module.generate_module_standard_react import generate_module_standard_react


def generate_modules(full_path):
    """
    Genera el archivo
    """

    # Perfil
    generate_module_standard_react(
        full_path,
        "Profile",
        "Profiles",
        [
            {"name": "name", "type": "STRING", "allowNull": True},
            {"name": "email", "type": "STRING", "allowNull": True},
            {"name": "password", "type": "STRING", "allowNull": True},
            {"name": "image_url", "type": "STRING", "allowNull": True},
        ],
        ["route", "list", "create", "edit", "create", "barrel", "service"],
    )


    # User Status
    generate_module_standard_react(
        full_path,
        "UserStatus",
        "UserStatuses",
        [
            {"name": "name", "type": "STRING", "allowNull": True},
        ],
        ["route", "list", "create", "edit", "barrel", "service"],
    )

    # User
    generate_module_standard_react(
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
    generate_module_standard_react(
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
    generate_module_standard_react(
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
    generate_module_standard_react(
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
