import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_section(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Sections")
    file_path = os.path.join(folder_path, "ThemedSection.jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""import classNames from "classnames";

export const ThemedSection = ({ title, subtitle, className, children }) => {
  return (
    <section className={classNames("section", className)}>
      <div className="section__container">
        {title && <h2 className="section__heading">{title}</h2>}
        {subtitle && <p className="section__subtitle">{subtitle}</p>}
        {children}
      </div>
    </section>
  );
};
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)