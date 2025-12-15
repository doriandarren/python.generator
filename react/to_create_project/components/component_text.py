import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_text(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Text")
    file_path = os.path.join(folder_path, "ThemedText.jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""export const ThemedText = ({
  className = "",
  type = "normal",
  children,
  ...rest
}) => {
  const baseClasses = "text-gray-700 mb-4";

  const typeClasses = {
    normal: "font-bold",
    h1: "text-3xl font-bold",
    h2: "text-2xl font-bold",
    link: "font-normal underline cursor-pointer hover:opacity-80",
  };

  return (
    <div
      className={[baseClasses, typeClasses[type], className].join(" ")}
      {...rest}
    >
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