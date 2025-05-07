import os
from helpers.helper_print import print_message, GREEN, CYAN


def generate_helpers(full_path):
    create_sweetalert2(full_path)
    create_data_fake(full_path)
    create_toast(full_path)
    create_variant_class(full_path)





def create_sweetalert2(full_path):
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


def create_data_fake(full_path):
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
    file_path = os.path.join(styles_path, "helperDataFake.js")

    # Contenido por defecto
    content = """
export const dataHeaderFake = [
  { key: "name", label: "Name" },
  { key: "title", label: "Title" },
  { key: "email", label: "Email" },
  { key: "role", label: "Role" },
];

export const dataBodyFake = [
  { id: 1, name: "Amelia Jones", title: "Data Scientist", email: "amelia.jones@example.com", role: "Designer" },
  { id: 2, name: "Ava Williams", title: "Project Manager", email: "ava.williams@example.com", role: "Admin" },
  { id: 3, name: "Harper Moore", title: "Database Administrator", email: "harper.moore@example.com", role: "Member" },
  { id: 4, name: "Ava Hernandez", title: "Back-end Developer", email: "ava.hernandez@example.com", role: "Analyst" },
  { id: 5, name: "Noah Miller", title: "Project Manager", email: "noah.miller@example.com", role: "Tester" },
  { id: 6, name: "Liam Brown", title: "Scrum Master", email: "liam.brown@example.com", role: "Manager" },
  { id: 7, name: "Ethan Johnson", title: "Data Scientist", email: "ethan.johnson@example.com", role: "Designer" },
  { id: 8, name: "Lindsay Davis", title: "QA Engineer", email: "lindsay.davis@example.com", role: "Admin" },
  { id: 9, name: "Liam Davis", title: "Full-stack Developer", email: "liam.davis@example.com", role: "Manager" },
  { id: 10, name: "Mason Jackson", title: "Full-stack Developer", email: "mason.jackson@example.com", role: "Manager" },
  { id: 11, name: "Noah Moore", title: "DevOps Engineer", email: "noah.moore@example.com", role: "Tester" },
  { id: 12, name: "Mason Gonzalez", title: "Front-end Developer", email: "mason.gonzalez@example.com", role: "Member" },
  { id: 13, name: "Liam Martinez", title: "Full-stack Developer", email: "liam.martinez@example.com", role: "Manager" },
  { id: 14, name: "Amelia Brown", title: "Project Manager", email: "amelia.brown@example.com", role: "Member" },
  { id: 15, name: "Amelia Gonzalez", title: "Project Manager", email: "amelia.gonzalez@example.com", role: "Tester" },
  { id: 16, name: "Ethan Smith", title: "Project Manager", email: "ethan.smith@example.com", role: "Admin" },
  { id: 17, name: "Olivia Jones", title: "QA Engineer", email: "olivia.jones@example.com", role: "Tester" },
  { id: 18, name: "Amelia Garcia", title: "Back-end Developer", email: "amelia.garcia@example.com", role: "Manager" },
  { id: 19, name: "Logan Jones", title: "QA Engineer", email: "logan.jones@example.com", role: "Manager" },
  { id: 20, name: "Harper Gonzalez", title: "Data Scientist", email: "harper.gonzalez@example.com", role: "Manager" },
  { id: 21, name: "Noah Gonzalez", title: "Project Manager", email: "noah.gonzalez@example.com", role: "Tester" },
  { id: 22, name: "Lindsay Williams", title: "Scrum Master", email: "lindsay.williams@example.com", role: "Analyst" },
  { id: 23, name: "Aiden Williams", title: "System Architect", email: "aiden.williams@example.com", role: "Designer" },
  { id: 24, name: "Olivia Hernandez", title: "DevOps Engineer", email: "olivia.hernandez@example.com", role: "DevOps" },
  { id: 25, name: "Charlotte Rodriguez", title: "QA Engineer", email: "charlotte.rodriguez@example.com", role: "Admin" },
  { id: 26, name: "Liam Moore", title: "Back-end Developer", email: "liam.moore@example.com", role: "Manager" },
  { id: 27, name: "Lindsay Taylor", title: "DevOps Engineer", email: "lindsay.taylor@example.com", role: "Manager" },
  { id: 28, name: "Ava Walton", title: "Product Manager", email: "ava.walton@example.com", role: "DevOps" },
  { id: 29, name: "Liam Walton", title: "Data Scientist", email: "liam.walton@example.com", role: "Designer" },
  { id: 30, name: "Lucas Rodriguez", title: "Full-stack Developer", email: "lucas.rodriguez@example.com", role: "Tester" },
  { id: 31, name: "Olivia Miller", title: "Database Administrator", email: "olivia.miller@example.com", role: "DevOps" },
  { id: 32, name: "Aiden Gonzalez", title: "Back-end Developer", email: "aiden.gonzalez@example.com", role: "DevOps" },
  { id: 33, name: "Mia Taylor", title: "Full-stack Developer", email: "mia.taylor@example.com", role: "Designer" },
  { id: 34, name: "Harper Gonzalez", title: "Full-stack Developer", email: "harper.gonzalez@example.com", role: "Tester" },
  { id: 35, name: "Elijah Walton", title: "DevOps Engineer", email: "elijah.walton@example.com", role: "Tester" },
  { id: 36, name: "Ethan Walton", title: "Software Engineer", email: "ethan.walton@example.com", role: "Analyst" },
  { id: 37, name: "Mia Moore", title: "Software Engineer", email: "mia.moore@example.com", role: "Member" },
  { id: 38, name: "Ethan Martinez", title: "Database Administrator", email: "ethan.martinez@example.com", role: "DevOps" },
  { id: 39, name: "Aiden Wilson", title: "Software Engineer", email: "aiden.wilson@example.com", role: "Manager" },
  { id: 40, name: "Mia Rodriguez", title: "System Architect", email: "mia.rodriguez@example.com", role: "Member" },
  { id: 41, name: "Lindsay Jackson", title: "Front-end Developer", email: "lindsay.jackson@example.com", role: "Admin" },
  { id: 42, name: "Caden Williams", title: "DevOps Engineer", email: "caden.williams@example.com", role: "Admin" },
  { id: 43, name: "Noah Johnson", title: "System Architect", email: "noah.johnson@example.com", role: "Member" },
  { id: 44, name: "Ethan Miller", title: "System Architect", email: "ethan.miller@example.com", role: "Manager" },
  { id: 45, name: "Lindsay Garcia", title: "Back-end Developer", email: "lindsay.garcia@example.com", role: "Analyst" },
  { id: 46, name: "Mia Jones", title: "Project Manager", email: "mia.jones@example.com", role: "Designer" },
  { id: 47, name: "James Gonzalez", title: "Project Manager", email: "james.gonzalez@example.com", role: "Manager" },
  { id: 48, name: "Aiden Wilson", title: "System Architect", email: "aiden.wilson@example.com", role: "Tester" },
  { id: 49, name: "Olivia Garcia", title: "Cybersecurity Specialist", email: "olivia.garcia@example.com", role: "Analyst" },
  { id: 50, name: "Elijah Walton", title: "DevOps Engineer", email: "elijah.walton@example.com", role: "Tester" },
  { id: 51, name: "Ethan Walton", title: "Software Engineer", email: "ethan.walton@example.com", role: "Analyst" },
  { id: 52, name: "Mia Moore", title: "Software Engineer", email: "mia.moore@example.com", role: "Member" },
  { id: 53, name: "Ethan Martinez", title: "Database Administrator", email: "ethan.martinez@example.com", role: "DevOps" },
  { id: 54, name: "Aiden Wilson", title: "Software Engineer", email: "aiden.wilson@example.com", role: "Manager" },
  { id: 55, name: "Mia Rodriguez", title: "System Architect", email: "mia.rodriguez@example.com", role: "Member" },
  { id: 56, name: "Lindsay Jackson", title: "Front-end Developer", email: "lindsay.jackson@example.com", role: "Admin" },
  { id: 57, name: "Caden Williams", title: "DevOps Engineer", email: "caden.williams@example.com", role: "Admin" },
  { id: 58, name: "Noah Johnson", title: "System Architect", email: "noah.johnson@example.com", role: "Member" },
  { id: 59, name: "Ethan Miller", title: "System Architect", email: "ethan.miller@example.com", role: "Manager" },
  { id: 60, name: "Lindsay Garcia", title: "Back-end Developer", email: "lindsay.garcia@example.com", role: "Analyst" },
  { id: 61, name: "Mia Jones", title: "Project Manager", email: "mia.jones@example.com", role: "Designer" },
  { id: 62, name: "James Gonzalez", title: "Project Manager", email: "james.gonzalez@example.com", role: "Manager" },
  { id: 63, name: "Aiden Wilson", title: "System Architect", email: "aiden.wilson@example.com", role: "Tester" },
  { id: 64, name: "Olivia Garcia", title: "Cybersecurity Specialist", email: "olivia.garcia@example.com", role: "Analyst" },
  { id: 65, name: "Charlotte Johnson", title: "UI/UX Designer", email: "charlotte.johnson@example.com", role: "Admin" }
];

"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_toast(full_path):
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
    file_path = os.path.join(styles_path, "helperToast.js")

    # Contenido
    content = """import Swal from \"sweetalert2\";

export const Toast = async (text, icon = \'success\') => {
  Swal.fire({
    toast: true,
    icon: icon,
    title: text,
    position: \'top-end\',
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.addEventListener(\'mouseenter\', Swal.stopTimer)
      toast.addEventListener(\'mouseleave\', Swal.resumeTimer)
    }
  });
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)



def create_variant_class(full_path):
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
    file_path = os.path.join(styles_path, "helperVariantClass.js")

    # Contenido
    content = """export const getVariantTextClass = (variant = "neutral") => {
  return (
    {
      neutral: "text-neutral",
      special_price: "text-special-price",
      danger: "text-danger",
      warning: "text-warning",
      success: "text-success",
      info: "text-info",
      primary: "text-primary",
      secondary: "text-secondary",
    }[variant] || "text-neutral"
  );
};

export const getVariantBgClass = (variant = "neutral") => {
  return (
    {
      neutral: "bg-neutral",
      special_price: "bg-special-price",
      danger: "bg-danger",
      warning: "bg-warning",
      success: "bg-success",
      info: "bg-info",
      primary: "bg-primary",
      secondary: "bg-secondary",
    }[variant] || "bg-neutral"
  );
};
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)