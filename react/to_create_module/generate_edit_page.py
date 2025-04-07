import os
from helpers.helper_print import create_folder



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
import {{ Preloader }} from "../../../components/Preloader/Preloader";
import {{ PreloaderButton }} from "../../../components/Preloader/PreloaderButton";




export const {singular_name}EditPage = () => {{
  const {{ t }} = useTranslation();
  const navigate = useNavigate();
  const {{ id }} = useParams();
  const [dataLoading, setDataLoading] = useState(true);
  const [isLoading, setIsLoading] = useState(false);


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
          setDataLoading(true);
          const response = await get{singular_name}ById(id);
          const data = response.data;
    
          if (response.success) {{
            {set_values}
          }} else {{
            Swal.fire({{
              title: t("error"),
              icon: "error",
              confirmButtonText: t("message.ok"),
              confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_ERROR
            }});
            navigate("/admin/{plural_name_kebab}");
          }}
        }} catch (error) {{
          console.error("Error al obtener los datos:", error);
          Swal.fire({{
            title: t("errors.error_proccess"),
            icon: "error",
            confirmButtonText: t("message.ok"),
            confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_ERROR
          }});
          navigate("/admin/{plural_name_kebab}");
        }} finally {{
          setDataLoading(false);
        }}
      }}
    
      fetchData();
      
  }}, [id, navigate, setValue]);

  
  
  // Función para manejar la actualización
  const onSubmit = async (data) => {{
      try {{
        setIsLoading(true);
    
        const response = await update{singular_name}(id, data);
    
        if (response) {{
          Swal.fire({{
            title: t("message.record_updated"),
            icon: "success",
            confirmButtonText: t("message.ok"),
            confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_SUCCESS
          }}).then(() => {{
            navigate("/admin/{plural_name_kebab}");
          }});
        }} else {{
          Swal.fire({{
            title: t("error"),
            icon: "error",
            confirmButtonText: t("message.ok"),
            confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_ERROR
          }});
        }}
      }} catch (error) {{
        console.error("Error al actualizar:", error);
        Swal.fire({{
          title: t("errors.error_proccess"),
          icon: "error",
          confirmButtonText: t("message.ok"),
          confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_ERROR
        }});
      }} finally {{
        setIsLoading(false);
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
        {{dataLoading ? (
          <Preloader />
        ) : (
          <form onSubmit={{handleSubmit(onSubmit)}} className="grid grid-cols-12 gap-6">

            {input_fields}

            <div className="col-span-12 flex justify-center items-center mt-7 gap-4 flex-wrap">
                <Button 
                  type="submit"
                  disabled={{isLoading}}
                  className="w-32 h-12 flex items-center justify-center"
                >
                  {{ 
                    isLoading 
                    ? <PreloaderButton /> 
                    : t("save")
                  }}
                </Button>
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
