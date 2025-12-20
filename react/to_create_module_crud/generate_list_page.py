import os
from helpers.helper_print import create_folder

from react.to_create_module_crud.helpers.helper_list import (
    clean_name,
    build_filters_state,
    build_reset_filters_body,
    build_filters_object,
    build_effect_deps,
    build_render_filters_fn,
)


def generate_list_page(
    project_path,
    singular_name,
    plural_name,
    singular_name_kebab,
    plural_name_kebab,
    singular_name_snake,
    plural_name_snake,
    singular_first_camel,
    columns,
):
    pages_dir = os.path.join(project_path, "src", "modules", plural_name_snake, "pages")
    file_path = os.path.join(pages_dir, f"{singular_name}Page.jsx")

    create_folder(pages_dir)

    column_names = [c["name"] for c in columns]

    # headers: label limpia _id
    data_headers = "\n".join(
        [f'    {{ key: "{col}", label: t("{clean_name(col)}") }},' for col in column_names]
    )

    # filtros (igual que Node)
    filters_state = build_filters_state(column_names)
    reset_filters_body = build_reset_filters_body(column_names)
    filters_object = build_filters_object(column_names, indent="          ")
    effect_deps = build_effect_deps(column_names)
    render_filters = build_render_filters_fn(column_names).rstrip()

    # Template con TOKENS únicos (sin format)
    template = r"""
import { useEffect, useState, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import Swal from "sweetalert2";
import { SessionLayout } from "../../../layouts/private/SessionLayout";
import { Toast } from "../../../helpers/helperToast";
import { Preloader } from "../../../components/Preloader/Preloader";
import { ThemedDataTable } from "../../../components/DataTables/ThemedDataTable";
import { ThemedButton } from "../../../components/Buttons/ThemedButton";
import { ThemedText } from "../../../components/Text/ThemedText";
import { delete__SINGULAR__, get__PLURAL__ } from "../services/__SERVICE__Service";

export const __SINGULAR__Page = () => {
  const navigate = useNavigate();
  const { t } = useTranslation();
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  // --- filtros (UI) ---
  __FILTERS_STATE__

  const resetFilters = useCallback(() => {
__RESET_FILTERS_BODY__
  }, []);

  const dataHeader = [
__DATA_HEADERS__
  ];

  useEffect(() => {
    const fetchApi = async () => {
      setLoading(true);
      try {

        const response = await get__PLURAL__({
__FILTERS_OBJECT__
        });

        const { data } = response;

        if (Array.isArray(data)) {
          setData(data);
        } else {
          console.warn("La API no devolvió un array:", response);
        }
      } catch (error) {
        console.error("Error al obtener los datos:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchApi();
  }, [__EFFECT_DEPS__]);

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
          const response = await delete__SINGULAR__(id);
          const { success, errors } = response;

          if (success) {
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
    navigate("/admin/__PLURAL_KEBAB__/create");
  };

  return (
    <SessionLayout>
      <div className="flex items-center justify-between mb-5">
        <ThemedText type="h2">{t("__PLURAL_SNAKE__")}</ThemedText>

        <div className="sm:flex sm:items-center">
          <div className="mt-4 sm:mt-0 sm:flex-none">
            <ThemedButton type="button" onClick={onAddClick}>
              {t("add")}
            </ThemedButton>
          </div>
        </div>
      </div>

      {/* filters */}
      __RENDER_FILTERS__

      {loading ? (
        <Preloader />
      ) : (
        <ThemedDataTable
          columns={dataHeader}
          data={data}
          editPath="/admin/__PLURAL_KEBAB__"
          onDelete={onDeleteClick}
        />
      )}
    </SessionLayout>
  );
};
""".lstrip()

    # Reemplazos (sin format → no KeyError nunca)
    content = (
        template
        .replace("__SINGULAR__", singular_name)
        .replace("__PLURAL__", plural_name)
        .replace("__SERVICE__", singular_first_camel)
        .replace("__PLURAL_KEBAB__", plural_name_kebab)
        .replace("__PLURAL_SNAKE__", plural_name_snake)
        .replace("__FILTERS_STATE__", filters_state)
        .replace("__RESET_FILTERS_BODY__", reset_filters_body)
        .replace("__DATA_HEADERS__", data_headers)
        .replace("__FILTERS_OBJECT__", filters_object)
        .replace("__EFFECT_DEPS__", effect_deps)
        .replace("__RENDER_FILTERS__", render_filters)
    )

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Archivo creado: {file_path}")
    except Exception as e:
        print(f"❌ Error al crear el archivo {file_path}: {e}")
