import os

def create_component_structure(base_ruta, path_component):
    """
    Crea la estructura de carpetas 'base_ruta/src/modules/path_component' en la ruta especificada.
    """
    # Crear la ruta completa base_ruta/src/modules/path_component
    component_folder_path = os.path.join(base_ruta, path_component)

    if not os.path.exists(component_folder_path):
        os.makedirs(component_folder_path)
        print(f"Estructura de carpetas '{component_folder_path}' creada.")
    else:
        print(f"Estructura de carpetas '{component_folder_path}' ya existe.")

    return component_folder_path


def generate_update_file(base_ruta, path_component, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns, singular_name_first_lower, plural_name_first_lower):
    """
    Genera un archivo de actualización en Vue.js basado en los nombres proporcionados y crea la estructura en base_ruta/path_component.
    """
    # Crear la estructura de carpetas
    component_folder_path = create_component_structure(base_ruta, path_component)

    # Nombre del archivo Vue será igual a singular_name
    file_name = f'{singular_name}Update.vue'
    component_file_path = os.path.join(component_folder_path, file_name)

    # Construir la lista de campos en `rules`
    validation_rules = ""
    for column in columns:
        field_name = column["name"]
        validation_rules += f"        {field_name}: {{\n"
        validation_rules += f"            required: helpers.withMessage(t('form.required'), required),\n"
        validation_rules += "        },\n"

    # Construir la lista de datos reactivos en `formData`
    reactive_data = ""
    for column in columns:
        field_name = column["name"]
        reactive_data += f"        {field_name}: '',\n"

    # Construir la asignación de datos dentro de `onMounted`
    on_mounted_data = ""
    for column in columns:
        field_name = column["name"]
        on_mounted_data += f"        formData.{field_name} = {singular_name_snake}.value.{field_name};\n"

    # Generar campos de formulario dinámicamente en el template
    form_fields = ""
    for column in columns:
        field_name = column["name"]
        form_fields += f"""
                <div class="col-span-12 md:col-span-6 lg:col-span-4">
                    <div class="input-form">
                        <label for="{field_name}" class="form-label w-full">
                             {{{{ $t("{field_name}") }}}} *
                        </label>
                        <input
                            v-model.trim="validate.{field_name}.$model"
                            id="{field_name}"
                            type="text"
                            name="{field_name}"
                            class="form-control"
                            :class="{{ 'border-danger': validate.{field_name}.$error }}"
                        />
                        <template v-if="validate.{field_name}.$error">
                            <div v-for="(error, index) in validate.{field_name}.$errors" :key="index" class="text-danger mt-2">
                                {{{{ error.$message }}}}
                            </div>
                        </template>
                    </div>
                </div>
        """

    # Contenido del archivo Vue.js
    vue_content = f"""<template>

    <!-- BEGIN: Card -->
    <div class="card">
        <!-- BEGIN: Form -->
        <form class="validate-form" @submit.prevent="save">

            <!-- BEGIN: container -->
            <div class="grid grid-cols-12 gap-6">

                <!-- Form fields -->
                {form_fields}

                <!-- BEGIN: Buttons -->
                <div class="col-span-12 md:col-span-12 lg:col-span-12">
                    <div class="flex justify-center">
                        <button type="submit" class="btn btn-primary mr-5">
                            <div class="flex">
                                <IconSave />
                                {{{{ $t("save") }}}}
                            </div>
                        </button>
                        <button @click.prevent="emit('cancelEdit')" class="btn btn-danger">
                            <div class="flex">
                                <IconCancel />
                                {{{{ $t("cancel") }}}}
                            </div>
                        </button>
                    </div>
                </div>
                <!-- END: Buttons -->

            </div>
            <!-- END: container -->

        </form>
        <!-- END: Form -->

    </div>
    <!-- END: Card -->

</template>


<script setup>

    import {{ onMounted, reactive, toRefs }} from 'vue';
    import use{plural_name} from '../../composables/{plural_name_snake}';
    import {{ required, helpers }} from '@vuelidate/validators';
    import {{ useVuelidate }} from '@vuelidate/core';
    import {{ useI18n }} from 'vue-i18n';
    import IconSave from '@/components/icons/IconSave.vue';
    import IconCancel from '@/components/icons/IconCancel.vue';

    const {{ {singular_name_first_lower}, get{singular_name} }} = use{plural_name}();
    const {{ t }} = useI18n();
    const props = defineProps(['{singular_name_first_lower}Id']);
    const emit = defineEmits(['cancelEdit', 'update{singular_name}Form']);

    const rules = {{
{validation_rules}
    }};

    const formData = reactive({{
{reactive_data}
    }});

    const validate = useVuelidate(rules, toRefs(formData));

    const save = () => {{
        validate.value.$touch();
        if (validate.value.$invalid) {{
            //TODO: manejar validación
        }} else {{
            emit('update{singular_name}Form', {singular_name_first_lower}.value.id, formData);
        }}
    }};

    onMounted(async () => {{
        await get{singular_name}(props.{singular_name_first_lower}Id);
{on_mounted_data}
    }});

</script>
"""

    # Escribir el archivo Vue.js con el contenido
    try:
        with open(component_file_path, 'w') as component_file:
            component_file.write(vue_content)
            print(f"Archivo Vue '{file_name}' creado en: {component_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo Vue '{file_name}': {e}")

