import os
from helpers.helper_print import create_folder



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
      <Route path="edit/:id" element={<TeamEditPage />} />
      
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
import { deleteTeam, getTeams } from "../services/teamService";
import Swal from "sweetalert2";
import { Toast } from "../../../helpers/helperToast";
import { Preloader } from "../../../components/Preloader/Preloader";


export const TeamPage = () => {
  const navigate = useNavigate();
  const { t } = useTranslation();
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);


  const dataHeader = [
    { key: "name", label: t("name") },
    { key: "transporeon_code", label: t("transporeon_code") },
    { key: "msoft_code", label: t("msoft_code") },
  ];


  useEffect(() => {
    const fetchApi = async () => {
      setLoading(true);

      try {
        const response = await getTeams();
        const { data } = response;

        //console.log("Datos de la API:", data[0]);

        if (Array.isArray(data)) {
          setData(data);
          //setData([]);
        } else {
          console.warn("La API no devolvió un array:", response);
        }
      } catch (error) {
        console.error("Error al obtener los equipos:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchApi();
  }, []);


  const onDeleteClick = async (id, description = "") => {
    Swal.fire({
      icon: "warning",
      title: t("message.are_you_sure"),
      text: t("delete") + (description !== "" ? ": " + description : ""),
      showCancelButton: true,
      confirmButtonText: t("delete"),
      cancelButtonText: t("cancel"),
      confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_SUCCESS,
    }).then(async (result) => {
      if (result.isConfirmed) {
        try {
          const response = await deleteTeam(id);
          const { success, errors } = response;
  
          if (success) {
            // Eliminando el registro de la tabla sin recargar la página
            setData((prevData) => prevData.filter((item) => item.id !== id));
            await Toast(t("message.record_deleted"), "success");
          } else {
            await Toast(errors?.[0]?.e || t("message.error_deleting"), "error");
          }
        } catch (error) {
          console.error("Error al eliminar el registro:", error);
          await Toast(t("message.error_deleting"), "error");
        }
      }
    });
  };

  const onAddClick = (e) => {
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
            <Button type="button" onClick={onAddClick}>
              {t("add")}
            </Button>
          </div>
        </div>
      </div>

      {loading ? (
        <Preloader />
      ) : (
        <Datatable
          columns={dataHeader}
          data={data}
          editPath="/admin/teams"
          onDelete={onDeleteClick}
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
    content = """import { useTranslation } from "react-i18next";
import { SessionLayout } from "../../../layouts/private/SessionLayout";
import { Button } from "../../../components/Buttons/Button";
import Swal from "sweetalert2";
import { useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import { createTeam } from "../services/teamService";





export const TeamCreatePage = () => {
  const { t } = useTranslation();
  const navigate = useNavigate();
  
  // Schema 
  const schema = yup.object().shape({
    name: yup.string().required(t("form.required")),
    transporeon_code: yup.string().required(t("form.required")),
    msoft_code: yup.string().required(t("form.required")),
  });

  // react-hook-form con Yup
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({ resolver: yupResolver(schema) });

  
  const onSubmit = async(data) => {
    try {
      console.log("Datos enviados:", data);
      
      const response = await createTeam(data);
  
      if (response) {
        Swal.fire("Registro guardado correctamente", "Registro guardado", "success").then(() => {
          navigate("/admin/teams");
        });
      } else {
        Swal.fire("Error", "No se pudo guardar el registro", "error");
      }
    } catch (error) {
      console.error("Error al enviar los datos:", error);
      Swal.fire("Error", "Hubo un problema al guardar el registro", "error");
    }
  };

  const onClickCancel = (e) => {
    e.preventDefault();
    navigate("/admin/teams");
  };

  return (
    <SessionLayout>
      <div>
        <h2 className="text-2xl font-semibold text-gray-700 mb-4">
          { t("add") }
        </h2>
      </div>

      <div className="mx-auto p-6 bg-white rounded-lg shadow-lg">
        <form onSubmit={handleSubmit(onSubmit)} className="grid grid-cols-12 gap-6">

          {/* Nombre */}
          <div className="col-span-12 md:col-span-6 lg:col-span-4">
            <label className="block text-gray-700">{t("name")}</label>
            <input
              type="text"
              {...register("name")}
              className={`w-full p-2 border ${
                errors.name ? "border-danger" : "border-gray-300"
              } rounded-md`}
            />
            {errors.name && <p className="text-danger text-sm">{errors.name.message}</p>}
          </div>

          {/* Código Transporeon */}
          <div className="col-span-12 md:col-span-6 lg:col-span-4">
            <label className="block text-gray-700">{t("transporeon_code")}</label>
            <input
              type="text"
              {...register("transporeon_code")}
              className={`w-full p-2 border ${
                errors.transporeon_code ? "border-danger" : "border-gray-300"
              } rounded-md`}
            />
            {errors.transporeon_code && (
              <p className="text-danger text-sm">{errors.transporeon_code.message}</p>
            )}
          </div>

          {/* Código MSoft */}
          <div className="col-span-12 md:col-span-6 lg:col-span-4">
            <label className="block text-gray-700">{t("msoft_code")}</label>
            <input
              type="text"
              {...register("msoft_code")}
              className={`w-full p-2 border ${
                errors.msoft_code ? "border-danger" : "border-gray-300"
              } rounded-md`}
            />
            {errors.msoft_code && (
              <p className="text-danger text-sm">{errors.msoft_code.message}</p>
            )}
          </div>

          {/* Botones */}
          <div className="col-span-12 flex justify-center mt-7">
            <Button type="submit">{t("save")}</Button>
            <Button variant="danger" onClick={onClickCancel}>
              {t("cancel")}
            </Button>
          </div>

        </form>
      </div>
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
    content = """import { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import { useNavigate, useParams } from "react-router-dom";
import { SessionLayout } from "../../../layouts/private/SessionLayout";
import { Button } from "../../../components/Buttons/Button";
import Swal from "sweetalert2";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import { getTeamById, updateTeam } from "../services/teamService";

// Esquema de validación con Yup
const schema = yup.object().shape({
  name: yup.string().required("Campo obligatorio"),
  transporeon_code: yup.string().required("Campo obligatorio"),
  msoft_code: yup.string().required("Campo obligatorio"),
});

export const TeamEditPage = () => {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const { id } = useParams();
  const [loading, setLoading] = useState(true);

  // Configuración de react-hook-form con Yup
  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm({ resolver: yupResolver(schema) });


  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await getTeamById(id);
        const {name, transporeon_code, msoft_code} = response.data;
        
        if (response) {
          setValue("name", name);
          setValue("transporeon_code", transporeon_code);
          setValue("msoft_code", msoft_code);
        } else {
          Swal.fire("Error", "No se pudo obtener el registro", "error");
          navigate("/admin/teams");
        }
      } catch (error) {
        console.error("Error al obtener los datos:", error);
        Swal.fire("Error", "Hubo un problema al obtener el registro", "error");
        navigate("/admin/teams");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [id, navigate, setValue]);

  // Función para manejar la actualización
  const onSubmit = async (data) => {
    try {
      console.log("Datos enviados:", data);
      const response = await updateTeam(id, data);

      if (response) {
        Swal.fire("Actualizado", "Registro actualizado correctamente", "success").then(() => {
          navigate("/admin/teams");
        });
      } else {
        Swal.fire("Error", "No se pudo actualizar el registro", "error");
      }
    } catch (error) {
      console.error("Error al actualizar:", error);
      Swal.fire("Error", "Hubo un problema al actualizar el registro", "error");
    }
  };

  // Función para cancelar
  const onClickCancel = (e) => {
    e.preventDefault();
    navigate("/admin/teams");
  };

  return (
    <SessionLayout>
      <div>
        <h2 className="text-2xl font-semibold text-gray-700 mb-4">
          {t("edit")}
        </h2>
      </div>

      <div className="mx-auto p-6 bg-white rounded-lg shadow-lg">
        {loading ? (
          <p className="text-center text-gray-600">Cargando...</p>
        ) : (
          <form onSubmit={handleSubmit(onSubmit)} className="grid grid-cols-12 gap-6">

            {/* Nombre */}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{t("name")}</label>
              <input
                type="text"
                {...register("name")}
                className={`w-full p-2 border ${
                  errors.name ? "border-danger" : "border-gray-300"
                } rounded-md`}
              />
              {errors.name && <p className="text-danger text-sm">{errors.name.message}</p>}
            </div>

            {/* Código Transporeon */}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{t("transporeon_code")}</label>
              <input
                type="text"
                {...register("transporeon_code")}
                className={`w-full p-2 border ${
                  errors.transporeon_code ? "border-danger" : "border-gray-300"
                } rounded-md`}
              />
              {errors.transporeon_code && (
                <p className="text-danger text-sm">{errors.transporeon_code.message}</p>
              )}
            </div>

            {/* Código MSoft */}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{t("msoft_code")}</label>
              <input
                type="text"
                {...register("msoft_code")}
                className={`w-full p-2 border ${
                  errors.msoft_code ? "border-danger" : "border-gray-300"
                } rounded-md`}
              />
              {errors.msoft_code && (
                <p className="text-danger text-sm">{errors.msoft_code.message}</p>
              )}
            </div>

            {/* Botones */}
            <div className="col-span-12 flex justify-center mt-7 gap-2">
              <Button type="submit">{t("save")}</Button>
              <Button variant="danger" onClick={onClickCancel}>
                {t("cancel")}
              </Button>
            </div>

          </form>
        )}
      </div>
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

/**
 * List
 */
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

/**
 * Show
 */
export const getTeamById = async (id) => {
    try {
        const token = localStorage.getItem("token_portuarios");
        if (!token) return null;

        const response = await api(`teams/show/${id}`, "GET", null, token);
        return response;
    } catch (error) {
        console.error("Error al obtener el registro:", error);
        return null;
    }
};


/**
 * Store
 */
export const createTeam = async (data) => {
    try {
        const token = localStorage.getItem("token_portuarios");
        if (!token) {
            console.warn("No hay token disponible en localStorage");
            return null;
        }

        const response = await api("teams/store", "POST", data, token);

        if (!response || typeof response !== "object") {
            console.error("Error en la respuesta de la API:", response);
            return null;
        }

        return response;
    } catch (error) {
        console.error("Error al enviar los datos:", error);
        return null;
    }
};



/**
 * Update
 */
export const updateTeam = async (id, data) => {
    try {
        const token = localStorage.getItem("token_portuarios");
        if (!token) return null;

        const response = await api(`teams/update/${id}`, "PUT", data, token);
        return response;
    } catch (error) {
        console.error("Error al actualizar el registro:", error);
        return null;
    }
};


/**
 * Delete
 */
export const deleteTeam = async (id) => {
    try {
        const token = localStorage.getItem("token_portuarios");
        if (!token) return null;

        const response = await api(`teams/delete/${id}`, "DELETE", null, token);
        return response;
    } catch (error) {
        console.error("Error al actualizar el registro:", error);
        return null;
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
