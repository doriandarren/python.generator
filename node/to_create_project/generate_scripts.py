import os
from helpers.helper_print import print_message, GREEN, CYAN



def generate_scripts(full_path):

    create_db_alter(full_path)
    create_db_reset(full_path)
    create_test_connection(full_path)


def create_db_alter(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "scripts")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "dbAlter.js")

    # Contenido por defecto
    content = r"""// src/scripts/dbAlter.js
import sequelize from '../database/settings/config.js';
import User from '../models/User.js';



async function syncAlter() {
  try {
    await sequelize.authenticate();
    console.log('🔌 Conectado a la base de datos');

    await sequelize.sync({ alter: true }); // 🧠 solo aplica cambios
    console.log('✅ Estructura actualizada (sin perder datos)');

  } catch (error) {
    console.error('❌ Error al aplicar alter:', error);
  } finally {
    await sequelize.close();
  }
}

syncAlter();

"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_db_reset(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "scripts")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "dbReset.js")

    # Contenido por defecto
    content = r"""import sequelize from '../database/settings/config.js';
/**********
 * Models
 **********/
import '../models/UserStatus.js'; 
import '../models/User.js'; 
import '../models/Role.js'; 
import '../models/Ability.js'; 
import '../models/RoleUser.js'; 
import '../models/AbilityUser.js'; 


/**********
 * Relaciones entre modelos
 **********/
import '../models/initAssociations.js';


/**********
 * Seeders
 **********/
import { seedUsers } from '../database/seeders/users/userSeeder.js';
import { seedUserStatuses } from '../database/seeders/userStatuses/userStatusSeeder.js';
import { seedRoles } from '../database/seeders/roles/roleSeeder.js';



async function resetDatabase() {
  try {
    await sequelize.authenticate();
    console.log('🔌 Conectado a la base de datos');

    await sequelize.sync({ force: true });
    console.log('🧨 Base de datos restablecida');


    await seedUserStatuses();
    await seedRoles();

    await seedUsers();

    console.log('✅ Datos sembrados correctamente');


  } catch (error) {
    console.error('❌ Error al restablecer la base de datos:', error);
  } finally {
    await sequelize.close();
  }
}

resetDatabase();
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_test_connection(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    folder_path = os.path.join(full_path, "src", "scripts")

    # Crear la carpeta si no existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print_message(f"Carpeta creada: {folder_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(folder_path, "dbTestConnection.js")

    # Contenido por defecto
    content = r"""// testConnection.js
import sequelize from '../database/settings/config.js';

async function dbTestConnection() {
  try {
    await sequelize.authenticate();
    console.log('✅ Conexión exitosa a la base de datos');
  } catch (error) {
    console.error('❌ Error al conectar:', error);
  }
}

dbTestConnection();
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
