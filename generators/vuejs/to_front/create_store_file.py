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


def generate_store_file(base_ruta, path_component, singular_name, plural_name, singular_name_kebab, plural_name_kebab, singular_name_snake, plural_name_snake, columns):
    """
    Genera un archivo Vue.js basado en los nombres proporcionados y crea la estructura de la carpeta src/modules/path_component dentro de base_ruta.
    """
    # Crear la estructura de carpetas llamando a create_component_structure
    component_folder_path = create_component_structure(base_ruta, path_component)

    # Nombre del archivo será en singular, por ejemplo: InvoiceHeaderStore.vue
    file_name = f'{singular_name}Create.vue'
    component_file_path = os.path.join(component_folder_path, file_name)

    # Obtener los nombres de las columnas dinámicamente para usarlas en el formulario
    form_fields = ""
    validation_rules = ""
    reactive_data = ""

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

        validation_rules += f"""
        {field_name}: {{
            required: helpers.withMessage(t("form.required"), required),
        }},
        """

        reactive_data += f"        {field_name}: '',\n"

    # Contenido del archivo Vue.js
    component_content = f"""
<template>

    <!-- BEGIN: Card -->
    <div class="card">
        <!-- BEGIN: Form -->
        <form @submit.prevent="save">

            <!-- BEGIN: container -->
            <div class="grid grid-cols-12 gap-6">
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
                        <button @click.prevent="emit('cancelCreate')" class="btn btn-danger">
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
    import {{ required }} from '@vuelidate/validators';
    import {{ useVuelidate }} from '@vuelidate/core';
    import {{ helpers }} from '@vuelidate/validators';
    import {{ useI18n }} from 'vue-i18n';
    import IconSave from '@/components/icons/IconSave.vue';
    import IconCancel from '@/components/icons/IconCancel.vue';

    const { singular_name_snake } = reactive({{
{reactive_data}
    }});

    const rules = {{
        {validation_rules}
    }};

    const validate = useVuelidate(rules, {{ {singular_name_snake} }});

    const save = () => {{
        validate.value.$touch();
        if (validate.value.$invalid) {{
            // TODO: handle invalid form
        }} else {{
            emit('saveInvoiceHeaderForm', {{ ...{singular_name_snake} }});
        }}
    }};

    onMounted(async () => {{
        // TODO: Implement on mount logic
    }});

</script>
"""

    # Escribir el archivo Vue.js
    try:
        with open(component_file_path, 'w') as component_file:
            component_file.write(component_content)
            print(f"Archivo Vue '{file_name}' creado en: {component_folder_path}")
    except Exception as e:
        print(f"Error al crear el archivo Vue '{file_name}': {e}")
