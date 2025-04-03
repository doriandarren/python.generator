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

        if (response.success) {{
          {set_values}
        }} else {{
          Swal.fire(t("error"), "error");
          navigate("/admin/{plural_name_kebab}");
        }}
      }} catch (error) {{
        console.error("Error al obtener los datos:", error);
        Swal.fire(t("errors.error_process"), "error");
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
        Swal.fire(t("message.record_updated"), "success").then(() => {{
          navigate("/admin/{plural_name_kebab}");
        }});
      }} else {{
        Swal.fire(t("error"), "error");
      }}
    }} catch (error) {{
      console.error("Error al actualizar:", error);
      Swal.fire(t("errors.error_process"), "error");
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
