#!/usr/bin/env python3
import sys
from importlib import import_module


COMMANDS = {
    # nombre_comando: ruta_del_módulo
    "music": "ai.cronjobs.music.cronjob_music",
    "music": "ai.cronjobs.music.cronjob_music",
    # aquí puedes añadir más cronjobs:
    # "emails": "ai.cronjobs.emails.cronjob_emails",
}


def main() -> int:
    if len(sys.argv) < 2:
        print("Uso: python run.py <comando>")
        print("Comandos disponibles:", ", ".join(COMMANDS.keys()))
        return 1

    cmd = sys.argv[1].lower()

    module_path = COMMANDS.get(cmd)
    if not module_path:
        print(f"Comando no reconocido: {cmd}")
        print("Comandos disponibles:", ", ".join(COMMANDS.keys()))
        return 1

    # Importa el módulo y ejecuta su main() si existe
    mod = import_module(module_path)

    if hasattr(mod, "main") and callable(mod.main):
        return int(mod.main())

    # Si no hay main(), simplemente lo importa (y se ejecuta lo que tenga al nivel global)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
