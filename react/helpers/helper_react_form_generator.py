# helpers/helper_react_form_generator.py
# Versión Python (sin f-strings en JSX) para evitar errores de llaves { } con Pylance.
# Genera strings JSX/Yup igual que tu helper en Node.

import re
import html


def base_from_field(field_name: str) -> str:
    # (fieldName || "").replace(/_?id$/i, "")
    return re.sub(r"_?id$", "", (field_name or ""), flags=re.IGNORECASE)


def to_pascal(s: str) -> str:
    if not s:
        return ""
    s = re.sub(r"[-_\s]+", " ", s.strip())
    words = re.findall(r"\w+", s)
    return "".join(w[:1].upper() + w[1:].lower() for w in words)


def to_camel(s: str) -> str:
    p = to_pascal(s)
    return (p[:1].lower() + p[1:]) if p else ""


def pluralize(s: str) -> str:
    if not s:
        return ""
    if re.search(r"[sxz]$", s, flags=re.IGNORECASE) or re.search(r"(sh|ch)$", s, flags=re.IGNORECASE):
        return s + "es"
    if re.search(r"y$", s, flags=re.IGNORECASE):
        return re.sub(r"y$", "ies", s, flags=re.IGNORECASE)
    return s + "s"


def to_yup_schema_for(col_type: str, required: bool) -> str:
    """
    Devuelve el encadenado de Yup como string (p.ej. "yup.number().integer().required(...)")
    """
    T = (col_type or "STRING").upper()

    base = (
        'yup.number().oneOf([0,1])' if T == "BOOLEAN" else
        'yup.number().typeError(t("form.number")).integer()' if T in {"INTEGER", "INT", "BIGINT"} else
        'yup.number().typeError(t("form.number"))' if T in {"FLOAT", "DOUBLE", "DECIMAL", "NUMERIC"} else
        'yup.string().required(t("form.required"))' if T == "DATE" else
        'yup.string().required(t("form.required"))' if T in {"DATETIME", "TIMESTAMP"} else
        'yup.string().email(t("form.email"))' if T == "EMAIL" else
        'yup.string()' if T == "UUID" else
        'yup.mixed()' if T in {"JSON", "FK"} else
        'yup.string()'
    )

    base += '.required(t("form.required"))' if required else '.nullable()'
    return base


def _required_suffix(allow_null) -> str:
    # En tu JS: col.allowNull === false ? ' + " *"' : ''
    return ' + " *"' if allow_null is False else ""


def input_for(col: dict) -> str:
    """
    Devuelve el bloque JSX (string) para un campo.
    OJO: sin f-string para que no explote con llaves.
    """
    name = (col.get("name") or "").strip()
    T = (col.get("type") or "STRING").upper()
    required_star = _required_suffix(col.get("allowNull"))

    # Error msg: {errors.name && <p ...>{errors.name?.message}</p>}
    error_msg = (
        "{errors.__NAME__ && <p className=\"text-danger text-sm\">"
        "{errors.__NAME__?.message}</p>}"
    ).replace("__NAME__", name)

    # ====== FK con ThemedCombobox ======
    if T == "FK":
        base = base_from_field(name)             # customer_id -> customer
        pascal = to_pascal(base)                 # Customer
        options_var = to_camel(pluralize(base))  # customers
        selected_var = f"selected{pascal}"
        set_selected_var = f"setSelected{pascal}"
        on_change_var = f"onChange{pascal}"

        tpl = """
            {/* __NAME__ */}
            <div className="col-span-12 md:col-span-6 lg:col-span-6">
              <ThemedCombobox
                label={t("__BASE__")__REQ__}
                options={__OPTIONS__}
                selected={__SELECTED__}
                setSelected={(item) => {
                  __SET_SELECTED__(item);
                  setValue("__NAME__", item?.id, { shouldValidate: true });
                }}
                error={errors.__NAME__?.message}
                getLabel={(item) =>
                  `${item?.name ?? ""}`.trim()
                }
                onChange={(value) => __ON_CHANGE__(value)}
              />
            </div>
""".strip("\n")

        return (
            tpl.replace("__NAME__", name)
               .replace("__BASE__", base)
               .replace("__REQ__", required_star)
               .replace("__OPTIONS__", options_var)
               .replace("__SELECTED__", selected_var)
               .replace("__SET_SELECTED__", set_selected_var)
               .replace("__ON_CHANGE__", on_change_var)
        )

    # ====== BOOLEAN con ThemedToggle (1/0) ======
    if T == "BOOLEAN":
        tpl = """
            {/* __NAME__ */}
            <div className="col-span-12 md:col-span-3 lg:col-span-3">
              <ThemedToggle
                label={t("__NAME__")__REQ__}
                enabled={watch("__NAME__") === 1}
                setEnabled={(value) =>
                  setValue("__NAME__", value ? 1 : 0, { shouldValidate: true })
                }
                error={errors.__NAME__?.message}
              />
              <input type="hidden" {...register("__NAME__")} />
            </div>
""".strip("\n")

        return (
            tpl.replace("__NAME__", name)
               .replace("__REQ__", required_star)
        )

    # ====== TEXT / JSON -> textarea ======
    if T in {"TEXT", "JSON"}:
        tpl = """
            {/* __NAME__ */}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{t("__NAME__")__REQ__}</label>
              <textarea
                rows={4}
                {...register("__NAME__")}
                className={`w-full p-2 border ${errors["__NAME__"] ? "border-danger" : "border-gray-300"} rounded-md`}
              />
              __ERROR__
            </div>
""".strip("\n")

        return (
            tpl.replace("__NAME__", name)
               .replace("__REQ__", required_star)
               .replace("__ERROR__", error_msg)
        )

    # ====== INTEGER ======
    if T in {"INTEGER", "INT", "BIGINT"}:
        tpl = """
            {/* __NAME__ */}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{t("__NAME__")__REQ__}</label>
              <input
                type="number"
                step="1"
                {...register("__NAME__", { valueAsNumber: true })}
                className={`w-full p-2 border ${errors["__NAME__"] ? "border-danger" : "border-gray-300"} rounded-md`}
              />
              __ERROR__
            </div>
""".strip("\n")

        return (
            tpl.replace("__NAME__", name)
               .replace("__REQ__", required_star)
               .replace("__ERROR__", error_msg)
        )

    # ====== FLOAT / DECIMAL / NUMERIC ======
    if T in {"FLOAT", "DOUBLE", "DECIMAL", "NUMERIC"}:
        tpl = """
            {/* __NAME__ */}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{t("__NAME__")__REQ__}</label>
              <input
                type="number"
                step="any"
                {...register("__NAME__", { valueAsNumber: true })}
                className={`w-full p-2 border ${errors["__NAME__"] ? "border-danger" : "border-gray-300"} rounded-md`}
              />
              __ERROR__
            </div>
""".strip("\n")

        return (
            tpl.replace("__NAME__", name)
               .replace("__REQ__", required_star)
               .replace("__ERROR__", error_msg)
        )

    # ====== DATE ======
    if T == "DATE":
        tpl = """
            {/* __NAME__ */}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{t("__NAME__")__REQ__}</label>
              <input
                type="date"
                {...register("__NAME__")}
                className={`w-full p-2 border ${errors["__NAME__"] ? "border-danger" : "border-gray-300"} rounded-md`}
              />
              __ERROR__
            </div>
""".strip("\n")

        return (
            tpl.replace("__NAME__", name)
               .replace("__REQ__", required_star)
               .replace("__ERROR__", error_msg)
        )

    # ====== DATETIME / TIMESTAMP ======
    if T in {"DATETIME", "TIMESTAMP"}:
        tpl = """
            {/* __NAME__ */}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{t("__NAME__")__REQ__}</label>
              <input
                type="datetime-local"
                {...register("__NAME__")}
                className={`w-full p-2 border ${errors["__NAME__"] ? "border-danger" : "border-gray-300"} rounded-md`}
              />
              __ERROR__
            </div>
""".strip("\n")

        return (
            tpl.replace("__NAME__", name)
               .replace("__REQ__", required_star)
               .replace("__ERROR__", error_msg)
        )

    # ====== EMAIL ======
    if T == "EMAIL":
        tpl = """
            {/* __NAME__ */}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{t("__NAME__")__REQ__}</label>
              <input
                type="email"
                {...register("__NAME__")}
                className={`w-full p-2 border ${errors["__NAME__"] ? "border-danger" : "border-gray-300"} rounded-md`}
              />
              __ERROR__
            </div>
""".strip("\n")

        return (
            tpl.replace("__NAME__", name)
               .replace("__REQ__", required_star)
               .replace("__ERROR__", error_msg)
        )

    # ====== default STRING/UUID/otros -> text ======
    tpl = """
            {/* __NAME__ */}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{t("__NAME__")__REQ__}</label>
              <input
                type="text"
                {...register("__NAME__")}
                className={`w-full p-2 border ${errors["__NAME__"] ? "border-danger" : "border-gray-300"} rounded-md`}
              />
              __ERROR__
            </div>
""".strip("\n")

    return (
        tpl.replace("__NAME__", name)
           .replace("__REQ__", required_star)
           .replace("__ERROR__", error_msg)
    )


def build_yup_schema_fields(columns: list[dict]) -> str:
    """
    columns.map(col => `${col.name}: ${toYupSchemaFor(col.type, required)}`).join(',\n    ')
    """
    lines = []
    for col in columns:
        required = col.get("allowNull") is False
        lines.append(f'{col["name"]}: {to_yup_schema_for(col.get("type"), required)}')
    return ",\n    ".join(lines)


def build_input_fields(columns: list[dict]) -> str:
    """
    columns.map(col => inputFor(col)).join('\\n')
    """
    return "\n".join(input_for(col) for col in columns)
