import os
from react.utils.utils import create_folder, camel_to_kebab, camel_to_snake




def generate_module_standard(project_path, singular_name, plural_name, columns):

    # Convertir singular_name y plural_name a kebab-case para las URLs
    singular_name_kebab = camel_to_kebab(singular_name)
    plural_name_kebab = camel_to_kebab(plural_name)
    singular_name_snake = camel_to_snake(singular_name)
    plural_name_snake = camel_to_snake(plural_name)
    singular_first_camel = singular_name[:1].lower() + singular_name[1:]


    ## Example:
    ##create_routes(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns)

    create_routes(project_path, singular_name, plural_name_snake)
    create_list_page(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns)
    create_create_page(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns)
    create_edit_page(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns)
    create_barrel_file(project_path, singular_name, plural_name_snake)
    create_service_file(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns)





def create_routes(project_path, singular_name, plural_name_snake):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", plural_name_snake, "routes")
    file_path = os.path.join(routes_dir, f"{singular_name}Routes.jsx")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo jsx
    content = f"""import {{ Route, Routes }} from "react-router";
import {{ {singular_name}Page, {singular_name}CreatePage, {singular_name}EditPage }} from "../pages";

export const {singular_name}Routes = () => {{
  return (
    <Routes>

      <Route path="/" element={{<{singular_name}Page />}} />
      <Route path="create" element={{<{singular_name}CreatePage />}} />
      <Route path="edit/:id" element={{<{singular_name}EditPage />}} />

    </Routes>
  )
}}
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")


def create_list_page(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns):
    """
    Genera dinámicamente el archivo {singular_name}Page.jsx con nombres adaptados.
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", plural_name_snake, "pages")
    file_path = os.path.join(pages_dir, f"{singular_name}Page.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Extraer solo los nombres de columna correctamente
    column_names = [col["name"] for col in columns]

    # Generar correctamente `dataHeader` sin formato erróneo
    data_headers = ",\n    ".join([f'{{ key: "{col}", label: t("{col}") }}' for col in column_names])

    # Contenido del archivo JSX con nombres dinámicos
    content = f"""import {{ SessionLayout }} from "../../../layouts/private/SessionLayout";
import {{ Datatable }} from "../../../components/DataTables/DataTable";
import {{ useNavigate }} from "react-router-dom";
import {{ useTranslation }} from "react-i18next";
import {{ Button }} from "../../../components/Buttons/Button";
import {{ useEffect, useState }} from "react";
import {{ delete{singular_name}, get{plural_name} }} from "../services/{singular_first_camel}Service";
import Swal from "sweetalert2";
import {{ Toast }} from "../../../helpers/helperToast";


export const {singular_name}Page = () => {{
  const navigate = useNavigate();
  const {{ t }} = useTranslation();
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  const dataHeader = [
    {data_headers}
  ];

  useEffect(() => {{
    const fetchApi = async () => {{
      setLoading(true);

      try {{
        const response = await get{plural_name}();
        const {{ data }} = response;

        if (Array.isArray(data)) {{
          setData(data);
        }} else {{
          console.warn("La API no devolvió un array:", response);
        }}
      }} catch (error) {{
        console.error("Error al obtener los datos:", error);
      }} finally {{
        setLoading(false);
      }}
    }};

    fetchApi();
  }}, []);

  const onDeleteClick = async (id, description = "") => {{
    Swal.fire({{
      icon: "warning",
      title: t("message.are_you_sure"),
      text: t("delete") + (description !== "" ? ": " + description : ""),
      showCancelButton: true,
      confirmButtonText: t("delete"),
      cancelButtonText: t("cancel"),
      confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_SUCCESS,
    }}).then(async (result) => {{
      if (result.isConfirmed) {{
        try {{
          const response = await delete{singular_name}(id);
          const {{ success, errors }} = response;

          if (success) {{
            setData((prevData) => prevData.filter((item) => item.id !== id));
            await Toast(t("message.record_deleted"), "success");
          }} else {{
            await Toast(errors?.[0]?.e || t("message.error_deleting"), "error");
          }}
        }} catch (error) {{
          console.error("Error al eliminar el registro:", error);
          await Toast(t("message.error_deleting"), "error");
        }}
      }}
    }});
  }};

  const onAddClick = (e) => {{
    e.preventDefault();
    navigate("/admin/{plural_name_kebab}/create");
  }};

  return (
    <SessionLayout>
      <div className="flex items-center justify-between mb-5">
        <div className="mt-1">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">{{ t("{plural_name_kebab}") }}</h2>
        </div>

        <div className="sm:flex sm:items-center">
          <div className="mt-4 sm:mt-0 sm:flex-none">
            <Button type="button" onClick={{onAddClick}}>
              {{ t("add") }}
            </Button>
          </div>
        </div>
      </div>

      {{ loading ? (
        <p className="text-center text-gray-600">{{ t("loading") }}</p>
      ) : (
        <Datatable
          columns={{dataHeader}}
          data={{data}}
          editPath="/admin/{plural_name_kebab}"
          onDelete={{onDeleteClick}}
        />
      ) }}
    </SessionLayout>
  );
}};
"""

    # Crear el archivo
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")


def create_create_page(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns):
    """
    Genera dinámicamente el archivo
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", plural_name_snake, "pages")
    file_path = os.path.join(pages_dir, f"{singular_name}CreatePage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Extraer los nombres de columna correctamente
    column_names = [col["name"] for col in columns]

    # Generar dinámicamente el esquema de validación con Yup
    schema_fields = ",\n    ".join([f'{col}: yup.string().required(t("form.required"))' for col in column_names])

    # Generar dinámicamente los inputs del formulario
    input_fields = "\n\n        ".join([
        f"""<div className="col-span-12 md:col-span-6 lg:col-span-4">
            <label className="block text-gray-700">{{t("{col}")}}</label>
            <input
              type="text"
              {{...register("{col}")}}
              className={{`w-full p-2 border ${{errors.{col} ? "border-danger" : "border-gray-300"}} rounded-md`}}
            />
            {{errors.{col} && <p className="text-danger text-sm">{{errors.{col}.message}}</p>}}
          </div>"""
        for col in column_names
    ])

    # Contenido del archivo JSX con nombres y campos dinámicos
    content = f"""import {{ useTranslation }} from "react-i18next";
import {{ SessionLayout }} from "../../../layouts/private/SessionLayout";
import {{ Button }} from "../../../components/Buttons/Button";
import Swal from "sweetalert2";
import {{ useNavigate }} from "react-router-dom";
import {{ useForm }} from "react-hook-form";
import {{ yupResolver }} from "@hookform/resolvers/yup";
import * as yup from "yup";
import {{ create{singular_name} }} from "../services/{singular_first_camel}Service";

export const {singular_name}CreatePage = () => {{
  const {{ t }} = useTranslation();
  const navigate = useNavigate();

  // Schema de validación con Yup
  const schema = yup.object().shape({{
    {schema_fields}
  }});

  // react-hook-form con Yup
  const {{
    register,
    handleSubmit,
    formState: {{ errors }},
  }} = useForm({{ resolver: yupResolver(schema) }});

  const onSubmit = async(data) => {{
    try {{
      console.log("Datos enviados:", data);

      const response = await create{singular_name}(data);

      if (response) {{
        Swal.fire("Registro guardado correctamente", "Registro guardado", "success").then(() => {{
          navigate("/admin/{plural_name_kebab}");
        }});
      }} else {{
        Swal.fire("Error", "No se pudo guardar el registro", "error");
      }}
    }} catch (error) {{
      console.error("Error al enviar los datos:", error);
      Swal.fire("Error", "Hubo un problema al guardar el registro", "error");
    }}
  }};

  const onClickCancel = (e) => {{
    e.preventDefault();
    navigate("/admin/{plural_name_kebab}");
  }};

  return (
    <SessionLayout>
      <div>
        <h2 className="text-2xl font-semibold text-gray-700 mb-4">
          {{ t("add") }}
        </h2>
      </div>

      <div className="mx-auto p-6 bg-white rounded-lg shadow-lg">
        <form onSubmit={{handleSubmit(onSubmit)}} className="grid grid-cols-12 gap-6">

          {input_fields}

          <div className="col-span-12 flex justify-center mt-7">
            <Button type="submit">{{ t("save") }}</Button>
            <Button variant="danger" onClick={{onClickCancel}}>
              {{ t("cancel") }}
            </Button>
          </div>

        </form>
      </div>
    </SessionLayout>
  );
}};
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")


def create_edit_page(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns):
    """
        Genera dinámicamente el archivo {singular_name}EditPage.jsx con nombres y campos adaptados.
        """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src", "modules", plural_name_snake, "pages")
    file_path = os.path.join(pages_dir, f"{singular_name}EditPage.jsx")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Extraer solo los nombres de columna
    column_names = [col["name"] for col in columns]

    # Genera correctamente el esquema de validación sin errores de interpolación
    schema_fields = ",\n    ".join([f'{col}: yup.string().required(t("{col}"))' for col in column_names])

    # Genera correctamente los valores `setValue`
    set_values = "\n        ".join([f'setValue("{col}", data.{col});' for col in column_names])

    # Genera correctamente los inputs sin dobles llaves
    input_fields = "\n\n          ".join([
        f"""<div className="col-span-12 md:col-span-6 lg:col-span-4">
                <label className="block text-gray-700">{{t("{col}")}}</label>
                <input
                  type="text"
                  {{...register("{col}")}}
                  className={{`w-full p-2 border ${{errors.{col} ? "border-danger" : "border-gray-300"}} rounded-md`}}
                />
                {{errors.{col} && <p className="text-danger text-sm">{{errors.{col}.message}}</p>}}
              </div>"""
        for col in column_names
    ])

    # Genera correctamente `dataHeader` sin errores de interpolación
    data_header = ",\n    ".join([f'{{ key: "{col}", label: t("{col}") }}' for col in column_names])

    # Contenido del archivo JSX con nombres y campos dinámicos
    content = f"""import {{ useEffect, useState }} from "react";
import {{ useTranslation }} from "react-i18next";
import {{ useNavigate, useParams }} from "react-router-dom";
import {{ SessionLayout }} from "../../../layouts/private/SessionLayout";
import {{ Button }} from "../../../components/Buttons/Button";
import Swal from "sweetalert2";
import {{ useForm }} from "react-hook-form";
import {{ yupResolver }} from "@hookform/resolvers/yup";
import * as yup from "yup";
import {{ get{singular_name}ById, update{singular_name} }} from "../services/{singular_first_camel}Service";



export const {singular_name}EditPage = () => {{
  const {{ t }} = useTranslation();
  const navigate = useNavigate();
  const {{ id }} = useParams();
  const [loading, setLoading] = useState(true);
  
  // Esquema de validación con Yup (fuera del componente)
  const schema = yup.object().shape({{
    {schema_fields}
  }});

  // Configuración de react-hook-form con Yup
  const {{
    register,
    handleSubmit,
    setValue,
    formState: {{ errors }},
  }} = useForm({{ resolver: yupResolver(schema) }});

  useEffect(() => {{
    const fetchData = async () => {{
      try {{
        setLoading(true);
        const response = await get{singular_name}ById(id);
        const data = response.data;

        if (response) {{
          {set_values}
        }} else {{
          Swal.fire("Error", "No se pudo obtener el registro", "error");
          navigate("/admin/{plural_name_kebab}");
        }}
      }} catch (error) {{
        console.error("Error al obtener los datos:", error);
        Swal.fire("Error", "Hubo un problema al obtener el registro", "error");
        navigate("/admin/{plural_name_kebab}");
      }} finally {{
        setLoading(false);
      }}
    }};

    fetchData();
  }}, [id, navigate, setValue]);

  // Función para manejar la actualización
  const onSubmit = async (data) => {{
    try {{
      console.log("Datos enviados:", data);
      const response = await update{singular_name}(id, data);

      if (response) {{
        Swal.fire("Actualizado", "Registro actualizado correctamente", "success").then(() => {{
          navigate("/admin/{plural_name_kebab}");
        }});
      }} else {{
        Swal.fire("Error", "No se pudo actualizar el registro", "error");
      }}
    }} catch (error) {{
      console.error("Error al actualizar:", error);
      Swal.fire("Error", "Hubo un problema al actualizar el registro", "error");
    }}
  }};

  // Función para cancelar
  const onClickCancel = (e) => {{
    e.preventDefault();
    navigate("/admin/{plural_name_kebab}");
  }};

  return (
    <SessionLayout>
      <div>
        <h2 className="text-2xl font-semibold text-gray-700 mb-4">
          {{ t("edit") }}
        </h2>
      </div>

      <div className="mx-auto p-6 bg-white rounded-lg shadow-lg">
        {{loading ? (
          <p className="text-center text-gray-600">Cargando...</p>
        ) : (
          <form onSubmit={{handleSubmit(onSubmit)}} className="grid grid-cols-12 gap-6">

            {input_fields}

            <div className="col-span-12 flex justify-center mt-7 gap-2">
              <Button type="submit">{{ t("save") }}</Button>
              <Button variant="danger" onClick={{onClickCancel}}>
                {{ t("cancel") }}
              </Button>
            </div>

          </form>
        )}}
      </div>
    </SessionLayout>
  );
}};
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")


def create_barrel_file(project_path, singular_name, plural_name_snake):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    routes_dir = os.path.join(project_path, "src", "modules", plural_name_snake, "pages")
    file_path = os.path.join(routes_dir, "index.js")

    # Crear la carpeta routes si no existe
    create_folder(routes_dir)

    # Contenido del archivo
    content = f"""export * from './{singular_name}Page';
export * from './{singular_name}CreatePage';
export * from './{singular_name}EditPage';
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")


def create_service_file(project_path, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, singular_first_camel, columns):
    """
        Genera dinámicamente el archivo de servicios {singular_name}Service.js con nombres adaptados.
        """
    # Define la ruta del archivo
    services_dir = os.path.join(project_path, "src", "modules", plural_name_snake, "services")


    file_path = os.path.join(services_dir, f"{singular_first_camel}Service.js")


    # Crear la carpeta services si no existe
    create_folder(services_dir)

    # Contenido del archivo JS con nombres dinámicos
    content = f"""import {{ api }} from "../../../api/api";

/**
 * List
 */
export const get{plural_name} = async () => {{
    try {{
        const token = localStorage.getItem("token_portuarios");
        if (!token) {{
            console.warn("No hay token disponible en localStorage");
            return [];
        }}

        const response = await api("{plural_name_kebab}/list", "GET", null, token);

        // Verificar si la API devuelve datos válidos
        if (!response || typeof response !== "object") {{
            console.error("Respuesta no válida de la API:", response);
            return [];
        }}

        return response;
    }} catch (error) {{
        console.error("Error al obtener los registros:", error);
        return [];
    }}
}};

/**
 * Show
 */
export const get{singular_name}ById = async (id) => {{
    try {{
        const token = localStorage.getItem("token_portuarios");
        if (!token) return null;

        const response = await api(`{plural_name_kebab}/show/${{id}}`, "GET", null, token);
        return response;
    }} catch (error) {{
        console.error("Error al obtener el registro:", error);
        return null;
    }}
}};

/**
 * Store
 */
export const create{singular_name} = async (data) => {{
    try {{
        const token = localStorage.getItem("token_portuarios");
        if (!token) {{
            console.warn("No hay token disponible en localStorage");
            return null;
        }}

        const response = await api("{plural_name_kebab}/store", "POST", data, token);

        if (!response || typeof response !== "object") {{
            console.error("Error en la respuesta de la API:", response);
            return null;
        }}

        return response;
    }} catch (error) {{
        console.error("Error al enviar los datos:", error);
        return null;
    }}
}};

/**
 * Update
 */
export const update{singular_name} = async (id, data) => {{
    try {{
        const token = localStorage.getItem("token_portuarios");
        if (!token) return null;

        const response = await api(`{plural_name_kebab}/update/${{id}}`, "PUT", data, token);
        return response;
    }} catch (error) {{
        console.error("Error al actualizar el registro:", error);
        return null;
    }}
}};

/**
 * Delete
 */
export const delete{singular_name} = async (id) => {{
    try {{
        const token = localStorage.getItem("token_portuarios");
        if (!token) return null;

        const response = await api(`{plural_name_kebab}/delete/${{id}}`, "DELETE", null, token);
        return response;
    }} catch (error) {{
        console.error("Error al eliminar el registro:", error);
        return null;
    }}
}};
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")