import os
from helpers.helper_menu import pause
from helpers.helper_print import create_folder, print_message, GREEN, CYAN

from react.helpers.helper_react_form_generator import (
    build_input_fields,
    build_yup_schema_fields,
)

from react.helpers.helper_react_relations import (
    build_combobox_import,
    build_variables,
    has_fk,
    build_combobox_use_effect,
    build_boolean_import,
    has_boolean,
    build_boolean_default_values_prop,
)


def generate_single_page(
    full_path,
    project_name,
    singular_name,
    plural_name,
    singular_name_kebab,
    plural_name_kebab,
    singular_name_snake,
    plural_name_snake,
    singular_first_camel,
    plural_first_camel,
    columns,
):
    """
    Genera el archivo
    """
    
    
    print(plural_name_snake)
    
    pause()
    
    folder_path = os.path.join(full_path, "src", "modules", plural_name_snake, "pages")
    file_path = os.path.join(folder_path, f"{singular_name}Page.jsx")
    

    create_folder(folder_path)

    # === Form generator ===
    schema_fields = build_yup_schema_fields(columns)
    input_fields = build_input_fields(columns)

    # === Combobox ===
    create_variables = build_variables(columns)
    combobox_import = build_combobox_import(columns)
    has_input_fk = has_fk(columns)
    combobox_use_effect = build_combobox_use_effect(columns)

    # === Boolean ===
    boolean_import = build_boolean_import(columns)
    has_input_boolean = has_boolean(columns)
    boolean_defaults_prop = build_boolean_default_values_prop(columns)

    # Helpers para insertar trozos condicionales en el template
    react_import_effect = " useEffect, " if has_input_fk else " "
    useform_setvalue = "\n    setValue," if has_input_fk else ""
    useform_watch = "\n    watch," if has_input_boolean else ""
    defaults_block = f"\n    {boolean_defaults_prop}" if boolean_defaults_prop else ""

    content = f'''import {{{react_import_effect}useState }} from "react";
import {{ useTranslation }} from "react-i18next";
import {{ useNavigate }} from "react-router-dom";
import {{ useForm }} from "react-hook-form";
import {{ yupResolver }} from "@hookform/resolvers/yup";
import * as yup from "yup";
import Swal from "sweetalert2";
import {{ SessionLayout }} from "../../../layouts/private/SessionLayout";
import {{ PreloaderButton }} from "../../../components/Preloader/PreloaderButton";{boolean_import}{combobox_import}
import {{ ThemedButton }} from "../../../components/Buttons/ThemedButton";
import {{ ThemedText }} from "../../../components/Text/ThemedText";
import {{ ThemedCard }} from "../../../components/Cards/ThemedCard";
import {{ get{plural_name} }} from "../services/{singular_first_camel}Service";

export const {singular_name}Page = () => {{
  const {{ t }} = useTranslation();
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(false);

  {create_variables}

  const schema = yup.object().shape({{
    {schema_fields}
  }});

  const {{
    register,
    handleSubmit,{useform_setvalue}{useform_watch}
    formState: {{ errors }},
  }} = useForm({{
    resolver: yupResolver(schema),{defaults_block}
  }});

  {combobox_use_effect}

  const onClickCancel = (e) => {{
    e.preventDefault();
    navigate("/admin/dashboard");
  }};

  const onSubmit = async() => {{
    try {{
      setIsLoading(true);
      const {{ success }} = await get{plural_name}();

      if (success) {{
        Swal.fire({{
          title: t("message.record_saved"),
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
          confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_DANGER
        }});
      }}
    }} catch (error) {{
      console.error("Error al enviar los datos:", error);
      Swal.fire({{
        title: t("errors.error_process"),
        icon: "error",
        confirmButtonText: t("message.ok"),
        confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_DANGER
      }});
    }} finally {{
      setIsLoading(false);
    }}
  }};

  return (
    <SessionLayout>
      
      <ThemedText type="h2">{{t("{plural_name_snake}")}}</ThemedText>

      <ThemedCard>
        <form onSubmit={{handleSubmit(onSubmit)}} className="grid grid-cols-12 gap-6">

          {input_fields}

          <div className="col-span-12 flex justify-center items-center mt-7 gap-4 flex-wrap">
            <ThemedButton 
              type="submit"
              disabled={{isLoading}}
              className="w-32 h-10 flex items-center justify-center"
            >
              {{ 
                isLoading 
                ? <PreloaderButton /> 
                : t("save")
              }}
            </ThemedButton>
            <ThemedButton variant="danger" onClick={{onClickCancel}}>
              {{t("cancel")}}
            </ThemedButton>
          </div>

        </form>
      </ThemedCard>
    </SessionLayout>
  );
}};
'''

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print_message(f"✅ Archivo creado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"❌ Error al crear el archivo {file_path}: {e}", CYAN)

