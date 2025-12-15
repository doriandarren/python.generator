import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_cards(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Cards")
    file_path = os.path.join(folder_path, "ThemedCard.jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""export const ThemedCard = ({ className = "", variant = "default", children }) => {
  const baseClasses = "mx-auto bg-white rounded-lg shadow-lg p-6";

  const variantClasses = {
    default: "",
    form: "max-w-4xl",       // para create/edit
    info: "border border-gray-200",
    stats: "bg-gradient-to-r from-indigo-500 to-purple-500 text-white",
  };

  return (
    <div className={[baseClasses, variantClasses[variant], className].join(" ")}>
      {children}
    </div>
  );
};
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)