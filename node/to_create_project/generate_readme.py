import os
from helpers.helper_print import print_message, GREEN, CYAN


def generate_readme(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path)

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "readme.md")

    # Contenido por defecto
    content = r"""# Project

## Installation

```sh

npm init -y

npm i express                           // Express
npm i express-validator                 // Validator fields
npm i bcryptjs                          // Encriptar password

npm i dotenv                            // DotEnv
npm i cors                              // Cors

npm install sequelize mysql2            // ORM Sequelize
npm i jsonwebtoken                      // JSON webtoken

```

## Run Server

```sh

npm run dev
npm run db:connection                   // Test DB connection

```

## Opcional Handlebars

Fuente: https://github.com/pillarjs/hbs

```sh

npm install hbs

```
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


