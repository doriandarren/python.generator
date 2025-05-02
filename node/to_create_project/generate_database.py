import os
from helpers.helper_print import print_message, GREEN, CYAN


def generate_database(full_path):
    create_seeder_roles(full_path)
    create_users(full_path)
    create_user_statuses(full_path)

    ## Settings
    create_settings(full_path)


def create_seeder_roles(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "database", "seeders", "roles")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "roleSeeder.js")

    # Contenido por defecto
    content = r"""import { EnumRole } from '../../../enums/enumRole.js';
import Role from '../../../models/Role.js';


export const seedRoles = async () => { 
  const roles = [
    {
      id: EnumRole.ADMIN_ID,
      name: EnumRole.ADMIN,
      description: EnumRole.ADMIN_DESCRIPTION,
    },
    {
      id: EnumRole.MANAGER_ID,
      name: EnumRole.MANAGER,
      description: EnumRole.MANAGER_DESCRIPTION,
    },
    {
      id: EnumRole.USER_ID,
      name: EnumRole.USER,
      description: EnumRole.USER_DESCRIPTION,
    },
    {
      id: EnumRole.ERP_ID,
      name: EnumRole.ERP,
      description: EnumRole.ERP_DESCRIPTION,
    },
  ];

  for (const role of roles) {
    const exists = await Role.findOne({ where: { id: role.id } });

    if (!exists) {
      await Role.create(role);
      console.log(`🟢 Rol "${role.name}" creado`);
    } else {
      console.log(`⚠️ Rol "${role.name}" ya existe`);
    }
  }

  console.log('🌱 Roles insertados correctamente');
};
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_users(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "database", "seeders", "users")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "userSeeder.js")

    # Contenido por defecto
    content = r"""import RoleUser from "../../../models/RoleUser.js";
import { EnumRole } from "../../../enums/enumRole.js";
import { EnumUserStatus } from "../../../enums/enumUserStatuses.js";
import User from "../../../models/User.js";
import bcrypt from "bcryptjs";
import UserStatus from "../../../models/UserStatus.js";
import Role from "../../../models/Role.js";


export const seedUsers = async () => {

  const salt = bcrypt.genSaltSync();

  const usersToCreate = [
    {
      name: 'Dorian',
      email: 'doriandarren1@gmail.com',
      password: 'Splytin2024',
      role: EnumRole.ADMIN,
      image_url: 'https://i.pravatar.cc/150?img=2'
    },
    {
      name: 'Milena',
      email: 'darimile@gmail.com',
      password: 'Splytin2024',
      role: EnumRole.ADMIN,
      image_url: 'https://i.pravatar.cc/150?img=1'
    },
    {
      name: 'Dilan',
      email: 'dilandarren@gmail.com',
      password: 'Splytin2024',
      role: EnumRole.ADMIN,
      image_url: 'https://i.pravatar.cc/150?img=3'
    },
    {
      name: 'Dariana',
      email: 'dorianadamiled@gmail.com',
      password: 'Splytin2024',
      role: EnumRole.ADMIN,
      image_url: 'https://i.pravatar.cc/150?img=4'
    },
    {
      name: 'Max',
      email: 'max16506@gmail.com',
      password: 'Splytin2024',
      role: EnumRole.ADMIN,
      image_url: 'https://i.pravatar.cc/150?img=5'
    },
    {
      name: 'Manager',
      email: 'manager@splytin.com',
      password: 'Splytin2024',
      role: EnumRole.MANAGER,
      image_url: 'https://i.pravatar.cc/150?img=6'
    },
    {
      name: 'User',
      email: 'user@splytin.com',
      password: 'Splytin2024',
      role: EnumRole.USER,
      image_url: 'https://i.pravatar.cc/150?img=7'
    }

  ];

  const userStatus = await UserStatus.findOne({ where: { name: EnumUserStatus.STATUS_ACTIVE_NAME } });

  if (!userStatus) {
    console.error('❌ Estado de usuario ACTIVO no encontrado');
    return;
  }

  for (const item of usersToCreate) {
    // Crear o encontrar usuario
    let user = await User.findOne({ where: { email: item.email } });

    if (!user) {
      user = await User.create({
        name: item.name,
        email: item.email,
        password: bcrypt.hashSync(item.password, salt),
        email_verified_at: new Date(),
        image_url: item.image_url,
        remember_token: null,
        user_status_id: userStatus.id,
      });
      console.log(`🟢 Usuario "${item.email}" creado`);
    } else {
      console.log(`⚠️ Usuario "${item.email}" ya existe`);
    }

    // Buscar rol
    const role = await Role.findOne({ where: { name: item.role.toLowerCase() } });

    if (!role) {
      console.warn(`⚠️ Rol "${item.role}" no existe`);
      continue;
    }

    // Asignar rol si no lo tiene
    const hasRole = await RoleUser.findOne({
      where: { user_id: user.id, role_id: role.id }
    });

    if (!hasRole) {
      await RoleUser.create({ user_id: user.id, role_id: role.id });
      console.log(`✅ Rol "${item.role}" asignado a ${item.email}`);
    } else {
      console.log(`🔁 ${item.email} ya tiene el rol "${item.role}"`);
    }
  }

  console.log('🌱 Usuarios con roles insertados correctamente');

};
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_user_statuses(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "database", "seeders", "userStatuses")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "userStatusSedder.js")

    # Contenido por defecto
    content = r"""import RoleUser from "../../../models/RoleUser.js";
import { EnumRole } from "../../../enums/enumRole.js";
import { EnumUserStatus } from "../../../enums/enumUserStatuses.js";
import User from "../../../models/User.js";
import bcrypt from "bcryptjs";
import UserStatus from "../../../models/UserStatus.js";
import Role from "../../../models/Role.js";


export const seedUsers = async () => {

  const salt = bcrypt.genSaltSync();

  const usersToCreate = [
    {
      name: 'Dorian',
      email: 'doriandarren1@gmail.com',
      password: 'Splytin2024',
      role: EnumRole.ADMIN,
      image_url: 'https://i.pravatar.cc/150?img=2'
    },
    {
      name: 'Milena',
      email: 'darimile@gmail.com',
      password: 'Splytin2024',
      role: EnumRole.ADMIN,
      image_url: 'https://i.pravatar.cc/150?img=1'
    },
    {
      name: 'Dilan',
      email: 'dilandarren@gmail.com',
      password: 'Splytin2024',
      role: EnumRole.ADMIN,
      image_url: 'https://i.pravatar.cc/150?img=3'
    },
    {
      name: 'Dariana',
      email: 'dorianadamiled@gmail.com',
      password: 'Splytin2024',
      role: EnumRole.ADMIN,
      image_url: 'https://i.pravatar.cc/150?img=4'
    },
    {
      name: 'Max',
      email: 'max16506@gmail.com',
      password: 'Splytin2024',
      role: EnumRole.ADMIN,
      image_url: 'https://i.pravatar.cc/150?img=5'
    },
    {
      name: 'Manager',
      email: 'manager@splytin.com',
      password: 'Splytin2024',
      role: EnumRole.MANAGER,
      image_url: 'https://i.pravatar.cc/150?img=6'
    },
    {
      name: 'User',
      email: 'user@splytin.com',
      password: 'Splytin2024',
      role: EnumRole.USER,
      image_url: 'https://i.pravatar.cc/150?img=7'
    }

  ];

  const userStatus = await UserStatus.findOne({ where: { name: EnumUserStatus.STATUS_ACTIVE_NAME } });

  if (!userStatus) {
    console.error('❌ Estado de usuario ACTIVO no encontrado');
    return;
  }

  for (const item of usersToCreate) {
    // Crear o encontrar usuario
    let user = await User.findOne({ where: { email: item.email } });

    if (!user) {
      user = await User.create({
        name: item.name,
        email: item.email,
        password: bcrypt.hashSync(item.password, salt),
        email_verified_at: new Date(),
        image_url: item.image_url,
        remember_token: null,
        user_status_id: userStatus.id,
      });
      console.log(`🟢 Usuario "${item.email}" creado`);
    } else {
      console.log(`⚠️ Usuario "${item.email}" ya existe`);
    }

    // Buscar rol
    const role = await Role.findOne({ where: { name: item.role.toLowerCase() } });

    if (!role) {
      console.warn(`⚠️ Rol "${item.role}" no existe`);
      continue;
    }

    // Asignar rol si no lo tiene
    const hasRole = await RoleUser.findOne({
      where: { user_id: user.id, role_id: role.id }
    });

    if (!hasRole) {
      await RoleUser.create({ user_id: user.id, role_id: role.id });
      console.log(`✅ Rol "${item.role}" asignado a ${item.email}`);
    } else {
      console.log(`🔁 ${item.email} ya tiene el rol "${item.role}"`);
    }
  }

  console.log('🌱 Usuarios con roles insertados correctamente');

};
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_settings(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "database", "settings")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "config.js")

    # Contenido por defecto
    content = r"""// database.js
import { Sequelize } from 'sequelize';
import dotenv from 'dotenv';


dotenv.config();

const sequelize = new Sequelize(process.env.DB_DATABASE, process.env.DB_USER, process.env.DB_PASSWORD, {
  host: process.env.DB_HOST,
  dialect: 'mysql',
});

export default sequelize;
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
