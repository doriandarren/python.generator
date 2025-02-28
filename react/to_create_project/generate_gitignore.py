import os
from .utils import print_message, GREEN, CYAN, run_command



def generate_gitignore(full_path):
    create_gitignore(full_path)


def create_gitignore(project_path):
    """
    Genera el archivo
    """
    file_path = os.path.join(project_path, ".gitignore")


    # Contenido del archivo
    content = """# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# local env files
.env*.local

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
.vscode
.env
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")
