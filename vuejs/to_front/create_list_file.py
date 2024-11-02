import os

def create_list_structure(base_ruta, path_views):
    """
    Crea la estructura de carpetas 'base_ruta/path_views' en la ruta especificada.
    """
    # Crear la ruta completa base_ruta/path_views
    list_folder_path = os.path.join(base_ruta, path_views)

    if not os.path.exists(list_folder_path):
        os.makedirs(list_folder_path)
        print(f"Estructura de carpetas '{list_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{list_folder_path}' ya existe.")

    return list_folder_path

def generate_list_file(base_ruta, path_views, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns, singular_name_first_lower, plural_name_first_lower):
    """
    Genera un archivo de lista de Vue.js basado en los nombres proporcionados y crea la estructura dentro de base_ruta/path_views.
    """
    # Crear la estructura de carpetas llamando a create_list_structure
    list_folder_path = create_list_structure(base_ruta, path_views)

    # Nombre del archivo Vue.js será en el formato InvoiceHeaderList.vue
    file_name = f'{singular_name}List.vue'
    list_file_path = os.path.join(list_folder_path, file_name)

    # Construir el contenido del archivo Vue.js
    vue_content = f"""<template>

    <!-- BEGIN: Page Layout Create -->
    <div v-animate v-if="isCreate">
        <Create
            @save{singular_name}Form="save{singular_name}Form"
            @cancelCreate="cancelCreate"
        />
    </div>

    <!-- BEGIN: Page Layout Update -->
    <div v-animate v-if="isEdit">
        <Edit
            :{singular_name_snake}Id="{singular_name_snake}Id"
            @cancelEdit="cancelEdit"
            @update{singular_name}Form="update{singular_name}Form"
        />
    </div>

    <!-- BEGIN: Table -->
    <div v-animate id="div_table">
        <div class="flex flex-col sm:flex-row xl:items-start justify-between mb-5">
            <h1 class="mt-0">{{{{ $t("{plural_name_snake}") }}}}</h1>
            <button class="btn-primary sm:w-auto" @click.prevent="showCreate{singular_name}">
                <div class="flex flex-row">
                    <IconAdd />
                    {{{{ $t("add") }}}}
                </div>
            </button>
        </div>

        <!-- BEGIN: Table -->
        <div class="p-5 border rounded-md shadow-sm">
            <div class="overflow-x-auto scrollbar-hidden">
                <VueGoodTable
                    :columns="columns"
                    :rows="rows"
                    :pagination-options="{{
                        enabled: true,
                        mode: 'records',
                        perPage: 5,
                        perPageDropdown: [10, 20, 50],
                        dropdownAllowAll: false,
                        setCurrentPage: 1,
                        nextLabel: $t('setting_table.next_table'),
                        prevLabel: $t('setting_table.prev_table'),
                        rowsPerPageLabel: $t('setting_table.rows_per_page'),
                        ofLabel: $t('setting_table.of'),
                        pageLabel: 'page',
                        allLabel: 'All',
                    }}"
                    :search-options="{{ enabled: true, placeholder: $t('setting_table.search') }}"
                >
                    <template #table-row="props">
                        <span v-if="props.column.field == 'actions'">
                            <button @click="showEdit{singular_name}(props.row.id)">
                                <IconEdit />
                            </button>
                            <button @click="showDelete{singular_name}(props.row.id)">
                                <IconDelete />
                            </button>
                        </span>
                    </template>
                </VueGoodTable>
            </div>
        </div>
    </div>

</template>

<script setup>
import {{ ref, onMounted, toRaw }} from 'vue';
import {{ useI18n }} from 'vue-i18n';
import {{ Toast }} from '@/utils/toast';
import Swal from 'sweetalert2';
import IconAdd from '@/components/icons/IconAdd.vue';
import IconEdit from '@/components/icons/IconEdit.vue';
import IconDelete from '@/components/icons/IconDelete.vue';
import use{singular_name} from "../../composables/{singular_name_snake}s";
import Create from "../../components/{singular_name_snake}s/{singular_name}Create.vue";
import Edit from "../../components/{singular_name_snake}s/{singular_name}Edit.vue";

// Tabulator
const rows = ref([]);

// Views
const isCreate = ref(false);
const isEdit = ref(false);
const {singular_name_snake}Id = ref(0);

const {{ t }} = useI18n();
const {{ {singular_name_snake}s, {singular_name_first_lower}Errors, get{plural_name}, store{singular_name}, update{singular_name}, destroy{singular_name} }} = use{singular_name}();

const findData = async () => {{
    await get{plural_name}();
    return toRaw({singular_name_snake}s.value);
}}

// Table
const columns = [
"""
    for column in columns:
        vue_content += f"""    {{ label: t("{column['name']}"), field: '{column['name']}' }},
"""
    vue_content += f"""
    {{ label: t('actions'), field: 'actions', sortable: false, searchable: false, width: '100px' }},
];

//Store
const showCreate{singular_name} = () => {{
    isCreate.value = true;
    div_table.style.display = 'none';
}}

const cancelCreate = () => {{
    isCreate.value = false;
    div_table.style.display = 'block';
}}

const save{singular_name}Form = async (form) => {{
    isCreate.value = false;
    div_table.style.display = 'block';
    await store{singular_name}({{ ...form }});
    if ({singular_name_first_lower}Errors.value.length === 0) {{
        await Toast(t("message.record_saved"), 'success');
    }} else {{
        const errorMessages = {singular_name_first_lower}Errors.value.flatMap(errorObj => Object.values(errorObj).flat()).join(', ');
        await Toast(errorMessages, 'error');
    }}
    rows.value = await findData();
}}

// Edit
const showEdit{singular_name} = (id) => {{
    isEdit.value = true;
    div_table.style.display = 'none';
    {singular_name_snake}Id.value = id;
}}

const cancelEdit = async () => {{
    isEdit.value = false;
    div_table.style.display = 'block';
}}

const update{singular_name}Form = async (id, data) => {{
    isEdit.value = false;
    div_table.style.display = 'block';
    await update{singular_name}(id, data);
    if ({singular_name_first_lower}Errors.value.length === 0) {{
        await Toast(t("message.record_updated"), 'success');
    }} else {{
        const errorMessages = {singular_name_first_lower}Errors.value.flatMap(errorObj => Object.values(errorObj).flat()).join(', ');
        await Toast(errorMessages, 'error');
    }}
    rows.value = await findData();
}}

// Delete
const showDelete{singular_name} = async (id, description = '') => {{
    Swal.fire({{
        icon: 'warning',
        title: t("message.are_you_sure"),
        text: t("delete") + (description !== '' ? ': ' + description : ''),
        showCancelButton: true,
        confirmButtonText: t("delete"),
        confirmButtonColor: import.meta.env.VITE_SWEETALERT_COLOR_BTN_SUCCESS,
    }}).then(async (result) => {{
        if (result.isConfirmed) {{
            await destroy{singular_name}(id);
            if ({singular_name_first_lower}Errors.value.length === 0) {{
                await Toast(t("message.record_deleted"), 'success');
            }} else {{
                const errorMessages = {singular_name_first_lower}Errors.value.flatMap(errorObj => Object.values(errorObj).flat()).join(', ');
                await Toast(errorMessages, 'error');
            }}
            rows.value = await findData();
        }}
    }});
}}

onMounted(async () => {{
    rows.value = await findData();
}});
</script>

<style scoped>
</style>
"""

    # Escribir el archivo Vue.js con el contenido generado
    try:
        with open(list_file_path, 'w') as list_file:
            list_file.write(vue_content.strip())
            print(f"Archivo Vue.js '{file_name}' creado en: {list_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo Vue.js '{file_name}': {e}")
