import re


# snake.case / dot.notation -> PascalCase (para nombres de estado: qCustomerCompanyName)
def to_var_suffix(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", s)
    # Capitaliza tras inicio o "_"
    return re.sub(r"(^|_)(\w)", lambda m: m.group(2).upper(), s)


# Limpia sufijo _id para etiquetas i18n
def clean_name(name: str) -> str:
    return re.sub(r"_id$", "", name)


# Heurística: columnas con "customer" un poco más anchas
def span_for(name: str) -> int:
    return 4 if "customer" in name else 3


def unique_keep_order(items):
    # equivalente a [...new Set(items)] preservando orden
    return list(dict.fromkeys(items))


# Genera el bloque de <div> con inputs por cada columna
def build_filter_blocks(column_names):
    unique_cols = unique_keep_order(column_names)

    blocks = []
    for name in unique_cols:
        pascal = to_var_suffix(name)
        span = span_for(name)
        ph_key = f"search_by_{clean_name(name)}"

        block = f"""
          <div className="md:col-span-{span}">
            <input
              type="text"
              value={{q{pascal}}}
              onChange={{(e) => setQ{pascal}(e.target.value)}}
              className="w-full border border-gray-300 rounded-lg p-2 bg-white"
              placeholder={{t("{clean_name(name)}")}}
            />
          </div>""".strip()

        blocks.append(block)

    return "\n".join(blocks)


# Función que construye la función JSX `renderFilters` (como string para el template)
def build_render_filters_fn(column_names):
    blocks = build_filter_blocks(column_names)

    return f"""
      <div className="border border-gray-200 shadow-sm rounded-xl px-4 py-4 mb-5 bg-gray-200/30">
        <div className="grid grid-cols-1 md:grid-cols-12 gap-3">
{blocks}
          <div className="md:col-span-2 flex items-end">
            <ThemedButton variant="warning" type="button" onClick={{resetFilters}} className="w-full">
              {{t("clear_filters")}}
            </ThemedButton>
          </div>
        </div>
      </div>
    """


# Estados de filtros (qX / setQX) para TODAS las columnas
def build_filters_state(column_names):
    unique_cols = unique_keep_order(column_names)
    return "\n  ".join(
        [f'const [q{to_var_suffix(name)}, setQ{to_var_suffix(name)}] = useState("");' for name in unique_cols]
    )


# Cuerpo del reset (setters a "")
def build_reset_filters_body(column_names):
    unique_cols = unique_keep_order(column_names)
    return "\n".join(
        [f'    setQ{to_var_suffix(name)}("");' for name in unique_cols]
    )


# Objeto para el service: { col: qCol, ... }
def build_filters_object(column_names, indent="          "):
    unique_cols = unique_keep_order(column_names)
    return "\n".join(
        [f"{indent}{name}: q{to_var_suffix(name)}," for name in unique_cols]
    )


# Dependencias del useEffect
def build_effect_deps(column_names):
    unique_cols = unique_keep_order(column_names)
    return ", ".join(
        [f"q{to_var_suffix(name)}" for name in unique_cols]
    )
