import re


def base_from_field(field_name: str) -> str:
    # (fieldName || "").replace(/_?id$/i, "")
    return re.sub(r"_?id$", "", (field_name or ""), flags=re.IGNORECASE)


def to_pascal(s: str) -> str:
    # s.replace(/[-_\s]+/g, " ")
    #  .replace(/\w+/g, w => w[0].toUpperCase() + w.slice(1).toLowerCase())
    #  .replace(/\s+/g, "");
    s = re.sub(r"[-_\s]+", " ", s or "")
    words = re.findall(r"\w+", s)
    pascal = "".join([w[:1].upper() + w[1:].lower() if w else "" for w in words])
    return pascal


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


# Devuelve el encadenado de Yup como string
def to_yup_schema_for(col_type: str, required: bool) -> str:
    T = (col_type or "STRING").upper()

    base = (
        'yup.number().oneOf([0,1])' if T == "BOOLEAN" else
        'yup.number().typeError(t("form.number")).integer()' if T in ("INTEGER", "INT", "BIGINT") else
        'yup.number().typeError(t("form.number"))' if T in ("FLOAT", "DOUBLE", "DECIMAL", "NUMERIC") else
        'yup.string().required(t("form.required"))' if T == "DATE" else
        'yup.string().required(t("form.required"))' if T in ("DATETIME", "TIMESTAMP") else
        'yup.string().email(t("form.email"))' if T == "EMAIL" else
        'yup.string()' if T == "UUID" else
        'yup.mixed()' if T in ("JSON", "FK") else
        'yup.string(t("form.required"))'
    )

    # base += required ? '.required(...)' : '.nullable()'
    base += '.required(t("form.required"))' if required else ".nullable()"
    return base


# Devuelve el bloque JSX como string para un campo concreto
def input_for(col: dict) -> str:
    name = col.get("name")
    T = (col.get("type") or "STRING").upper()

    # {errors.name && <p ...>{errors.name?.message}</p>}
    error_msg = f'{{errors.{name} && <p className="text-danger text-sm">{{errors.{name}?.message}}</p>}}'

    required_star = ' + " *"' if col.get("allowNull") is False else ""

    # ====== FK con ThemedComboBox ======
    if T == "FK":
        base = base_from_field(name)                # customer_id -> customer
        pascal = to_pascal(base)                    # Customer
        options_var = to_camel(pluralize(base))     # customers
        selected_var = f"selected{pascal}"          # selectedCustomer
        set_selected_var = f"setSelected{pascal}"   # setSelectedCustomer
        on_change_var = f"onChange{pascal}"         # onChangeCustomer

        return f"""
            {{/* {name} */}}
            <div className="col-span-12 md:col-span-6 lg:col-span-6">
              <ThemedComboBox
                label={{t("{base}"){required_star}}}
                options={{{options_var}}}
                selected={{{selected_var}}}
                setSelected={{(item) => {{
                  {set_selected_var}(item);
                  setValue("{name}", item?.id, {{ shouldValidate: true }});
                }}}}
                error={{errors.{name}?.message}}
                getLabel={{(item) =>
                  `{{${{item?.name ?? ""}}}}`.trim()
                }}
                onChange={{(value) => {on_change_var}(value)}}
              />
            </div>""".rstrip()

    # ====== BOOLEAN con ThemedToggle ======
    if T == "BOOLEAN":
        return f"""
            {{/* {name} */}}
            <div className="col-span-12 md:col-span-3 lg:col-span-3">
              <ThemedToggle
                label={{t("{name}"){required_star}}}
                enabled={{watch("{name}") === 1}}
                setEnabled={{(value) =>
                  setValue("{name}", value ? 1 : 0, {{ shouldValidate: true }})
                }}
                error={{errors.{name}?.message}}
              />
              <input type="hidden" {{...register("{name}")}} />
            </div>""".rstrip()

    # TEXT / JSON -> textarea
    if T in ("TEXT", "JSON"):
        return f"""
            {{/* {name} */}}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{{t("{name}"){required_star}}}</label>
              <textarea
                rows={{4}}
                {{...register("{name}")}}
                className={{`w-full p-2 border ${{errors["{name}"] ? "border-danger" : "border-gray-300"}} rounded-md`}}
              />
              {error_msg}
            </div>""".rstrip()

    # INTEGER/INT/BIGINT -> number step 1
    if T in ("INTEGER", "INT", "BIGINT"):
        return f"""
            {{/* {name} */}}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{{t("{name}"){required_star}}}</label>
              <input
                type="number"
                step="1"
                {{...register("{name}", {{ valueAsNumber: true }})}}
                className={{`w-full p-2 border ${{errors["{name}"] ? "border-danger" : "border-gray-300"}} rounded-md`}}
              />
              {error_msg}
            </div>""".rstrip()

    # FLOAT/DOUBLE/DECIMAL/NUMERIC -> number step any
    if T in ("FLOAT", "DOUBLE", "DECIMAL", "NUMERIC"):
        return f"""
            {{/* {name} */}}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{{t("{name}"){required_star}}}</label>
              <input
                type="number"
                step="any"
                {{...register("{name}", {{ valueAsNumber: true }})}}
                className={{`w-full p-2 border ${{errors["{name}"] ? "border-danger" : "border-gray-300"}} rounded-md`}}
              />
              {error_msg}
            </div>""".rstrip()

    # DATE -> date input
    if T == "DATE":
        return f"""
            {{/* {name} */}}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{{t("{name}"){required_star}}}</label>
              <input
                type="date"
                {{...register("{name}")}}
                className={{`w-full p-2 border ${{errors["{name}"] ? "border-danger" : "border-gray-300"}} rounded-md`}}
              />
              {error_msg}
            </div>""".rstrip()

    # DATETIME/TIMESTAMP -> datetime-local input
    if T in ("DATETIME", "TIMESTAMP"):
        return f"""
            {{/* {name} */}}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{{t("{name}"){required_star}}}</label>
              <input
                type="datetime-local"
                {{...register("{name}")}}
                className={{`w-full p-2 border ${{errors["{name}"] ? "border-danger" : "border-gray-300"}} rounded-md`}}
              />
              {error_msg}
            </div>""".rstrip()

    # EMAIL -> email input
    if T == "EMAIL":
        return f"""
            {{/* {name} */}}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{{t("{name}"){required_star}}}</label>
              <input
                type="email"
                {{...register("{name}")}}
                className={{`w-full p-2 border ${{errors["{name}"] ? "border-danger" : "border-gray-300"}} rounded-md`}}
              />
              {error_msg}
            </div>""".rstrip()

    # default STRING/UUID/otros -> text
    return f"""
            {{/* {name} */}}
            <div className="col-span-12 md:col-span-6 lg:col-span-4">
              <label className="block text-gray-700">{{t("{name}"){required_star}}}</label>
              <input
                type="text"
                {{...register("{name}")}}
                className={{`w-full p-2 border ${{errors["{name}"] ? "border-danger" : "border-gray-300"}} rounded-md`}}
              />
              {error_msg}
            </div>""".rstrip()


# Builders de bloques completos
def build_yup_schema_fields(columns) -> str:
    parts = []
    for col in columns:
        required = col.get("allowNull") is False
        parts.append(f'{col.get("name")}: {to_yup_schema_for(col.get("type"), required)}')
    return ",\n    ".join(parts)


def build_input_fields(columns) -> str:
    return "\n".join([input_for(col) for col in columns])
