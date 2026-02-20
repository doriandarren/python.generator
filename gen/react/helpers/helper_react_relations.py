# helpers/helper_react_relations.py
# Conversión de helpers/helperReactRelations.js a Python
# (generadores de strings para inyectar en templates JSX)

import re
from typing import List, Dict


# ---------- helpers de nombres ----------
def base_from_field(field_name: str = "") -> str:
    # fieldName.replace(/_?id$/i, "")
    return re.sub(r"_?id$", "", field_name or "", flags=re.IGNORECASE)


def to_pascal(s: str = "") -> str:
    # s.replace(/[-_\s]+/g, " ").replace(/\w+/g, ...).replace(/\s+/g, "")
    s = s or ""
    s = re.sub(r"[-_\s]+", " ", s.strip())
    words = re.findall(r"\w+", s)
    return "".join(w[:1].upper() + w[1:].lower() for w in words)


def to_camel(s: str = "") -> str:
    p = to_pascal(s)
    return (p[:1].lower() + p[1:]) if p else ""


def pluralize(s: str = "") -> str:
    if not s:
        return ""
    if re.search(r"[sxz]$", s, flags=re.IGNORECASE) or re.search(r"(sh|ch)$", s, flags=re.IGNORECASE):
        return s + "es"
    if re.search(r"y$", s, flags=re.IGNORECASE):
        return re.sub(r"y$", "ies", s, flags=re.IGNORECASE)
    return s + "s"


# ---------- detector de FK ----------
def is_fk(c: Dict) -> bool:
    return (c.get("type") or "").upper() == "FK"


def has_fk(columns: List[Dict] = None) -> bool:
    columns = columns or []
    return any(is_fk(c) for c in columns)


# ---------- builder de variables ----------
def build_variables(columns: List[Dict] = None) -> str:
    """
    Devuelve un string listo para inyectar tras isLoading (uno por cada FK)
    """
    columns = columns or []
    fks = [c for c in columns if is_fk(c)]
    if not fks:
        return ""

    blocks = []
    for c in fks:
        name = c.get("name", "")
        base = base_from_field(name)              # "customer"
        pascal = to_pascal(base)                  # "Customer"
        options_var = to_camel(pluralize(base))   # "customers"

        block = f"""
  // {pascal}
  const [{options_var}, set{to_pascal(options_var)}] = useState([]);
  const [selected{pascal}, setSelected{pascal}] = useState(null);
  const onChange{pascal} = () => {{}};
""".rstrip()

        blocks.append(block)

    return "\n".join(blocks)


# =========================
# Helpers para ComboBox
# =========================
def build_combobox_import(columns: List[Dict] = None) -> str:
    """
    - Import del ComboBox (una sola vez)
    - Un import de servicio por cada FK
    Devuelve con salto de línea inicial: "\nimport ...\nimport ..."
    """
    columns = columns or []
    fks = [c for c in columns if is_fk(c)]
    if not fks:
        return ""

    lines = []
    seen = set()

    def add(line: str):
        if line not in seen:
            seen.add(line)
            lines.append(line)

    add('import ThemedComboBox from "../../../components/ComboBoxes/ThemedComboBox";')

    for c in fks:
        name = c.get("name", "")
        base = base_from_field(name)           # "customer"
        plural = pluralize(base)               # "customers"
        getter = f"get{to_pascal(plural)}"     # "getCustomers"
        format_url = to_camel(base)            # "customer"

        service_path = f'../../{plural}/services/{format_url}Service'
        add(f'import {{ {getter} }} from "{service_path}";')

    return "\n" + "\n".join(lines)


def build_combobox_use_effect(columns: List[Dict] = None) -> str:
    """
    useEffect de carga para todas las FKs detectadas
    """
    columns = columns or []
    fks = [c for c in columns if is_fk(c)]
    if not fks:
        return ""

    items = []
    for c in fks:
        name = c.get("name", "")
        base = base_from_field(name)
        plural = pluralize(base)
        getter = f"get{to_pascal(plural)}"
        options_var = to_camel(plural)
        set_options = f"set{to_pascal(options_var)}"
        pascal = to_pascal(base)
        items.append({
            "name": name,
            "base": base,
            "plural": plural,
            "getter": getter,
            "optionsVar": options_var,
            "setOptions": set_options,
            "pascal": pascal
        })

    res_names = ", ".join(f'{it["optionsVar"]}Res' for it in items)
    promise_calls = ", ".join(f'{it["getter"]}()' for it in items)

    per_fk_assign = "\n".join(
        f"""
      if ({it["optionsVar"]}Res?.success) {{
        {it["setOptions"]}({it["optionsVar"]}Res.data);
        
        // TODO default:
        // const x = {it["optionsVar"]}Res.data.find( x => x.id === 64 );
        // setSelected{it["pascal"]}(x);
        // setValue("{it["name"]}", x?.id, {{shouldValidate: true,}});

      }} else {{
        Swal.fire({{
          title: t("error"),
          icon: "error",
          confirmButtonText: t("message.ok"),
          confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_ERROR,
        }});
      }}""".rstrip()
        for it in items
    )

    return f"""
  useEffect(() => {{
    const fetchData = async () => {{
      try {{
        const [{res_names}] = await Promise.all([{promise_calls}]);

{per_fk_assign}
      }} catch (error) {{
       console.error("Error al enviar los datos:", error);
        Swal.fire({{
          title: t("errors.error_process"),
          icon: "error",
          confirmButtonText: t("message.ok"),
          confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_ERROR,
        }});
      }}
    }};

    fetchData();
  }}, [t]);""".rstrip()


def build_edit_fetch_pieces(columns: List[Dict] = None) -> Dict[str, str]:
    """
    Para EDIT:
    - resNames: "customersRes, suppliersRes"
    - promiseCalls: "getCustomers(), getSuppliers()"
    - fkLoadBlocks: if (...) setOptions(...); else Swal(ERROR)
    - fkSelectBlocks: setSelectedX(res.data.find(... por data.<fk_id>))
    """
    columns = columns or []
    fks = [c for c in columns if is_fk(c)]
    if not fks:
        return {"resNames": "", "promiseCalls": "", "fkLoadBlocks": "", "fkSelectBlocks": ""}

    items = []
    for c in fks:
        name = c.get("name", "")
        base = base_from_field(name)
        plural = pluralize(base)
        getter = f"get{to_pascal(plural)}"
        options_var = to_camel(plural)
        set_options = f"set{to_pascal(options_var)}"
        pascal = to_pascal(base)
        selected_setter = f"setSelected{pascal}"
        res_name = f"{options_var}Res"

        items.append({
            "name": name,
            "getter": getter,
            "optionsVar": options_var,
            "setOptions": set_options,
            "selectedSetter": selected_setter,
            "resName": res_name
        })

    res_names = ", ".join(i["resName"] for i in items)
    promise_calls = ", ".join(f'{i["getter"]}()' for i in items)

    fk_load_blocks = "\n".join(
        f"""
        if ({i["resName"]}?.success) {{

          {i["setOptions"]}({i["resName"]}.data);
          
        }} else {{
          Swal.fire({{
            title: t("error"),
            icon: "error",
            confirmButtonText: t("message.ok"),
            confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_ERROR,
          }});
        }}""".rstrip()
        for i in items
    )

    fk_select_blocks = "\n".join(
        f"""
          // {i["name"]}
          {i["selectedSetter"]}({i["resName"]}.data?.find(x => x?.id === data.{i["name"]}) ?? null);""".rstrip()
        for i in items
    )

    return {
        "resNames": res_names,
        "promiseCalls": promise_calls,
        "fkLoadBlocks": fk_load_blocks,
        "fkSelectBlocks": fk_select_blocks
    }


# =========================
# Helpers para BOOLEAN
# =========================
def is_boolean(c: Dict) -> bool:
    return (c.get("type") or "").upper() == "BOOLEAN"


def has_boolean(columns: List[Dict] = None) -> bool:
    columns = columns or []
    return any(is_boolean(c) for c in columns)


def build_boolean_import(columns: List[Dict] = None) -> str:
    return '\nimport { ThemedToggle } from "../../../components/Toggles/ThemedToggle";' if has_boolean(columns or []) else ""


def build_boolean_default_values_prop(columns: List[Dict] = None) -> str:
    """
    Devuelve string para pegar dentro de useForm:
    defaultValues: { "a": 0, "b": 0 },
    """
    columns = columns or []
    names = [c.get("name") for c in columns if is_boolean(c)]
    names = [n for n in names if n]
    if not names:
        return ""

    inner = ", ".join(f'"{n}": 0' for n in names)
    return f"defaultValues: {{ {inner} }},"


def build_boolean_edit_set_values(columns: List[Dict] = None, data_var: str = "data") -> str:
    """
    Genera líneas setValue para todos los BOOLEAN:
    setValue("<field>", Number(data.<field> ?? 0));
    """
    columns = columns or []
    names = [c.get("name") for c in columns if is_boolean(c)]
    names = [n for n in names if n]
    if not names:
        return ""

    return "\n          ".join(
        f'setValue("{n}", Number({data_var}.{n} ?? 0));'
        for n in names
    )
