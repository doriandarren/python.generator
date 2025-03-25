import os
from helpers.helper_print import print_message, GREEN, CYAN

from php.to_create_project.shared.abilities.generate_controller_abilities import generate_controller_abilities
from php.to_create_project.shared.abilities.generate_factory_abilities import generate_factory_abilities
from php.to_create_project.shared.abilities.generate_repository_abilities import generate_repository_abilities
from php.to_create_project.shared.abilities.generate_model_abilities import generate_model_abilities
from php.to_create_project.shared.abilities.generate_route_abilities import generate_route_abilities
from php.to_create_project.shared.abilities.generate_seeder_abilities import generate_seeder_abilities
from php.to_create_project.shared.ability_groups.generate_factory_ability_groups import generate_factory_ability_groups
from php.to_create_project.shared.ability_groups.generate_route_ability_groups import generate_route_ability_groups
from php.to_create_project.shared.ability_groups.generate_seeder_ability_groups import generate_seeder_ability_groups
from php.to_create_project.shared.ability_groups.generate_controller_ability_groups import generate_controller_ability_groups
from php.to_create_project.shared.ability_groups.generate_model_ability_groups import generate_model_ability_groups
from php.to_create_project.shared.ability_groups.generate_repository_ability_groups import generate_repository_ability_groups
from php.to_create_project.shared.ability_users.generate_controller_ability_users import generate_controller_ability_users
from php.to_create_project.shared.ability_users.generate_model_ability_users import generate_model_ability_users
from php.to_create_project.shared.ability_users.generate_repository_ability_users import generate_repository_ability_users
from php.to_create_project.shared.ability_users.generate_factory_ability_users import generate_factory_ability_users
from php.to_create_project.shared.ability_users.generate_route_ability_users import generate_route_ability_users
from php.to_create_project.shared.ability_users.generate_seeder_ability_users import generate_seeder_ability_users
from php.to_create_project.shared.countries.generate_controller_countries import generate_controller_countries
from php.to_create_project.shared.countries.generate_model_countries import generate_model_countries
from php.to_create_project.shared.countries.generate_repository_countries import generate_repository_countries
from php.to_create_project.shared.countries.generate_factory_countries import generate_factory_countries
from php.to_create_project.shared.countries.generate_route_countries import generate_route_countries
from php.to_create_project.shared.countries.generate_seeder_countries import generate_seeder_countries
from php.to_create_project.shared.migrations.generate_ability_groups_table import generate_ability_groups_table
from php.to_create_project.shared.migrations.generate_countries_table import generate_countries_table
from php.to_create_project.shared.migrations.generate_roles_table import generate_roles_table
from php.to_create_project.shared.migrations.update_create_users_table import update_create_users_table
from php.to_create_project.shared.role_users.generate_controller_role_users import generate_controller_role_users
from php.to_create_project.shared.role_users.generate_model_role_users import generate_model_role_users
from php.to_create_project.shared.role_users.generate_factory_role_users import generate_factory_role_users
from php.to_create_project.shared.role_users.generate_route_role_users import generate_route_role_users
from php.to_create_project.shared.role_users.generate_seeder_role_users import generate_seeder_role_users
from php.to_create_project.shared.roles.generate_controller_roles import generate_controller_roles
from php.to_create_project.shared.roles.generate_model_roles import generate_model_roles
from php.to_create_project.shared.roles.generate_repository_roles import generate_repository_roles
from php.to_create_project.shared.roles.generate_factory_roles import generate_factory_roles
from php.to_create_project.shared.roles.generate_seeder_roles import generate_seeder_roles
from php.to_create_project.shared.roles.generate_route_roles import generate_route_roles
from php.to_create_project.shared.update_database_seeders.update_database_seeders import update_database_seeder
from php.to_create_project.shared.user_statuses.generate_controller_user_statuses import generate_controller_user_statuses
from php.to_create_project.shared.user_statuses.generate_model_user_statuses import generate_model_user_statuses
from php.to_create_project.shared.user_statuses.generate_repository_user_statuses import generate_repository_user_statuses
from php.to_create_project.shared.user_statuses.generate_factory_user_statuses import generate_factory_user_statuses
from php.to_create_project.shared.user_statuses.generate_route_user_statuses import generate_route_user_statuses
from php.to_create_project.shared.user_statuses.generate_seeder_user_statuses import generate_seeder_user_statuses
from php.to_create_project.shared.user_roles_abilities.generate_seeder_user_roles_abilities import generate_seeder_user_roles_abilities




def generate_shared(full_path):

    # Abilities
    generate_controller_abilities(full_path)
    generate_model_abilities(full_path)
    generate_repository_abilities(full_path)
    generate_factory_abilities(full_path)
    generate_seeder_abilities(full_path)
    generate_route_abilities(full_path)


    # Abilities Groups
    generate_controller_ability_groups(full_path)
    generate_model_ability_groups(full_path)
    generate_repository_ability_groups(full_path)
    generate_factory_ability_groups(full_path)
    generate_seeder_ability_groups(full_path)
    generate_route_ability_groups(full_path)


    # Abilities Users
    generate_controller_ability_users(full_path)
    generate_model_ability_users(full_path)
    generate_repository_ability_users(full_path)
    generate_factory_ability_users(full_path)
    generate_seeder_ability_users(full_path)
    generate_route_ability_users(full_path)


    # Countries
    generate_controller_countries(full_path)
    generate_model_countries(full_path)
    generate_repository_countries(full_path)
    generate_factory_countries(full_path)
    generate_seeder_countries(full_path)
    generate_route_countries(full_path)


    # Role Users
    generate_controller_role_users(full_path)
    generate_model_role_users(full_path)
    generate_factory_role_users(full_path)
    generate_seeder_role_users(full_path)
    generate_seeder_role_users(full_path)
    generate_route_role_users(full_path)


    # Role
    generate_controller_roles(full_path)
    generate_model_roles(full_path)
    generate_repository_roles(full_path)
    generate_factory_roles(full_path)
    generate_seeder_roles(full_path)
    generate_route_roles(full_path)



    # User Statuses
    generate_controller_user_statuses(full_path)
    generate_model_user_statuses(full_path)
    generate_repository_user_statuses(full_path)
    generate_factory_user_statuses(full_path)
    generate_seeder_user_statuses(full_path)
    generate_route_user_statuses(full_path)


    # UserRolesAbilities
    generate_seeder_user_roles_abilities(full_path)


    # Update DatabaseSeeder
    update_database_seeder(full_path)

    # Migrations
    update_create_users_table(full_path)
    generate_ability_groups_table(full_path)
    generate_roles_table(full_path)
    generate_countries_table(full_path)