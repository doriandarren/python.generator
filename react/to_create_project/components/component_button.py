import os
from helpers.helper_print import print_message, GREEN, CYAN

def generate_button(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Buttons")
    file_path = os.path.join(folder_path, "ThemedButton.jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""import classNames from "classnames";

export const ThemedButton = ({ children, type = "button", variant = "primary", onClick, className, disabled = false }) => {
  return (
    <button
      type={type}
      className={classNames(
        "py-2 px-4 w-full xl:w-32 xl:mr-3 rounded-md text-white font-semibold transition-all duration-200 cursor-pointer",
        {
          "bg-gray-400 cursor-not-allowed": disabled,
          "bg-primary hover:bg-primary-dark": !disabled && variant === "primary",
          "bg-danger hover:bg-danger-dark": !disabled && variant === "danger",
          "bg-secondary hover:bg-secondary-dark": !disabled && variant === "secondary",
          "bg-success hover:bg-success-dark": !disabled && variant === "success",
          "bg-info hover:bg-info-dark": !disabled && variant === "info",
          "bg-warning hover:bg-warning-dark": !disabled && variant === "warning",
        },
        className
      )}
      onClick={!disabled ? onClick : undefined}
      disabled={disabled}
    >
      {children}
    </button>
  );
};
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)