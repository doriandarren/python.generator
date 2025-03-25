import os
from helpers.helper_print import print_message, GREEN, CYAN


def generate_company_logos(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "public", "brand", "images", "company_logos")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "logo.svg")

    # Contenido por defecto
    content = """<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 26.5.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 1024 300.8388" style="enable-background:new 0 0 1024 300.8388;" xml:space="preserve">
<style type="text/css">
	.st0{fill:#333333;}
	.st1{fill:#19DCF7;}
	.st2{fill:#00C7F7;}
	.st3{fill:#28BEF7;}
	.st4{fill:#4AE6F7;}
	.st5{fill:#00D3F7;}
	.st6{fill:#0096E8;}
</style>
<g>
	<path class="st0" d="M374.7561,274.9509c-6.2169,0-11.7849,4.9175-11.7849,13.037c0,7.748,4.7787,12.8509,12.1555,12.8509
		c3.2484,0,6.1711-0.9738,8.7226-2.9693v-3.5259c-2.691,2.4592-5.7068,3.5259-8.583,3.5259c-5.0571,0-8.6295-3.3864-9.1397-8.8148
		h18.9755c0.0465-0.5101,0.093-1.0203,0.093-1.67C385.1952,279.2188,380.5087,274.9509,374.7561,274.9509z M366.1731,286.3172
		c0.5566-5.2424,4.3144-8.4435,8.5365-8.4435c3.7112,0,7.2837,2.5979,7.4232,8.4435H366.1731z M421.6556,280.0538
		c-1.8095-3.3399-5.4284-5.1028-8.9544-5.1028c-5.8921,0-11.367,4.9641-11.367,12.9439c0,7.9333,5.4749,12.9439,11.367,12.9439
		c3.5259,0,7.1449-1.7165,9.1397-5.3819l0.4179,4.8718h2.5514v-37.0231h-3.1546V280.0538z M413.1191,297.823
		c-4.8253,0-8.6295-3.9896-8.6295-9.9281c0-5.9851,3.8043-9.9289,8.6295-9.9289c4.7787,0,8.6295,4.0368,8.6295,9.8824
		C421.7486,293.7869,417.8978,297.823,413.1191,297.823z M59.6273,179.1992c-5.2454-8.5575-14.9072-14.079-25.5353-14.079
		C16.4249,165.1202,0,180.7176,0,202.9393c0,22.6365,16.1488,37.8191,33.816,37.8191c10.6281,0,19.7377-5.3834,24.8451-13.5261
		v9.6611c0,12.8367-10.49,21.3942-23.8788,21.3942c-9.5238,0-19.4609-4.1411-27.191-10.9041v16.4249
		c7.8681,5.6595,18.0813,9.1097,28.2953,9.1097c21.5322,0,39.0614-13.3881,39.0614-38.2332v-67.9081H61.4211L59.6273,179.1992z
		 M37.681,226.1279c-12.1465,0-21.3942-9.9379-21.3942-23.0506c0-13.112,9.2477-23.1879,21.3942-23.1879
		s21.3942,9.6618,21.3942,22.7738C59.0752,216.052,49.8275,226.1279,37.681,226.1279z M154.8592,164.9822
		c-21.6703,0-38.3712,16.5629-38.3712,39.4755s16.5629,39.4755,38.3712,39.4755c21.8076,0,38.2332-16.5629,38.2332-39.4755
		S176.6667,164.9822,154.8592,164.9822z M154.8592,229.026c-11.1802,0-21.9463-8.9716-21.9463-24.5683
		s10.7661-24.5683,21.9463-24.5683s21.8076,8.9716,21.8076,24.5683S166.0394,229.026,154.8592,229.026z M479.484,131.5803h-16.2868
		v110.5584h16.2868V131.5803z M346.4346,179.7514c-5.3834-9.2477-15.0453-14.7692-26.0874-14.7692
		c-17.2531,0-33.816,15.5974-33.816,39.6135c0,23.7401,16.5629,39.3374,33.816,39.3374c11.0422,0,20.704-5.5215,26.0874-14.7692
		l1.7937,12.9747h13.5268v-75.362h-13.5268L346.4346,179.7514z M324.4883,229.026c-12.2845,0-21.6703-10.0759-21.6703-24.5683
		c0-14.3543,9.3857-24.5683,21.6703-24.5683c12.0085,0,21.3942,10.214,21.3942,24.5683
		C345.8824,218.95,336.4967,229.026,324.4883,229.026z M88.7478,242.1387h16.2868V131.5803H88.7478V242.1387z M325.1649,291.8379
		v-13.5471h7.2844v-2.8297h-7.2844v-5.8456h-3.0616v5.8456h-3.8508v2.8297h3.7578v13.6866c0,5.6137,3.4794,8.583,8.3977,8.583
		c1.2986,0,2.3661-0.1853,2.6445-0.2318v-2.8298c-0.7892,0.1388-1.5312,0.2318-2.2274,0.2318
		C327.5311,297.7307,325.1649,296.0135,325.1649,291.8379z M245.9529,164.9822c-10.214,0-20.4279,5.2454-25.3965,14.217v-47.6189
		h-16.2868v110.5584h13.5261l1.7945-12.9747c5.3827,9.2477,15.0445,14.7692,25.8106,14.7692
		c17.6672,0,34.2301-15.3213,34.2301-39.4755S263.6201,164.9822,245.9529,164.9822z M241.6745,229.026
		c-12.1465,0-21.3942-10.0759-21.3942-24.5683c0-14.3543,9.2477-24.5683,21.2561-24.5683c12.2838,0,21.6695,10.214,21.6695,24.7063
		C263.206,218.95,253.8202,229.026,241.6745,229.026z M434.2717,279.4971h-0.0465l-0.3706-4.0361h-2.5057v24.8676h3.1546v-14.893
		c0-4.9641,3.5259-7.2379,6.9596-7.2379c0.5566,0,1.1133,0.0465,1.6234,0.1395v-3.0623c-0.4636-0.0465-0.9738-0.0923-1.5769-0.0923
		C439.2823,275.1827,435.9882,276.203,434.2717,279.4971z M348.3604,274.9509c-3.1088,0-5.8463,1.4374-7.2844,3.7112h-0.0465
		v-15.3566h-3.1546v37.0231h3.1546v-15.6349c0-4.64,3.2941-6.7278,6.9131-6.7278c4.2686,0,6.3564,2.3661,6.3564,7.1914v15.1713
		h3.1546V283.951C357.4535,278.0125,353.8811,274.9509,348.3604,274.9509z M375.9692,242.1387h16.2868V131.5803h-16.2868V242.1387z
		 M567.1279,271.2389v4.2221h-3.619v2.8297h3.6655v22.0379h3.1553v-22.0379h7.3774v-2.8297h-7.424v-3.6655
		c0-3.8973,1.8094-5.6137,5.0578-5.6137c1.2048,0,2.8298,0.3249,3.7105,0.6962v-3.1088c-1.1598-0.4179-2.5972-0.6954-3.8965-0.6954
		C570.5623,263.0738,567.1279,266.2749,567.1279,271.2389z M632.5482,221.4347c-7.5905,5.9356-16.0107,8.9716-24.5675,8.9716
		c-13.2515,0-23.3267-7.7293-25.6733-20.9793h54.2439c0.2761-1.9325,0.4141-4.0031,0.4141-6.3497
		c0-24.9824-15.0445-38.0951-33.2639-38.0951c-20.1519,0-36.9908,15.5974-36.9908,39.7516
		c0,23.1879,14.9064,39.1994,39.6135,39.1994c9.6611,0,18.4954-2.6227,26.2239-7.8681V221.4347z M603.5635,178.509
		c9.385,0,17.5292,6.625,17.9432,20.0138h-39.1994C584.2399,186.1003,593.3488,178.509,603.5635,178.509z M607.256,300.3287h3.1539
		v-37.0231h-3.1539V300.3287z M591.0667,274.9509c-6.2162,0-11.7841,4.9175-11.7841,13.037c0,7.748,4.7787,12.8509,12.1547,12.8509
		c3.2484,0,6.1711-0.9738,8.7233-2.9693v-3.5259c-2.6917,2.4592-5.7075,3.5259-8.5838,3.5259c-5.0563,0-8.6288-3.3864-9.1389-8.8148
		h18.9755c0.0465-0.5101,0.093-1.0203,0.093-1.67C601.5065,279.2188,596.8192,274.9509,591.0667,274.9509z M582.4844,286.3172
		c0.5566-5.2424,4.3137-8.4435,8.5358-8.4435c3.712,0,7.2844,2.5979,7.424,8.4435H582.4844z M618.0634,300.3287h3.1553v-37.0231
		h-3.1553V300.3287z M682.2354,229.164c-9.1104,0-15.7347-4.4164-15.7347-15.1825v-33.4019h20.8406v-13.8029h-20.8406v-17.5292
		h-15.7361v17.5292h-11.3175v13.8029h11.0414v34.2301c0,17.9433,10.6288,28.5714,28.434,28.5714
		c4.5552,0,8.0046-0.5522,10.0752-0.9663v-13.9409C686.5131,228.8879,684.306,229.164,682.2354,229.164z M680.0433,296.6167h-0.093
		l-6.9589-21.1556h-3.4344l-6.9124,21.1556h-0.093l-5.799-21.1556h-3.2484l7.1915,24.8676h3.5724l6.9138-20.692h0.1381
		l6.9603,20.692h3.5724l7.1449-24.8676h-3.1088L680.0433,296.6167z M638.8004,274.9509c-7.0054,0-12.1547,5.5672-12.1547,12.9439
		c0,7.4232,5.1494,12.9439,12.1547,12.9439c6.9588,0,12.1097-5.5672,12.1097-12.9439S645.7592,274.9509,638.8004,274.9509z
		 M638.8004,297.823c-4.5927,0-9.0009-3.5724-9.0009-9.9281c0-6.3099,4.3616-9.9289,9.0009-9.9289
		c4.5927,0,8.9543,3.619,8.9543,9.9289C647.7548,294.204,643.3931,297.823,638.8004,297.823z M412.957,156.8395v9.9371h-10.6281
		v13.8029h10.6281v61.5591h16.2868v-61.5591h20.842v-13.8029h-20.9801v-8.1434c0-9.2477,4.6932-13.3881,13.5268-13.3881
		c3.8643,0,8.1434,0.9655,10.9041,1.9318v-14.3543c-4.2791-1.3804-8.6956-2.2082-13.3888-2.2082
		C423.309,130.6144,412.957,142.3464,412.957,156.8395z M491.0993,274.9509c-6.2169,0-11.7849,4.9175-11.7849,13.037
		c0,7.748,4.7788,12.8509,12.1555,12.8509c3.2484,0,6.1711-0.9738,8.7226-2.9693v-3.5259c-2.691,2.4592-5.7068,3.5259-8.583,3.5259
		c-5.0571,0-8.6295-3.3864-9.1397-8.8148h18.9756c0.0465-0.5101,0.093-1.0203,0.093-1.67
		C501.5383,279.2188,496.8518,274.9509,491.0993,274.9509z M482.5163,286.3172c0.5566-5.2424,4.3144-8.4435,8.5365-8.4435
		c3.7112,0,7.2837,2.5979,7.4232,8.4435H482.5163z M526.6858,164.9822c-20.1519,0-36.9909,15.5974-36.9909,39.7516
		c0,23.1879,14.9072,39.1994,39.6136,39.1994c9.6618,0,18.4954-2.6227,26.2247-7.8681v-14.6304
		c-7.5913,5.9356-16.0108,8.9716-24.5683,8.9716c-13.2508,0-23.3267-7.7293-25.6726-20.9793h54.2436
		c0.2761-1.9325,0.4141-4.0031,0.4141-6.3497C559.95,178.0949,544.9051,164.9822,526.6858,164.9822z M505.2923,198.5228
		c1.9318-12.4225,11.0414-20.0138,21.2554-20.0138c9.3857,0,17.5292,6.625,17.9432,20.0138H505.2923z M447.7243,300.3287h3.1546
		v-24.8676h-3.1546V300.3287z M449.3012,264.6972c-1.2521,0-2.1335,0.8815-2.1335,2.0878c0,1.2528,0.8815,2.1343,2.1335,2.1343
		c1.2993,0,2.1808-0.8815,2.1808-2.1343C451.482,265.5787,450.6005,264.6972,449.3012,264.6972z M466.5123,296.6632h-0.1395
		l-7.4232-21.2021h-3.3406l9.0474,24.8676h3.4794l9.0474-24.8676h-3.2941L466.5123,296.6632z M510.1176,279.4971h-0.0465
		l-0.3714-4.0361h-2.5049v24.8676h3.1546v-14.893c0-4.9641,3.5259-7.2379,6.9596-7.2379c0.5566,0,1.1133,0.0465,1.6234,0.1395
		v-3.0623c-0.4636-0.0465-0.9738-0.0923-1.5769-0.0923C515.1282,275.1827,511.8341,276.203,510.1176,279.4971z M540.2711,286.3172
		c-3.5724-1.1133-5.9386-1.9483-5.9386-4.547c0-2.2731,1.9483-3.85,5.3812-3.85c2.9692,0,5.6145,1.1133,7.3774,2.6902v-3.4794
		c-1.7172-1.3451-4.5469-2.1801-7.3309-2.1801c-5.2424,0-8.5831,2.9693-8.5831,7.0518c0,4.3144,3.619,5.5207,7.7946,6.8201
		c3.7112,1.1598,6.2634,2.0413,6.2634,4.8245c0,2.4592-2.1343,4.2221-5.7997,4.2221c-3.5724,0-6.5417-1.67-8.4435-3.7112v3.7578
		c2.3661,1.9955,5.4285,2.9228,8.4901,2.9228c5.4284,0,8.8613-2.8298,8.8613-7.2372
		C548.3433,288.6375,543.9824,287.477,540.2711,286.3172z M523.7555,277.6877h2.1801l0.5101-11.8307h-3.3864L523.7555,277.6877z"/>
	<g>
		<g>
			<polygon class="st1" points="1003.9441,0 963.8322,10.0279 983.8881,50.1398 			"/>
		</g>
		<g>
			<polygon class="st2" points="753.0228,130.0986 763.2729,170.4753 793.3569,150.4194 			"/>
		</g>
		<g>
			<polygon class="st3" points="833.4687,30.0838 843.4967,60.1677 903.6645,90.2516 883.6085,30.0838 			"/>
		</g>
		<g>
			<polygon class="st4" points="763.2729,170.4753 723.1611,300.8387 793.3569,150.4194 			"/>
		</g>
		<g>
			<polygon class="st2" points="793.3569,150.4194 723.1611,300.8387 733.1891,300.8387 833.4687,220.6151 903.6645,120.3355 			"/>
		</g>
		<g>
			<polygon class="st5" points="833.4687,220.6151 923.7204,220.6151 903.6645,120.3355 			"/>
		</g>
		<g>
			<polygon class="st4" points="983.8881,50.1398 923.7204,220.6151 953.8042,300.8387 963.8322,300.8387 1013.972,170.4753 			"/>
		</g>
		<g>
			<polygon class="st1" points="903.6645,120.3355 923.7204,220.6151 983.8881,50.1398 			"/>
		</g>
		<g>
			<polygon class="st6" points="903.6645,90.2516 903.6645,120.3355 983.8881,50.1398 			"/>
		</g>
		<g>
			<path class="st5" d="M963.8322,10.0279h-60.1677l-20.056,20.0559l20.056,60.1678l80.2236-40.1118L963.8322,10.0279z
				 M913.6924,40.1118c-5.5383,0-10.0279-4.4897-10.0279-10.028s4.4896-10.0279,10.0279-10.0279
				c5.5383,0,10.028,4.4896,10.028,10.0279S919.2307,40.1118,913.6924,40.1118z"/>
		</g>
		<g>
			<polygon class="st6" points="795.4675,270.7549 823.4407,300.8387 833.4687,300.8387 830.3345,240.671 			"/>
		</g>
		<g>
			<polygon class="st6" points="1016.0785,205.6669 993.9161,270.7548 1013.972,300.8387 1024,300.8388 			"/>
		</g>
	</g>
</g>
</svg>
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
