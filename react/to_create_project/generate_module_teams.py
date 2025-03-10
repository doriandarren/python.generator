import os
from .utils import print_message, GREEN, CYAN, run_command, create_folder





def generate_module_teams(project_path):
    create_routes(project_path)
    create_team_page(project_path)


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
import { TeamPage } from "../pages/TeamPage";


export const TeamRoutes = () => {
  return (
    <Routes>

      <Route path="/" element={<TeamPage />} />
      
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


def create_team_page(project_path):
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
import { dataBodyFake, dataHeaderFake } from "../../../helpers/helperDataFake";
import { useTranslation } from "react-i18next";
import { Button } from "../../../components/Buttons/Button";

// Header
const columns = dataHeaderFake;

// Data
const data = dataBodyFake;


// Edit and Delete
const handleEdit = (id) => alert(`Editando usuario con ID: ${id}`);
const handleDelete = (id) => alert(`Eliminando usuario con ID: ${id}`);


export const TeamPage = () => {

  const navigate = useNavigate();
  const { t } = useTranslation();


  const onButtonClick = (e) => {
    e.preventDefault();
    navigate("/admin/team/create");
  }


  return (
    <SessionLayout>

      <div className="flex items-center justify-between">

        <div className="pt-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">{ t("team") }</h2>
        </div>

        {/* Header con botón dinámico */}
        <div className="sm:flex sm:items-center">
            <div className="mt-4 sm:mt-0  sm:flex-none">
              <Button
                type="button"
                onClick={onButtonClick}
              >
                Nuevo
              </Button>
            </div>
        </div>
      </div>


      <Datatable
        columns={columns}
        data={data}
        editPath="/users"
        onEdit={handleEdit}
        onDelete={handleDelete}
      />

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