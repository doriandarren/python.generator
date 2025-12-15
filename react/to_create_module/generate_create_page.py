import os
from helpers.helper_print import create_folder

from react.to_create_module.helpers.helper_react_form_generator import (
    build_yup_schema_fields,
    build_input_fields,
)

from react.to_create_module.helpers.helper_react_relations import (
    build_combobox_import,
    build_variables,
    has_fk,
    build_combobox_use_effect,
    build_boolean_import,
    has_boolean,
    build_boolean_default_values_prop,
)


def create_create_page(
    full_path,
    singular_name,
    plural_name,
    singular_name_kebab,
    plural_name_kebab,
    singular_name_snake,
    plural_name_snake,
    singular_name_camel,
    plural_name_camel,
    columns,
):
    """
    Genera: src/modules/{plural_snake}/pages/{Singular}CreatePage.jsx
    (equivalente al generateCreate de Node)
    """

    pages_dir = os.path.join(full_path, "src", "modules", plural_name_snake, "pages")
    file_path = os.path.join(pages_dir, f"{singular_name}CreatePage.jsx")

    create_folder(pages_dir)

    # --- Schema + Inputs (tu helperReactFormGenerator) ---
    schema_fields = build_yup_schema_fields(columns)
    input_fields = build_input_fields(columns)

    # --- FK / Combobox ---
    create_variables = build_variables(columns)
    combobox_import = build_combobox_import(columns)
    has_input_fk = has_fk(columns)
    combobox_use_effect = build_combobox_use_effect(columns)

    # --- Boolean ---
    boolean_import = build_boolean_import(columns)
    has_input_boolean = has_boolean(columns)
    boolean_defaults_prop = build_boolean_default_values_prop(columns)

    # Fragments dinámicos (como Node)
    react_import = " useEffect, " if has_input_fk else " "
    set_value_line = "\n    setValue," if has_input_fk else ""
    watch_line = "\n    watch," if has_input_boolean else ""
    defaults_block = f"\n    {boolean_defaults_prop}" if boolean_defaults_prop else ""

    # Template con tokens (NO format)
    template = r"""
import {__REACT_IMPORT__useState } from "react";
import { useTranslation } from "react-i18next";
import { useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import Swal from "sweetalert2";
import { SessionLayout } from "../../../layouts/private/SessionLayout";
import { PreloaderButton } from "../../../components/Preloader/PreloaderButton";
import { ThemedButton } from "../../../components/Buttons/ThemedButton";
import { ThemedCard } from "../../../components/Cards/ThemedCard";
import { ThemedText } from "../../../components/Text/ThemedText";
import { create__SINGULAR__ } from "../services/__SINGULAR_CAMEL__Service";__BOOLEAN_IMPORT____COMBOBOX_IMPORT__

export const __SINGULAR__CreatePage = () => {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(false);

  __CREATE_VARIABLES__

  const schema = yup.object().shape({
    __SCHEMA_FIELDS__
  });

  const {
    register,
    handleSubmit,__SET_VALUE____WATCH__
    formState: { errors },
  } = useForm({
    resolver: yupResolver(schema),__DEFAULTS_BLOCK__
  });

  __COMBOBOX_USE_EFFECT__

  const onSubmit = async(data) => {
    try {
      setIsLoading(true);
      const { success } = await create__SINGULAR__(data);

      if (success) {
        Swal.fire({
          title: t("message.record_saved"),
          icon: "success",
          confirmButtonText: t("message.ok"),
          confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_SUCCESS
        }).then(() => {
          navigate("/admin/__PLURAL_KEBAB__");
        });
      } else {
        Swal.fire({
          title: t("error"),
          icon: "error",
          confirmButtonText: t("message.ok"),
          confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_DANGER
        });
      }
    } catch (error) {
      console.error("Error al enviar los datos:", error);
      Swal.fire({
        title: t("errors.error_process"),
        icon: "error",
        confirmButtonText: t("message.ok"),
        confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_DANGER
      });
    } finally {
      setIsLoading(false);
    }
  };

  const onClickCancel = (e) => {
    e.preventDefault();
    navigate("/admin/__PLURAL_KEBAB__");
  };

  return (
    <SessionLayout>

      <ThemedText type="h2">{t("add")}</ThemedText>

      <ThemedCard>
        <form onSubmit={handleSubmit(onSubmit)} className="grid grid-cols-12 gap-6">

          __INPUT_FIELDS__

          <div className="col-span-12 flex justify-center items-center mt-7 gap-4 flex-wrap">
            <ThemedButton
              type="submit"
              disabled={isLoading}
              className="w-32 h-10 flex items-center justify-center"
            >
              {
                isLoading
                ? <PreloaderButton />
                : t("save")
              }
            </ThemedButton>

            <ThemedButton variant="danger" onClick={onClickCancel}>
              { t("cancel") }
            </ThemedButton>
          </div>

        </form>
      </ThemedCard>
    </SessionLayout>
  );
};
""".lstrip()

    content = (
        template
        .replace("__REACT_IMPORT__", react_import)
        .replace("__SINGULAR__", singular_name)
        .replace("__PLURAL_KEBAB__", plural_name_kebab)
        .replace("__SINGULAR_CAMEL__", singular_name_camel)
        .replace("__SCHEMA_FIELDS__", schema_fields)
        .replace("__INPUT_FIELDS__", input_fields)
        .replace("__CREATE_VARIABLES__", create_variables)
        .replace("__COMBOBOX_IMPORT__", combobox_import)
        .replace("__BOOLEAN_IMPORT__", boolean_import)
        .replace("__COMBOBOX_USE_EFFECT__", combobox_use_effect)
        .replace("__SET_VALUE__", set_value_line)
        .replace("__WATCH__", watch_line)
        .replace("__DEFAULTS_BLOCK__", defaults_block)
    )

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Archivo creado: {file_path}")
    except Exception as e:
        print(f"❌ Error al crear el archivo {file_path}: {e}")
