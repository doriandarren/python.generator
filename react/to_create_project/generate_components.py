import os
from .utils import print_message, GREEN, CYAN, run_command




def generate_components(full_path):

    generate_button(full_path, "Button.jsx")
    generate_section(full_path, "Section.jsx")





def generate_button(full_path, file_name):
    """
    Genera un archivo CSS en la carpeta src/styles.

    Args:
        full_path (str): Ruta completa del proyecto.
        file_name (str): Nombre del archivo a generar (por defecto, 'globals.css').
    """
    styles_path = os.path.join(full_path, "src", "layouts", "components")

    # Crear la carpeta src/styles si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, file_name)

    # Contenido por defecto
    content = """import classNames from "classnames";

export const Button = ({children, type="button", variant="primary", onClick, className, disabled}) => {
  return (
    <button
        type={type}
        className={classNames("btn", `btn--${variant}`, className, { "btn--disabled": disabled })}
        onClick={onClick}
        disabled={disabled}
    >
        {children}
    </button>
  )
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)




def generate_section(full_path, file_name):
    """
    Genera un archivo CSS en la carpeta src/styles.

    Args:
        full_path (str): Ruta completa del proyecto.
        file_name (str): Nombre del archivo a generar (por defecto, 'globals.css').
    """
    styles_path = os.path.join(full_path, "src", "layouts", "components")

    # Crear la carpeta src/styles si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, file_name)

    # Contenido por defecto
    content = """import classNames from "classnames";

export const Section = ({title, subtitle, className, children}) => {
  return (
    <section className={classNames("section", className)}>
        <div className="section__container">
        {title && <h2 className="section__heading">{title}</h2>}
        {subtitle && <p className="section__subtitle">{subtitle}</p>}
        {children}
        </div>
    </section>
  )
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
