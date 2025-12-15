import os
from helpers.helper_print import create_folder




def generate_module_profile(project_path):

    create_routes(project_path)
    create_profile_page(project_path)



def create_routes(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", "profile", "routes")
    file_path = os.path.join(routes_dir, "ProfileRoutes.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo jsx
    content = """import { Navigate, Route, Routes } from "react-router";
import { ProfilePage } from "../pages/ProfilePage";


export const ProfileRoutes = () => {
  return (
    <Routes>
      
      <Route path="/" element={ <ProfilePage /> } />
      
      
      <Route path="/*" element={ <Navigate to="/auth/dashboard" /> } />
      
    </Routes>
  )
}

"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")


def create_profile_page(project_path):
    """
    Genera el archivo jsx dentro de la carpeta modules/dashboard/pages.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "profile", "pages")
    file_path = os.path.join(pages_dir, "ProfilePage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    content = """import { useTranslation } from "react-i18next"
import { useState } from "react";
import Swal from "sweetalert2";
import { SessionLayout } from "../../../layouts/private/SessionLayout"
import { ThemedButton } from "../../../components/Buttons/ThemedButton";


const dataForm = {
  name: "",
  title: "",
  email: "",
  role: "",
};

export const ProfilePage = () => {

  const {t} = useTranslation();

  const [formData, setFormData] = useState(dataForm);
  
  // Manejar cambios en el formulario
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const onSubmit = (e) => {
    e.preventDefault();
    // TODO: implements
    //navigate("/admin/profile");
    Swal.fire("Registro guardado correctamente", "Registro guardado", "success")
  };



  return (
    <SessionLayout>
      <div>
        <h2 className="text-2xl font-semibold text-gray-700 mb-4">
          { t("profile") }
        </h2>
      </div>

      <div className="mx-auto p-6 bg-white rounded-lg shadow-lg">

        <form onSubmit={onSubmit} className="space-y-4">

          <div>
            <label className="block text-gray-700">Nombre</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              className="w-full p-2 border border-gray-300 rounded-md"
            />
          </div>

          <div>
            <label className="block text-gray-700">Título</label>
            <input
              type="text"
              name="title"
              value={formData.title}
              onChange={handleChange}
              required
              className="w-full p-2 border border-gray-300 rounded-md"
            />
          </div>

          <div>
            <label className="block text-gray-700">Correo Electrónico</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              className="w-full p-2 border border-gray-300 rounded-md"
            />
          </div>

          <div>
            <label className="block text-gray-700">Rol</label>
            <select
              name="role"
              value={formData.role}
              onChange={handleChange}
              required
              className="w-full p-2 border border-gray-300 rounded-md"
            >
              <option value="">Selecciona un rol</option>
              <option value="Admin">Admin</option>
              <option value="Manager">Manager</option>
              <option value="User">User</option>
            </select>
          </div>

          <div className="flex justify-end items-end mt-7">
            <ThemedButton 
              type="submit"
            >
              {t("save")}
            </ThemedButton>
          </div>

        </form>
      </div>
      
    </SessionLayout>
  )
}
"""
    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")



