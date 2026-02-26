import os


def generate_readme(full_path):
    create_readme(full_path)


def create_readme(project_path):
    """
    Genera el archivo
    """
    file_path = os.path.join(project_path, "README.md")


    # Contenido del archivo
    content = """# Project

## Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")
