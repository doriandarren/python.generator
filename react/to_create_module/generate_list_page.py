import os
from helpers.helper_print import create_folder



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
import {{ Preloader }} from "../../../components/Preloader/Preloader";


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
          <h2 className="text-2xl font-bold text-gray-800 mb-4">{{ t("{plural_name_snake}") }}</h2>
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
        <Preloader />
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
