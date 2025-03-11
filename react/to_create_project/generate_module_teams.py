import os
from .utils import print_message, GREEN, CYAN, run_command, create_folder



def generate_module_teams(project_path):
    create_routes(project_path)
    create_list_page(project_path)
    create_create_page(project_path)
    create_edit_page(project_path)
    create_barrel_file(project_path)

    ## Service
    create_service_file(project_path)



def create_routes(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", "teams", "routes")
    file_path = os.path.join(routes_dir, "TeamRoutes.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo jsx
    content = """import { Navigate, Route, Routes } from "react-router";
import { TeamPage, TeamCreatePage, TeamEditPage } from "../pages";

export const TeamRoutes = () => {
  return (
    <Routes>
    
      <Route path="/" element={<TeamPage />} />
      <Route path="create" element={<TeamCreatePage />} />
      <Route path=":id/edit" element={<TeamEditPage />} />
      
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


def create_list_page(project_path):
    """
    Genera el archivo jsx
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "teams", "pages")
    file_path = os.path.join(pages_dir, "TeamPage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    content = """import { SessionLayout } from "../../../layouts/private/SessionLayout";
import { Datatable } from "../../../components/DataTables/DataTable";
import { useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import { Button } from "../../../components/Buttons/Button";
import { useEffect, useState } from "react";
import { getTeams } from "../services/teamService"; // Importa la función correcta
import { dataHeaderFake } from "../../../helpers/helperDataFake"; // Mantiene solo el header, sin datos fake

export const TeamPage = () => {
  const navigate = useNavigate();
  const { t } = useTranslation();
  const [data, setData] = useState([]); // Estado para almacenar los datos reales
  const [loading, setLoading] = useState(true); // Estado de carga

  useEffect(() => {
    const fetchTeams = async () => {
      setLoading(true);
      try {
        const response = await getTeams();
        //console.log("🚀 Datos de la API:", response);

        if (Array.isArray(response.data)) {
          setData(response.data);
          //setData([]);
        } else {
          console.warn("⚠️ La API no devolvió un array:", response);
        }
      } catch (error) {
        console.error("🚨 Error al obtener los equipos:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  const handleEdit = (id) => alert(`Editando usuario con ID: ${id}`);
  const handleDelete = (id) => alert(`Eliminando usuario con ID: ${id}`);

  const onButtonClick = (e) => {
    e.preventDefault();
    navigate("/admin/teams/create");
  };

  return (
    <SessionLayout>
      <div className="flex items-center justify-between mb-5">
        <div className="mt-1">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">{t("teams")}</h2>
        </div>

        <div className="sm:flex sm:items-center">
          <div className="mt-4 sm:mt-0 sm:flex-none">
            <Button type="button" onClick={onButtonClick}>
              {t("add")}
            </Button>
          </div>
        </div>
      </div>

      {loading ? (
        <p className="text-center text-gray-600">Cargando equipos...</p>
      ) : (
        <Datatable
          columns={dataHeaderFake}
          data={data}
          editPath="/admin/teams"
          onEdit={handleEdit}
          onDelete={handleDelete}
        />
      )}
    </SessionLayout>
  );
};
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")



def create_create_page(project_path):
    """
    Genera el archivo jsx
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "teams", "pages")
    file_path = os.path.join(pages_dir, "TeamCreatePage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    content = """import { useTranslation } from "react-i18next"
import { SessionLayout } from "../../../layouts/private/SessionLayout"
import { useState } from "react";
import { Button } from "../../../components/Buttons/Button";
import Swal from "sweetalert2";
import { useNavigate } from "react-router-dom";


const dataForm = {
  name: "",
  title: "",
  email: "",
  role: "",
};

export const TeamCreatePage = () => {

  const { t } = useTranslation();
  const navigate = useNavigate();

  const [formData, setFormData] = useState(dataForm);
  
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

  const onClickCancel = (e) => {
    e.preventDefault();
    navigate("/admin/teams");
  }



  return (
    <SessionLayout>
      <div>
        <h2 className="text-2xl font-semibold text-gray-700 mb-4">
          { t("teams") }
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

          <div className="flex justify-center items-end mt-7">
            <Button 
              type="submit"
            >
              { t("save") }
            </Button>

            <Button
              variant="danger"
              onClick={onClickCancel}
            >
              { t("cancel") }
            </Button>

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


def create_edit_page(project_path):
    """
    Genera el archivo jsx
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "teams", "pages")
    file_path = os.path.join(pages_dir, "TeamEditPage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    content = """import { useTranslation } from "react-i18next"
import { SessionLayout } from "../../../layouts/private/SessionLayout"
import { useState } from "react";
import { Button } from "../../../components/Buttons/Button";
import Swal from "sweetalert2";
import { useNavigate } from "react-router-dom";


const dataForm = {
  name: "",
  title: "",
  email: "",
  role: "",
};

export const TeamEditPage = () => {

  const { t } = useTranslation();
  const navigate = useNavigate();

  const [formData, setFormData] = useState(dataForm);
  
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

  const onClickCancel = (e) => {
    e.preventDefault();
    navigate("/admin/teams");
  }



  return (
    <SessionLayout>
      <div>
        <h2 className="text-2xl font-semibold text-gray-700 mb-4">
          { t("teams") }
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

          <div className="flex justify-center items-end mt-7">
            <Button 
              type="submit"
            >
              { t("save") }
            </Button>

            <Button
              variant="danger"
              onClick={onClickCancel}
            >
              { t("cancel") }
            </Button>

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


def create_barrel_file(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", "teams", "pages")
    file_path = os.path.join(routes_dir, "index.js")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo
    content = """export * from './TeamPage';
export * from './TeamCreatePage';
export * from './TeamEditPage';
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")



def create_service_file(project_path):
    """
    Genera el archivo jsx
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", "teams", "services")
    file_path = os.path.join(pages_dir, "teamService.js")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido de file
    content = """import { api } from "../../../api/api";

export const getTeams = async () => {
    try {
        const token = localStorage.getItem("token_portuarios");
        if (!token) {
            console.warn("No hay token disponible en localStorage");
            return [];
        }

        const response = await api("teams/list", "GET", null, token);

        // Verificar si la API devuelve datos válidos
        if (!response || typeof response !== "object") {
            console.error("Respuesta no válida de la API:", response);
            return [];
        }

        return response;
    } catch (error) {
        console.error("Error al obtener los equipos:", error);
        return [];
    }
};
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")
