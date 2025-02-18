import os
from .utils import print_message, GREEN, CYAN, run_command


def generate_helpers(full_path):
    generate_helper_sweetalert2(full_path)



def generate_helper_sweetalert2(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "src", "helpers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "helperSwal.js")

    # Contenido por defecto
    content = """import Swal from "sweetalert2";
 
/* USE:    
const handleError = () => {
    showErrorAlert("Ocurrió un error inesperado");
};

const handleConfirm = async () => {
    const confirmed = await showConfirmDialog("¿Seguro que quieres continuar?");
    if (confirmed) {
      showSuccessAlert("Acción confirmada");
    }
};
*/

export const showSuccessAlert = (message) => {
  Swal.fire({
    title: "¡Éxito!",
    text: message,
    icon: "success",
    confirmButtonText: "OK",
  });
};

export const showErrorAlert = (message) => {
  Swal.fire({
    title: "¡Error!",
    text: message,
    icon: "error",
    confirmButtonText: "OK",
  });
};

export const showConfirmDialog = async (message) => {
  const result = await Swal.fire({
    title: "¿Estás seguro?",
    text: message,
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Sí, continuar",
    cancelButtonText: "Cancelar",
  });
  return result.isConfirmed;
};
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

