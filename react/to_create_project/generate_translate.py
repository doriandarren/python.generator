import os
from .utils import print_message, GREEN, CYAN, run_command





def create_folder(path):
    """Crea una carpeta si no existe."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Carpeta creada: {path}")



def generate_translate(full_path):
    setup_i18n(full_path)
    create_i18n(full_path)
    create_locales_en(full_path)
    create_locales_es(full_path)
    update_file_main(full_path)




def setup_i18n(full_path):
    """Instala ClassNames."""
    print_message("Instalando i18n...", CYAN)
    run_command("npm install i18next react-i18next i18next-http-backend i18next-browser-languagedetector", cwd=full_path)
    print_message("i18n instalado correctamente.", GREEN)




def create_i18n(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "src")
    file_path = os.path.join(pages_dir, "i18n.js")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido del archivo
    home_page_content = """import i18n from "i18next";
import { initReactI18next } from "react-i18next";
import LanguageDetector from "i18next-browser-languagedetector";
import HttpBackend from "i18next-http-backend";

const storedLang = localStorage.getItem("i18nextLng") || "es"

i18n
    .use(HttpBackend)
    .use(LanguageDetector)
    .use(initReactI18next)
    .init({
        lng: storedLang,
        fallbackLng: "es",
        debug: false,
        interpolation: {
            escapeValue: false,
        },
            detection: {
            order: ["querystring", "cookie", "localStorage", "navigator"],
            caches: ["cookie"],
        },
    })

export default i18n;
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(home_page_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")



def create_locales_es(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "public", "locales", "es")
    file_path = os.path.join(pages_dir, "translation.json")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido del archivo
    home_page_content = """{
  "welcome": "Bievendido!",
  "languages": {
    "en": "Inglés",
    "es": "Español"
  },
  "title": {
    "config": "Configuración"
  },
  "message":{
    "are_you_sure": "¿Estás seguro?",
    "record_saved": "Registro guardado",
    "record_deleted": "Registro eliminado",
    "record_updated": "Registro actualizado"
  },
  "menu": {
    "contact": "Contacto",
    "about": "¿Quienes somos?"
  },
  "login_page":{
    "title": "Bienvend@ Globalfleet",
    "subtitle": "Plataforma GlobalFleet Facturas.",
    "email_placeholder": "Correo electrónico",
    "password_placeholder": "Contraseña",
    "remember": "Recuérdame",
    "email" : "Correo electrónico",
    "password" : "Contraseña",
    "sign_in": "Acceder",
    "remember_me": "Recuerdame",
    "forgot_password": "Olvidaste la contraseña?",
    "forgot": "¿Olvidaste tu contraseña?",
    "btn_login": "Acceder",
    "register": "Registrarse",
    "or_continue_with": "Continuar con",
    "terms_txt1": "Al acceder estás de acuerdo con nuestros ",
    "terms_txt2": "Términos y Condiciones",
    "terms_txt3": "y nuestra",
    "terms_txt4": "Política de Privacidad",
    "credential_error": "Claves de acceso no válidas"
  },
  "privacity_polices": "Políticas de Privacidad",
  "link_interest": "Enlaces de interés",
  "login": "Login",
  "coockies": "Cookies",
  "page_not_found": "Página no encontrada",
  "actions": "Acciones",
  "dashboard": "Inicio",
  "logout": "Cerrar sesión",
  "profile": "Perfil",
  "resources": "Recursos",
  "home": "Inicio",
  "search": "Buscar",
  "save": "Guardar",
  "add": "Nuevo",
  "cancel": "Cancelar",
  "delete": "Borrar",
  "name": "Nombre",
  "yes": "Sí",
  "no": "No",
  "month": "Mes",
  "year": "Año",
  "insert": "Agregar",
  "setting": "Configuración",
  "setting_table":{
    "next_table": "Sig",
    "prev_table": "Prev",
    "rows_per_page": "Páginas",
    "of": "de",
    "search": "Buscar"
  },
  "form": {
    "required": "Requerido",
    "select": "Seleccione",
    "must_be_number": "Número"
  },
  "errors":{
    "error_internal": "Error Interno"
  },
  "error": "Error al procesar la información",
  "code": "Código",
  "address": "Dirección",
  "cif": "Código identificación fiscal",
  "email": "Correo electrónico",
  "website": "Sitio web",
  "phone": "Teléfono",
  "code_zip": "Código postal",
  "project_id": "Proyecto Id",
  "projects": "Proyectos",
  "hours": "Horas",
  "invoice_at": "Fecha factura",
  "customer_id": "Cliente",
  "invoices": "Facturas",
  "invoice": "Factura",
  "company_id": "Compañia Id",
  "company_name": "Razón social",
  "companies": "Compañias",
  "customer": "Cliente",
  "customers": "Clientes",
  "number": "Número",
  "date": "Fecha",
  "invoice_id": "Factura Id",
  "invoice_header_id": "Factura cabecera Id",
  "invoice_headers": "Facturas",
  "vat": "IVA",
  "unit_prices": "Precio unidad",
  "project_hours": "Horas proyecto",
  "total": "Total",
  "description": "Descripción",
  "project_hour_id": "Hora proyecto Id",
  "own_company_id": "Compañias propias Id",
  "own_companies": "Compañias propias",
  "total_hours": "Horas Totales",
  "current_hours": "Horas Actuales",
  "started_at": "Fecha Inicio",
  "finished_at": "Fecha Finalizado",
  "country_id": "País",
  "tax": "NIF",
  "state": "Estado",
  "municipality": "Municipio",
  "zip_code": "Codigo Postal",
  "is_generated": "Está Generado",
  "invoice_counter_id": "Serie",
  "invoice_lines": "Factura lineas",
  "due_date": "Fecha de Vencimiento",
  "vat_quote": "IVA",
  "total_without_vat": "Total sin IVA",
  "total_with_vat": "Total con IVA",
  "has_paid": "Pagada",
  "providers": "Proveedores",
  "products": "Productos",
  "services": "Servicios",
  "service": "Servicio",
  "invoice_counters": "Contadores",
  "amount_without_vat": "Importe sin IVA",
  "amount_with_vat": "Importe con IVA",
  "counter": "Contador",
  "serial": "Serial",
  "purchase_price_without_vat": "Precio de compra sin IVA",
  "sale_price_without_vat": "Precio de venta sin IVA",
  "invoiced_at": "Facturado",
  "path": "Ruta",
  "processed_at": "Procesado",
  "ims_invoice_headers": "Ficheros IMS",
  "provider_id": "Proveedor",
  "plate": "Matrícula",
  "customer_devices": "Dispositivos",
  "rental_price_without_vat": "Alquiler sin IVA",
  "provider_rental_price_without_vat": "Alquiler Prov. sin IVA",
  "installed_at": "Fecha de Instalación",
  "product_id": "Producto",
  "service_id": "Servicio",
  "code_ims": "Código IMS",
  "sim": "SIM",
  "file": "campo",
  "remittance_types": "Tipos de Remesas",
  "remittance_type_id": "Remesa",
  "invoice_date": "Fecha de factura",
  "invoice_due_date": "Fecha de Vencimiento",
  "vat_type": "Tipo de IVA",
  "invoice_counter": "Contador",
  "unit_nb": "Cantidad",
  "customer_data": "Datos",
  "customer_invoices": "Facturación cliente",
  "customers_invoices": "Facturas",
  "bank_account": " Cuenta bancaria",
  "bank_name": "Nombre del banco",
  "account_holder": "Titular de la cuenta",
  "due_date_by_days": "A cuantos días",
  "due_date_days": "Vencimiento el día",
  "customer_code": "Código de cliente",
  "team": "Equipo"
}
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(home_page_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")



def create_locales_en(project_path):
    """
    Genera el archivo
    """
    # Define la ruta del archivo
    pages_dir = os.path.join(project_path, "public", "locales", "en")
    file_path = os.path.join(pages_dir, "translation.json")

    # Crear la carpeta pages si no existe
    create_folder(pages_dir)

    # Contenido del archivo
    home_page_content = """{
  "welcome": "Welcome!",
  "languages": {
    "en": "English",
    "es": "Spanish"
  },
  "title": {
    "config": "Settings"
  },
  "message": {
    "are_you_sure": "Are you sure?",
    "record_saved": "Record saved",
    "record_deleted": "Record deleted",
    "record_updated": "Record updated"
  },
  "menu": {
    "contact": "Contact",
    "about": "About"
  },
  "login_page": {
    "title": "Welcome to GlobalFleet",
    "subtitle": "GlobalFleet Invoices Platform.",
    "email_placeholder": "Email",
    "password_placeholder": "Password",
    "remember": "Remember me",
    "email": "Email",
    "password": "Password",
    "sign_in": "Sign in",
    "remember_me": "Remember me",
    "forgot_password": "Forgot your password?",
    "forgot": "Forgot your password?",
    "btn_login": "Sign in",
    "register": "Create account",
    "or_continue_with": "Continue with",
    "terms_txt1": "By signing in, you agree to our ",
    "terms_txt2": "Terms and Conditions",
    "terms_txt3": " and our ",
    "terms_txt4": "Privacy Policy",
    "credential_error": "Invalid credentials"
  },
  "privacity_polices": "Privacy Policies",
  "link_interest": "Useful links",
  "login": "Login",
  "coockies": "Cookies",
  "page_not_found": "Page not found",
  "actions": "Actions",
  "dashboard": "Home",
  "logout": "Log out",
  "profile": "Your profile",
  "resources": "Resources",
  "home": "Home",
  "search": "Search",
  "save": "Save",
  "add": "New",
  "cancel": "Cancel",
  "delete": "Delete",
  "name": "Name",
  "yes": "Yes",
  "no": "No",
  "month": "Month",
  "year": "Year",
  "insert": "Add",
  "setting": "Settings",
  "setting_table": {
    "next_table": "Next",
    "prev_table": "Prev",
    "rows_per_page": "Pages",
    "of": "of",
    "search": "Search"
  },
  "form": {
    "required": "Required",
    "select": "Select",
    "must_be_number": "Number"
  },
  "errors": {
    "error_internal": "Internal Error"
  },
  "error": "Error processing the information",
  "code": "Code",
  "address": "Address",
  "cif": "Tax Identification Code",
  "email": "Email",
  "website": "Website",
  "phone": "Phone",
  "code_zip": "Zip Code",
  "project_id": "Project Id",
  "projects": "Projects",
  "hours": "Hours",
  "invoice_at": "Invoice Date",
  "customer_id": "Customer",
  "invoices": "Invoices",
  "invoice": "Invoice",
  "company_id": "Company Id",
  "company_name": "Company Name",
  "companies": "Companies",
  "customer": "Customer",
  "customers": "Customers",
  "number": "Number",
  "date": "Date",
  "invoice_id": "Invoice Id",
  "invoice_header_id": "Invoice Header Id",
  "invoice_headers": "Invoices",
  "vat": "VAT",
  "unit_prices": "Unit Price",
  "project_hours": "Project Hours",
  "total": "Total",
  "description": "Description",
  "project_hour_id": "Project Hour Id",
  "own_company_id": "Own Company Id",
  "own_companies": "Own Companies",
  "total_hours": "Total Hours",
  "current_hours": "Current Hours",
  "started_at": "Start Date",
  "finished_at": "End Date",
  "country_id": "Country",
  "tax": "Tax ID",
  "state": "State",
  "municipality": "Municipality",
  "zip_code": "Zip Code",
  "is_generated": "Is Generated",
  "invoice_counter_id": "Series",
  "invoice_lines": "Invoice Lines",
  "due_date": "Due Date",
  "vat_quote": "VAT",
  "total_without_vat": "Total without VAT",
  "total_with_vat": "Total with VAT",
  "has_paid": "Paid",
  "providers": "Providers",
  "products": "Products",
  "services": "Services",
  "service": "Service",
  "invoice_counters": "Counters",
  "amount_without_vat": "Amount without VAT",
  "amount_with_vat": "Amount with VAT",
  "counter": "Counter",
  "serial": "Serial",
  "purchase_price_without_vat": "Purchase Price without VAT",
  "sale_price_without_vat": "Sale Price without VAT",
  "invoiced_at": "Invoiced",
  "path": "Path",
  "processed_at": "Processed",
  "ims_invoice_headers": "IMS Files",
  "provider_id": "Provider",
  "plate": "Plate",
  "customer_devices": "Devices",
  "rental_price_without_vat": "Rental without VAT",
  "provider_rental_price_without_vat": "Provider Rental without VAT",
  "installed_at": "Installation Date",
  "product_id": "Product",
  "service_id": "Service",
  "code_ims": "IMS Code",
  "sim": "SIM",
  "file": "Field",
  "remittance_types": "Remittance Types",
  "remittance_type_id": "Remittance",
  "invoice_date": "Invoice Date",
  "invoice_due_date": "Due Date",
  "vat_type": "VAT Type",
  "invoice_counter": "Counter",
  "unit_nb": "Quantity",
  "customer_data": "Data",
  "customer_invoices": "Customer Billing",
  "customers_invoices": "Invoices",
  "bank_account": "Bank Account",
  "bank_name": "Bank Name",
  "account_holder": "Account Holder",
  "due_date_by_days": "Due in Days",
  "due_date_days": "Due Date",
  "customer_code": "Customer Code",
  "team": "Team"
}
"""

    # Crear el archivo y escribir el contenido
    try:
        with open(file_path, "w") as file:
            file.write(home_page_content)
        print(f"Archivo creado: {file_path}")
    except Exception as e:
        print(f"Error al crear el archivo {file_path}: {e}")



def update_file_main(full_path):
    """
    Actualiza el archivo src/main.jsx
    """
    main_jsx_path = os.path.join(full_path, "src", "main.jsx")

    # Verificar si el archivo existe
    if not os.path.exists(main_jsx_path):
        print_message(f"Error: {main_jsx_path} no existe.", CYAN)
        return

    try:

        # Leer el contenido del archivo
        with open(main_jsx_path, "r") as f:
            content = f.read()


        # Reemplazos
        content = content.replace(
            "import { createRoot } from 'react-dom/client'",
            "import { createRoot } from \'react-dom/client\';\nimport \'./i18n\';"
        )

        # Escribir el contenido actualizado
        with open(main_jsx_path, "w") as f:
            f.write(content)

        print_message("main.jsx configurado correctamente.", GREEN)

    except Exception as e:
        print_message(f"Error al actualizar {main_jsx_path}: {e}", CYAN)


