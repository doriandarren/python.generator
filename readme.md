## Project Generators


```sh
cd generators
python3 main.py
```


### Install

```sh

// Entorno virtual (https://flask.palletsprojects.com/en/3.0.x/installation/)
- python3 -m venv venv                      // MacOs
- source venv/bin/activate                  // MacOs
- pip install --upgrade pip

- python3.exe -m venv venv                  // Windows
- .\venv\bin\activate                       // Windows
- python3.exe -m pip install --upgrade pip  // Windows
- deactivate                                // Deactivate

// Instala los requirimientos:
pip freeze > requirements.txt     // Crear archivo requerimientos
pip install -r requirements.txt   // Instalar requerimientos 

```


### Instalar librerias

```sh

pip install mysql-connector-python 
pip install inflect

pip install aiohttp

pip install colorama


pip uninstall mysql-connector-python    ## Desinstalar cualquier error reintalar

```




### Ejecucion del programa

databases: proyecto que ejecuta desde una base datos se conecta y genera las tablas. Se ejecuata PHP - OK


helpers: carpeta de 





### Ollama

```sh

OLLAMA_HOST=192.168.1.100:11434 ollama serve

ollama serve
ollama run llama2

pip install aiohttp

```





[instantic_special_prices] InstanticSpecialPrice *** InstanticSpecialPrices : station_id product_type customer_code discount_type price currency valid_from sent
[user_customizations] UserCustomization *** UserCustomizations : user_id drivers_self_management max_diesel_liters_per_trx max_red_liters_per_trx max_adblue_liters_per_trx max_gas_kilos_per_trx prepaid_type random_auth_code type_auth_management two_factor_authentication reports_by_product own_customers own_customer_balance liquidation own_customers_commission gp_partner gp_customer_child own_customer_id autoactivate_qrcard rappel_info toll_own_customer toll_own_customer_commission
[users_api] UsersApi *** UsersApis : name email api_token remember_token
[roles] Role *** Roles : name slug
[toll_obu_plate_changes] TollObuPlateChange *** TollObuPlateChanges : gt_obu_id provider_id customer_code company_name obu_number plate_number vehicle_country vehicle_identification_number vehicle_tractor_axles vehicle_euro_pollution plate_number_old status error_code error_code_description gt_transaction_origin
[toll_obu_request_rejections] TollObuRequestRejection *** TollObuRequestRejections : toll_obu_request_id toll_obu_request_reason_id observations
[groups] Group *** Groups : name
[migrations] Migration *** Migrations : migration batch
[washes_invoice_subtotals] WashesInvoiceSubtotal *** WashesInvoiceSubtotals : header_id units amount vat_quote total_amount payment_type
[failed_jobs] FailedJob *** FailedJobs : connection queue payload exception failed_at
[reminders] Reminder *** Reminders : user_id code completed completed_at
[washes_payment_modes] WashesPaymentMode *** WashesPaymentModes : name
[customers] Customer *** Customers : group_id customer_code accounting_code name nif address zip_code country city state province extension phone email commission
[customer_risks] CustomerRisk *** CustomerRisks : customer_id in out balance
[activations] Activation *** Activations : user_id code completed completed_at
[customer_wash_types] CustomerWashType *** CustomerWashTypes : wash_id customer_code price
[wash_customer_plates_authorizations] WashCustomerPlatesAuthorization *** WashCustomerPlatesAuthorizations : customer_code status
[wash_customer_codes] WashCustomerCode *** WashCustomerCodes : customer_code status
[sms_receiveds] SmsReceived *** SmsReceiveds : sms_to sms_from sms_text sms_date username smsc
[wash_risk_customers] WashRiskCustomer *** WashRiskCustomers : country_id code_alpha_2 customer_code company_name phone address code_zip country_name population province fiscal_identification email type
[persistences] Persistence *** Persistences : user_id code
[toll_obu_request_reasons] TollObuRequestReason *** TollObuRequestReasons : name
[toll_obu_requests] TollObuRequest *** TollObuRequests : customer_code company_name provider_id plate_number vehicle_country vehicle_identification_number vehicle_tractor_axles vehicle_euro_pollution service_countries status
[wash_transactions] WashTransaction *** WashTransactions : wash_id type concept_id extra_weight
[washes_invoice_headers] WashesInvoiceHeader *** WashesInvoiceHeaders : wash_id invoice_string serie invoice_nb year invoice_date due_date payment_mode remittance_type remittance_type_id customer_code company_name address city zipcode cif state vat_base vat_type vat_quote total invoice_sent paid sage_file origin
[throttle] Throttle *** Throttles : user_id type ip
[toll_obu_returns] TollObuReturn *** TollObuReturns : gt_obu_id provider_id reason_id obu_number customer_code company_name status error_code error_code_description
[driver_limit_products] DriverLimitProduct *** DriverLimitProducts : driver_id product_id
[toll_obu_plate_change_files] TollObuPlateChangeFile *** TollObuPlateChangeFiles : toll_obu_plate_change_id document_type_id file
[wash_risk_customer_banks] WashRiskCustomerBank *** WashRiskCustomerBanks : customer_id bank_id iban bank_name account_number swift_bic account_holder pay_day remitance_type remittance_type_id due_date risk_req quantity mandate_reference status globaldocs_document_id
[wash_vehicles] WashVehicle *** WashVehicles : company_name customer_code plate
[invoice_counters] InvoiceCounter *** InvoiceCounters : year serial counter
[washes] Wash *** Washes : wash_counter trx_date customer_code company_name plate trailer_plate driver driver_doc wash_type_id init_time finish_time price special_price courtesy operator_id extras comments payment_method invoiced invoice_package_id in_job status
[washes_daily_sessions_details] WashesDailySessionsDetail *** WashesDailySessionsDetails : wash_session_id amount type count
[toll_obu_return_reasons] TollObuReturnReason *** TollObuReturnReasons : name
[role_users] RoleUser *** RoleUsers : role_id user_id
[wash_vat_customers] WashVatCustomer *** WashVatCustomers : customer_code exempt
[user_logs] UserLog *** UserLogs : user_id group_id transaction_id transaction_date plate diesel_liters adblue_liters red_liters gas_kilos type_action
[washes_invoice_subtotal_lines] WashesInvoiceSubtotalLine *** WashesInvoiceSubtotalLines : subtotal_id wash_type units amount vat_quote total_amount
[wash_fixed_extras] WashFixedExtra *** WashFixedExtras : name price
[wash_types] WashType *** WashTypes : name duration price
[washes_daily_sessions] WashesDailySession *** WashesDailySessions : opened_at closed_at
[washes_invoice_packages] WashesInvoicePackage *** WashesInvoicePackages : washes_str header_id
[vehicles] Vehicle *** Vehicles : group_id phone extension extension_country plate customer_id
[washes_invoice_lines] WashesInvoiceLine *** WashesInvoiceLines : header_id transaction_id type amount amount_with_vat
[toll_obu_request_files] TollObuRequestFile *** TollObuRequestFiles : toll_obu_request_id document_type_id file
[wash_operators] WashOperator *** WashOperators : name
[password_resets] PasswordReset *** PasswordResets : email token
[vehicles_old] VehiclesOld *** VehiclesOlds : group_id phone extension extension_country plate customer_id
[drivers] Driver *** Drivers : group_id name phone extension extension_country dni plate client_code locked self_management periodicity_limit product_limit
[favorite_customers] FavoriteCustomer *** FavoriteCustomers : user_id customer_code
[wash_extras] WashExtra *** WashExtras : name duration price
[users] User *** Users : app_customer_id name email password remember_token token secret_word customer_code session_id last_login group_id agent_id prepaid status
[jobs] Job *** Jobs : queue payload attempts reserved_at available_at



