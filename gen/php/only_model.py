
from gen.php.to_module_crud.generate_model_file import generate_model_file
from gen.helpers.helper_print import input_with_validation, print_header







if __name__ == '__main__':
    print_header("PHP")

    extracted_models = [{'plural_name_snake': 'washes_invoice_subtotals',
  'singular_name': 'WashesInvoiceSubtotal',
  'plural_name': 'WashesInvoiceSubtotals'},
 {'plural_name_snake': 'washes_payment_modes',
  'singular_name': 'WashesPaymentMode',
  'plural_name': 'WashesPaymentModes'},
 {'plural_name_snake': 'wash_customer_plates_authorizations',
  'singular_name': 'WashCustomerPlatesAuthorization',
  'plural_name': 'WashCustomerPlatesAuthorizations'},
 {'plural_name_snake': 'wash_customer_codes',
  'singular_name': 'WashCustomerCode',
  'plural_name': 'WashCustomerCodes'},
 {'plural_name_snake': 'wash_risk_customers',
  'singular_name': 'WashRiskCustomer',
  'plural_name': 'WashRiskCustomers'},
 {'plural_name_snake': 'wash_transactions',
  'singular_name': 'WashTransaction',
  'plural_name': 'WashTransactions'},
 {'plural_name_snake': 'washes_invoice_headers',
  'singular_name': 'WashesInvoiceHeader',
  'plural_name': 'WashesInvoiceHeaders'},
 {'plural_name_snake': 'wash_risk_customer_banks',
  'singular_name': 'WashRiskCustomerBank',
  'plural_name': 'WashRiskCustomerBanks'},
 {'plural_name_snake': 'washes_daily_sessions_details',
  'singular_name': 'WashesDailySessionsDetail',
  'plural_name': 'WashesDailySessionsDetails'},
 {'plural_name_snake': 'customer_wash_types',
  'singular_name': 'CustomerWashType',
  'plural_name': 'CustomerWashTypes'},
 {'plural_name_snake': 'wash_vehicles',
  'singular_name': 'WashVehicle',
  'plural_name': 'WashVehicles'},
 {'plural_name_snake': 'washes',
  'singular_name': 'Wash',
  'plural_name': 'Washes'},
 {'plural_name_snake': 'wash_vat_customers',
  'singular_name': 'WashVatCustomer',
  'plural_name': 'WashVatCustomers'},
 {'plural_name_snake': 'washes_invoice_subtotal_lines',
  'singular_name': 'WashesInvoiceSubtotalLine',
  'plural_name': 'WashesInvoiceSubtotalLines'},
 {'plural_name_snake': 'wash_types',
  'singular_name': 'WashType',
  'plural_name': 'WashTypes'},
 {'plural_name_snake': 'washes_daily_sessions',
  'singular_name': 'WashesDailySession',
  'plural_name': 'WashesDailySessions'},
 {'plural_name_snake': 'wash_fixed_extras',
  'singular_name': 'WashFixedExtra',
  'plural_name': 'WashFixedExtras'},
 {'plural_name_snake': 'washes_invoice_packages',
  'singular_name': 'WashesInvoicePackage',
  'plural_name': 'WashesInvoicePackages'},
 {'plural_name_snake': 'washes_invoice_lines',
  'singular_name': 'WashesInvoiceLine',
  'plural_name': 'WashesInvoiceLines'},
 {'plural_name_snake': 'wash_operators',
  'singular_name': 'WashOperator',
  'plural_name': 'WashOperators'},
 {'plural_name_snake': 'wash_extras',
  'singular_name': 'WashExtra',
  'plural_name': 'WashExtras'}]


    for item in extracted_models:

        singular_name = 'GM' + item['singular_name']
        plural_name = item['plural_name']
        plural_name_snake = item['plural_name_snake']

        print(plural_name_snake)

        ruta = '/Users/dorian/PhpstormProjects81/docker-laravel-84/projects/api.truckwashvilamalla.eu/'
        path_model = "Models/BatchProcesses/" + plural_name

        generate_model_file(ruta, path_model, singular_name, plural_name, plural_name_snake)

