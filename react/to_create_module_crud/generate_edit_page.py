import os
from helpers.helper_print import create_folder

from react.to_create_module_crud.helpers.helper_react_form_generator import (
    build_yup_schema_fields,
    build_input_fields,
)

from react.to_create_module_crud.helpers.helper_react_relations import (
    build_combobox_import,
    build_variables,
    has_fk,
    build_edit_fetch_pieces,
    build_boolean_import,
    has_boolean,
    build_boolean_edit_set_values,
)


def pascal_to_camel_case(name: str) -> str:
    """Profile -> profile"""
    if not name:
        return ""
    return name[:1].lower() + name[1:]


def create_edit_page(
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
    Genera dinámicamente:
    src/modules/{plural_name_snake}/pages/{SingularName}EditPage.jsx

    Equivalente al generateEdit.js (Node).
    """
    pages_dir = os.path.join(full_path, "src", "modules", plural_name_snake, "pages")
    create_folder(pages_dir)

    file_path = os.path.join(pages_dir, f"{singular_name}EditPage.jsx")

    lower_first = pascal_to_camel_case(singular_name)

    # columnNames + setValues
    column_names = [c["name"] for c in columns]
    set_values = "\n          ".join([f'setValue("{col}", data.{col});' for col in column_names])

    # schema + inputs
    schema_fields = build_yup_schema_fields(columns)
    input_fields = build_input_fields(columns)

    # Combobox pieces
    create_variables = build_variables(columns)
    combobox_import = build_combobox_import(columns)
    has_any_fk = has_fk(columns)

    fk_pieces = build_edit_fetch_pieces(columns)
    res_names = fk_pieces.get("resNames", "")
    promise_calls = fk_pieces.get("promiseCalls", "")
    fk_load_blocks = fk_pieces.get("fkLoadBlocks", "")
    fk_select_blocks = fk_pieces.get("fkSelectBlocks", "")

    # Boolean pieces
    boolean_import = build_boolean_import(columns)
    needs_watch = has_boolean(columns)
    boolean_edit_set_values = build_boolean_edit_set_values(columns, data_var="data")

    # Construcción del Promise.all como en Node:
    # const [ profileRes, customersRes, ... ] = await Promise.all([ getProfileById(id), getCustomers(), ... ])
    promise_array = f"get{singular_name}ById(id)"
    if promise_calls:
        promise_array += f",\n          {promise_calls}"
        # en Node meten una coma extra al final si hay promiseCalls; no hace falta, pero no molesta.
    destructuring = f"{lower_first}Res"
    if res_names:
        destructuring += f", {res_names}"

    watch_line = "\n    watch," if needs_watch else ""

    # IMPORTS: aquí NO usamos f-string para evitar choque con llaves; usamos placeholders
    template = r"""
import { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import { useNavigate, useParams } from "react-router-dom";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";
import Swal from "sweetalert2";
import { SessionLayout } from "../../../layouts/private/SessionLayout";
import { ThemedButton } from "../../../components/Buttons/ThemedButton";
import { ThemedText } from "../../../components/Text/ThemedText";
import { ThemedCard } from "../../../components/Cards/ThemedCard";
import { Preloader } from "../../../components/Preloader/Preloader";
import { PreloaderButton } from "../../../components/Preloader/PreloaderButton";
import { get__SINGULAR__ById, update__SINGULAR__ } from "../services/__SINGULAR_CAMEL__Service";__BOOLEAN_IMPORT____COMBOBOX_IMPORT__

export const __SINGULAR__EditPage = () => {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const { id } = useParams();
  const [dataLoading, setDataLoading] = useState(true);
  const [isLoading, setIsLoading] = useState(false);

__CREATE_VARIABLES__

  const schema = yup.object().shape({
    __SCHEMA_FIELDS__
  });

  const {
    register,
    handleSubmit,
    setValue,__WATCH__
    formState: { errors },
  } = useForm({ resolver: yupResolver(schema) });

  useEffect(() => {
    const fetchData = async () => {
      try {
        setDataLoading(true);

        const [ __DESTRUCT__ ] = await Promise.all([
          __PROMISE_ARRAY__
        ]);

__FK_LOAD_BLOCKS__

        if (__LOWER_RES__.success) {

          const {data} = __LOWER_RES__;
          __SET_VALUES__

__FK_SELECT_BLOCKS__

__BOOLEAN_SET_VALUES__

        } else {

          Swal.fire({
            title: t("error"),
            icon: "error",
            confirmButtonText: t("message.ok"),
            confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_DANGER
          });
          navigate("/admin/__PLURAL_KEBAB__");

        }
      } catch (error) {

        console.error("Error al obtener los datos:", error);
        Swal.fire({
          title: t("errors.error_process"),
          icon: "error",
          confirmButtonText: t("message.ok"),
          confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_DANGER
        });
        navigate("/admin/__PLURAL_KEBAB__");

      } finally {

        setDataLoading(false);

      }
    };

    fetchData();
  }, [id, navigate, setValue, t]);

  const onSubmit = async (data) => {
    try {
      setIsLoading(true);
      const response = await update__SINGULAR__(id, data);

      if (response.success) {
        Swal.fire({
          title: t("message.record_updated"),
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
      console.error("Error al actualizar:", error);
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

      <ThemedText type="h2">{t("edit")}</ThemedText>

      <ThemedCard>
        {dataLoading ? (
          <Preloader />
        ) : (
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
                {t("cancel")}
              </ThemedButton>
            </div>
          </form>
        )}
      </ThemedCard>
    </SessionLayout>
  );
};
""".lstrip()

    # Bloques condicionales FK/Boolean
    fk_load_blocks = fk_load_blocks.strip()
    if not has_any_fk or not fk_load_blocks:
        fk_load_blocks_final = ""
    else:
        fk_load_blocks_final = fk_load_blocks

    fk_select_blocks = fk_select_blocks.strip()
    if not has_any_fk or not fk_select_blocks:
        fk_select_blocks_final = ""
    else:
        fk_select_blocks_final = fk_select_blocks

    boolean_set_values = boolean_edit_set_values.strip()
    if not needs_watch or not boolean_set_values:
        boolean_set_values_final = ""
    else:
        boolean_set_values_final = boolean_set_values

    content = (
        template
        .replace("__SINGULAR__", singular_name)
        .replace("__SINGULAR_CAMEL__", singular_name_camel)
        .replace("__PLURAL_KEBAB__", plural_name_kebab)
        .replace("__BOOLEAN_IMPORT__", boolean_import)
        .replace("__COMBOBOX_IMPORT__", combobox_import)
        .replace("__CREATE_VARIABLES__", create_variables)
        .replace("__SCHEMA_FIELDS__", schema_fields)
        .replace("__INPUT_FIELDS__", input_fields)
        .replace("__WATCH__", watch_line)
        .replace("__DESTRUCT__", destructuring)
        .replace("__PROMISE_ARRAY__", promise_array)
        .replace("__LOWER_RES__", f"{lower_first}Res")
        .replace("__SET_VALUES__", set_values)
        .replace("__FK_LOAD_BLOCKS__", fk_load_blocks_final)
        .replace("__FK_SELECT_BLOCKS__", fk_select_blocks_final)
        .replace("__BOOLEAN_SET_VALUES__", boolean_set_values_final)
    )

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Archivo creado: {file_path}")
    except Exception as e:
        print(f"❌ Error al crear archivo {file_path}: {e}")
