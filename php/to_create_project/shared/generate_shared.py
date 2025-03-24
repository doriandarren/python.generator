import os
from helpers.helper_print import print_message, GREEN, CYAN
from php.to_create_project.shared.abilities.generate_controller_abilities import generate_controller_abilities

from php.to_create_project.shared.abilities.generate_model_abilities import generate_model_abilities
from php.to_create_project.shared.ability_users.generate_model_ability_users import generate_model_ability_users
from php.to_create_project.shared.ability_users.generate_repository_ability_users import generate_repository_ability_users

from php.to_create_project.shared.abilities.generate_repository_abilities import generate_repository_abilities
from php.to_create_project.shared.ability_groups.generate_controller_ability_groups import \
    generate_controller_ability_groups
from php.to_create_project.shared.ability_groups.generate_model_ability_groups import generate_model_ability_groups
from php.to_create_project.shared.ability_groups.generate_repository_ability_groups import \
    generate_repository_ability_groups
from php.to_create_project.shared.ability_users.generate_controller_ability_users import \
    generate_controller_ability_users
from php.to_create_project.shared.countries.generate_controller_countries import generate_controller_countries
from php.to_create_project.shared.countries.generate_model_countries import generate_model_countries
from php.to_create_project.shared.countries.generate_repository_countries import generate_repository_countries
from php.to_create_project.shared.role_users.generate_controller_role_users import generate_controller_role_users
from php.to_create_project.shared.role_users.generate_model_role_users import generate_model_role_users
from php.to_create_project.shared.roles.generate_controller_roles import generate_controller_roles
from php.to_create_project.shared.roles.generate_model_roles import generate_model_roles
from php.to_create_project.shared.roles.generate_repository_roles import generate_repository_roles
from php.to_create_project.shared.user_statuses.generate_controller_user_statuses import \
    generate_controller_user_statuses
from php.to_create_project.shared.user_statuses.generate_model_user_statuses import generate_model_user_statuses
from php.to_create_project.shared.user_statuses.generate_repository_user_statuses import \
    generate_repository_user_statuses


def generate_shared(full_path):

    # Abilities
    generate_controller_abilities(full_path)
    generate_model_abilities(full_path)
    generate_repository_abilities(full_path)


    # Abilities Groups
    generate_controller_ability_groups(full_path)
    generate_model_ability_groups(full_path)
    generate_repository_ability_groups(full_path)


    # Abilities Users
    generate_controller_ability_users(full_path)
    generate_model_ability_users(full_path)
    generate_repository_ability_users(full_path)


    # Countries
    generate_controller_countries(full_path)
    generate_model_countries(full_path)
    generate_repository_countries(full_path)

    # Role Users
    generate_controller_role_users(full_path)
    generate_model_role_users(full_path)


    # Role
    generate_controller_roles(full_path)
    generate_model_roles(full_path)
    generate_repository_roles(full_path)

    # User Statuses
    generate_controller_user_statuses(full_path)
    generate_model_user_statuses(full_path)
    generate_repository_user_statuses(full_path)


