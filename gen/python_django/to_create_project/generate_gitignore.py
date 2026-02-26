import os
from gen.helpers.helper_print import print_message, GREEN, CYAN


def generate_gitignore(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path)
    file_path = os.path.join(folder_path, ".gitignore")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Virtualenvs
env/
venv/
ENV/
VENV/
venv.bak/
env.bak/
python_env/
python_venv/
myenv/

# Environments / dotenv
.env
/.env
.env.*
*.env

# Django
db.sqlite3
*.sqlite3
*.sqlite3-journal

# Django uploads + static build
media/
staticfiles/

# Logs
logs/
log/
*.log

# Cache / sessions / celery / redis
.cache/
*.pid
celerybeat-schedule
celerybeat.pid
dump.rdb

# Distribution / packaging
build/
dist/
downloads/
eggs/
.eggs/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
wheels/
share/python-wheels/

# PyInstaller
*.manifest
*.spec

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
coverage.xml
*.cover
.hypothesis/
.pytest_cache/
nosetests.xml

# Jupyter Notebook
.ipynb_checkpoints/

# Type checkers
.mypy_cache/

# IDEs
.idea/
.vscode/

# macOS
.DS_Store

# Frontend (optional)
node_modules/

# Temp files
*.swp
*.swo
*~
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)