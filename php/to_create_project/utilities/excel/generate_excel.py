import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command



def generate_excel(full_path):
    create_example_export(full_path)
    create_example_export_per_sheet(full_path)


def create_example_export(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Utilities", "Exls", "Exports", "Example")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "ExampleExport.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Utilities\\Exls\\Exports\\Example;

use Maatwebsite\\Excel\\Concerns\\Exportable;
use Maatwebsite\\Excel\\Concerns\\WithMultipleSheets;


class ExampleExport implements WithMultipleSheets
{

    use Exportable;

    protected $data;


    /**
     * Constructor.
     * @param $data
     */
    public function __construct($data)
    {
        $this->data = $data;
    }



    public function sheets(): array
    {
        //Create Sheet
        $sheets = [];

        /**
         * Resume First page
         */
        $dataSheet = [];


        //Create Title
        $dataSheet[] = [
            "Fecha de Factura",
            "Num de Factura",
            "codigo Targeta",
            "Tarjeta",
            "Matricula",
        ];


        // Create Data
        foreach ($this->data as $item){

            $dataSheet[] = [
                $item->invoice_date,
                $item->invoice_number,
                $item->card_code,
                $item->card,
                $item->plate,
            ];

        }

        $sheets[] = new ExampleExportPerSheet($dataSheet, 'Resumen');

        return $sheets;

    }

}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)


def create_example_export_per_sheet(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Utilities", "Exls", "Exports", "Example")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "ExampleExportPerSheet.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Utilities\\Exls\\Exports\\Example;

use Maatwebsite\\Excel\\Concerns\\FromArray;
use Maatwebsite\\Excel\\Concerns\\ShouldAutoSize;
use Maatwebsite\\Excel\\Concerns\\WithEvents;
use Maatwebsite\\Excel\\Concerns\\WithTitle;
use Maatwebsite\\Excel\\Events\\AfterSheet;

class ExampleExportPerSheet implements WithTitle, FromArray, ShouldAutoSize, WithEvents
{

    protected $data;
    protected $sheetTitle;
    protected $sheetColumns;


    /**
     * VisaExportPerSheet constructor.
     * @param $data
     * @param $sheetTitle
     */
    public function __construct($data, $sheetTitle)
    {
        $this->data = $data;
        $this->sheetTitle = $sheetTitle;
        $this->sheetColumns = count($data[0]);
    }


    public function title(): string
    {
        return $this->sheetTitle;
    }



    public function array(): array
    {

//        return [
//            [1, 2, 3],
//            [4, 5, 6]
//        ];
        return $this->data;
    }


    public function registerEvents(): array
    {
        return [
            AfterSheet::class    => function(AfterSheet $event) {
                //Color
                $event->sheet->getDelegate()->getStyle('A1:' . $this->numberToExcelColumn($this->sheetColumns) . '1')->getFill()
                    ->setFillType(\\PhpOffice\\PhpSpreadsheet\\Style\\Fill::FILL_SOLID)
                    ->getStartColor()
                    ->setRGB('D0D0D0');
                //->setARGB('FFFF0000');


                //Align
                $event->sheet->getDelegate()->getStyle('A1:' . $this->numberToExcelColumn($this->sheetColumns) . '1')
                    ->applyFromArray(
                        array(
                            'font' => array(
                                'name' => 'Calibri',
                                'size' => 14,
                                //'color' => array('rgb' => 'FF0000'), //Color letra
                            ),
                            'borders' => [
                                //'outline' => [
                                'allBorders' => [
                                    //'borderStyle' => \\PhpOffice\\PhpSpreadsheet\\Style\\Border::BORDER_THICK,
                                    'borderStyle' => \\PhpOffice\\PhpSpreadsheet\\Style\\Border::BORDER_THIN,
                                    'color' => ['rgb' => '000000'],
                                    //'color' => ['argb' => 'FFFF0000'],
                                ],
                            ],
                        )
                    )
                    ->getAlignment()->applyFromArray(
                        array(
                            'horizontal' => 'center',
                        )
                    );


                $event->sheet->getDelegate()->getRowDimension(1)->setRowHeight(35);


                //OK
//                $event->sheet->getDelegate()->getStyle('A1:W1')->applyFromArray(
//                    array(
//                        'font' => array(
//                            'name' => 'Calibri',
//                            'size' => 18,
//                            'color' => array('rgb' => 'FF0000'), //Color letra
//                        ),
//                    )
//                );


//                $styleArray = [
//                    'borders' => [
//                        'outline' => [
//                            'borderStyle' => \\PhpOffice\\PhpSpreadsheet\\Style\\Border::BORDER_THICK,
//                            'color' => ['argb' => 'FFFF0000'],
//                        ],
//                    ],
//                ];
//                $event->sheet->getDelegate()->getStyle('B2:G8')->applyFromArray($styleArray);


//                $cellRange = 'A1:W1'; // All headers
//                $event->sheet->getDelegate()->getStyle($cellRange)->getFont()->setSize(14);

            },
        ];

    }



    /**
     * @param $number
     * @return string
     */
    private function numberToExcelColumn($number): string
    {
        $dividend = $number;
        $columnName = '';
        while ($dividend > 0) {
            $modulo = ($dividend - 1) % 26;
            $columnName = chr(65 + $modulo) . $columnName;
            $dividend = intdiv($dividend - 1, 26);
        }
        return $columnName;
    }
}
"""

    try:
        # Crear o sobrescribir el archivo con el contenido
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
