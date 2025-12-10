import os
from helpers.helper_print import print_message, GREEN, CYAN, run_command


def generate_helpers(full_path):
    create_helper_date(full_path)
    create_helper_file(full_path)



def create_helper_date(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Utilities", "Helpers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "HelperDate.php")

    # Contenido por defecto
    content = """<?php

namespace App\\Utilities\\Helpers;

use DateTime;
use Exception;
use stdClass;

class HelperDate
{

    /**
     * Convert String to timestamp
     *
     * Ex. 20190429234640   ->   2019-04-29 23:46:40
     */
    public static function formatStringToTimestamp($strDate)
    {

        $year = substr($strDate, 0, 4);
        $month = substr($strDate, 4, 2);
        $day = substr($strDate, 6, 2);

        $hour = substr($strDate, 8, 2);
        $min = substr($strDate, 10, 2);
        $seg = substr($strDate, 12, 2);

        return $year . "-" . $month . "-" . $day. ' ' . $hour . ":" . $min . ":" . $seg;
    }



    /**
     * Convert String to timestamp
     *
     * Ex. 20190429   ->   2019-04-29
     */
    public static function formatStringToDate($strDate)
    {

        $year = substr($strDate, 0, 4);
        $month = substr($strDate, 4, 2);
        $day = substr($strDate, 6, 2);

        return $year . "-" . $month . "-" . $day;
    }



    /**
     * Convert and reverse date
     *
     * Ex. 2019-04-29   ->   29-04-2019
     *
     *
     * @param $str
     * @return string
     */
    public static function formatReverseDate($str)
    {

        $year = substr($str, 0, 4);
        $month = substr($str, 5, 2);
        $day = substr($str, 8, 2);

        return  $day . "-" . $month . "-" . $year;
    }



    /**
     * Convert date format for database Mysql
     *
     * Ex. 29-04-2019  ->  2019-04-29
     *
     *
     * @param $str
     * @return string
     */
    public static function formatDateForDB($str)
    {


        $day = substr($str, 0, 2);
        $month = substr($str, 3, 2);
        $year = substr($str, 6, 4);

        return $year. "-" . $month . "-" . $day;
    }


    /**
     * Convert date format for database Mysql
     *
     * Ex. 1/4/22  ->  2022-04-01
     *
     *
     * @param $str
     * @return string
     */
    public static function formatDateByDBShort($str)
    {
        $date = explode("/", $str);
        $day = str_pad($date[0], 2, '0', STR_PAD_LEFT);
        $month = str_pad($date[1], 2, '0', STR_PAD_LEFT);

        if(strlen($date[2]) == 4){
            $year = $date[2];
        }else{
            $year = '20' . $date[2];
        }


        return $year. "-" . $month . "-" . $day;
    }



    /**
     * Calculate days before of date
     * Ex. calculate 20 day's
     *      2019-04-10   ->   20-04-2019
     */
    public static function calculateDaysBeforeOrAfter($date, $days, $before = false)
    {
        if($before){
            return date('d-m-Y', strtotime('-'.$days.' day', strtotime($date)));
        }else{
            return date('d-m-Y', strtotime($days.' day', strtotime($date)));
        }

    }


    /**
     * Calculate days SENSE FORMAT before of date
     * Ex. calculate 20 day's
     *      2019-04-10   ->   2019-04-20
     */
    public static function calculateDaysBeforeOrAfterSenseFormat($date, $days, $before = false, $dateTime = false)
    {
        //Format date or datetimestamp
        if($dateTime){
            $format = 'Y-m-d H:i:s';
        }else{
            $format = 'Y-m-d';
        }

        if($before){
            return date($format, strtotime('-'.$days.' day', strtotime($date)));
        }else{
            return date($format, strtotime($days.' day', strtotime($date)));
        }

    }



    /**
     * @param $startDate
     * @param $days
     * @return string
     */
    public static function calculateDueDate($startDate, $days): string
    {
        try{
            $startDateTime = new DateTime($startDate);
            $endDateTime = clone $startDateTime;
            $endDateTime->modify("+$days days");
            return $endDateTime->format('Y-m-d H:i:s');

        }catch (Exception $e){
            return '';
        }
    }




    /**
     * Order Array years until today Ex. [2021,2020,2019...]
     * @param $start_year
     * @return array
     */
    public static function getYearsList($start_year): array
    {

        $start_year = intval($start_year);
        $yearNow = intval(date('Y'));
        $arr = [];

        for($i=$start_year; $i <= $yearNow; $i++){
            $arr[] = $i;
        }

        rsort($arr);

        return $arr;

    }



    /**
     * Return only the month.  Ex. 6  --> June
     * @return false|string
     */
    public static function getLastMonth()
    {
        $exd_new = strtotime ( '-1 month' , strtotime(date('Y-m-d')));
        return date ( 'n' , $exd_new );
    }




    /**
     * @param $thisMonth :int
     * @param $type // short or large
     * @return string
     */
    public static function monthName($thisMonth, $type) {
        $string = '';

        switch ($thisMonth) {
            case 1:     if($type == 'short') { $string = "Ene"; } elseif ($type == 'large') { $string = "Enero"; }      break;
            case '01':     if($type == 'short') { $string = "Ene"; } elseif ($type == 'large') { $string = "Enero"; }      break;
            case 2:     if($type == 'short') { $string = "Feb"; } elseif ($type == 'large') { $string = "Febrero"; }    break;
            case '02':     if($type == 'short') { $string = "Feb"; } elseif ($type == 'large') { $string = "Febrero"; }    break;
            case 3:     if($type == 'short') { $string = "Mar"; } elseif ($type == 'large') { $string = "Marzo"; }      break;
            case '03':     if($type == 'short') { $string = "Mar"; } elseif ($type == 'large') { $string = "Marzo"; }      break;
            case 4:     if($type == 'short') { $string = "Abr"; } elseif ($type == 'large') { $string = "Abril"; }      break;
            case '04':     if($type == 'short') { $string = "Abr"; } elseif ($type == 'large') { $string = "Abril"; }      break;
            case 5:     if($type == 'short') { $string = "May"; } elseif ($type == 'large') { $string = "Mayo"; }       break;
            case '05':     if($type == 'short') { $string = "May"; } elseif ($type == 'large') { $string = "Mayo"; }       break;
            case 6:     if($type == 'short') { $string = "Jun"; } elseif ($type == 'large') { $string = "Junio"; }      break;
            case '06':     if($type == 'short') { $string = "Jun"; } elseif ($type == 'large') { $string = "Junio"; }      break;
            case 7:     if($type == 'short') { $string = "Jul"; } elseif ($type == 'large') { $string = "Julio"; }      break;
            case '07':     if($type == 'short') { $string = "Jul"; } elseif ($type == 'large') { $string = "Julio"; }      break;
            case 8:     if($type == 'short') { $string = "Ago"; } elseif ($type == 'large') { $string = "Agosto"; }     break;
            case '08':     if($type == 'short') { $string = "Ago"; } elseif ($type == 'large') { $string = "Agosto"; }     break;
            case 9:     if($type == 'short') { $string = "Sep"; } elseif ($type == 'large') { $string = "Septiembre"; } break;
            case '09':     if($type == 'short') { $string = "Sep"; } elseif ($type == 'large') { $string = "Septiembre"; } break;
            case 10:    if($type == 'short') { $string = "Oct"; } elseif ($type == 'large') { $string = "Octubre"; }    break;
            case 11:    if($type == 'short') { $string = "Nov"; } elseif ($type == 'large') { $string = "Noviembre"; }  break;
            case 12:    if($type == 'short') { $string = "Dic"; } elseif ($type == 'large') { $string = "Diciembre"; }  break;
        }

//        switch ($thisMonth) {
//            case 1:     if($type == 'short') { $string = "Ene"; } elseif ($type == 'large') { $string = "Enero"; }      break;
//            case 2:     if($type == 'short') { $string = "Feb"; } elseif ($type == 'large') { $string = "Febrero"; }    break;
//            case 3:     if($type == 'short') { $string = "Mar"; } elseif ($type == 'large') { $string = "Marzo"; }      break;
//            case 4:     if($type == 'short') { $string = "Abr"; } elseif ($type == 'large') { $string = "Abril"; }      break;
//            case 5:     if($type == 'short') { $string = "May"; } elseif ($type == 'large') { $string = "Mayo"; }       break;
//            case 6:     if($type == 'short') { $string = "Jun"; } elseif ($type == 'large') { $string = "Junio"; }      break;
//            case 7:     if($type == 'short') { $string = "Jul"; } elseif ($type == 'large') { $string = "Julio"; }      break;
//            case 8:     if($type == 'short') { $string = "Ago"; } elseif ($type == 'large') { $string = "Agosto"; }     break;
//            case 9:     if($type == 'short') { $string = "Sep"; } elseif ($type == 'large') { $string = "Septiembre"; } break;
//            case 10:    if($type == 'short') { $string = "Oct"; } elseif ($type == 'large') { $string = "Octubre"; }    break;
//            case 11:    if($type == 'short') { $string = "Nov"; } elseif ($type == 'large') { $string = "Noviembre"; }  break;
//            case 12:    if($type == 'short') { $string = "Dic"; } elseif ($type == 'large') { $string = "Diciembre"; }  break;
//        }


        return $string;
    }


    public static function uniqueFormat()
    {
        $date = DateTime::createFromFormat('U.u', microtime(TRUE));
        //dd($date->format('Y-m-d H:i:s.u'));
        //$fileName = $date->format('YmdHisu');

        return $date->format('YmdHisu');
    }


    public static function getMonthlist()
    {

        $arr = [];

        $objE = new stdClass();
        $objE->number = '01';
        $objE->text = 'ENERO';
        $arr[] = $objE;

        $objF = new stdClass();
        $objF->number = '02';
        $objF->text = 'FEBRERO';
        $arr[] = $objF;

        $objM = new stdClass();
        $objM->number = '03';
        $objM->text = 'MARZO';
        $arr[] = $objM;


        $objA = new stdClass();
        $objA->number = '04';
        $objA->text = 'ABRIL';
        $arr[] = $objA;

        $objM = new stdClass();
        $objM->number = '05';
        $objM->text = 'MAYO';
        $arr[] = $objM;

        $objJ = new stdClass();
        $objJ->number = '06';
        $objJ->text = 'JUNIO';
        $arr[] = $objJ;

        $objL = new stdClass();
        $objL->number = '07';
        $objL->text = 'JULIO';
        $arr[] = $objL;

        $objAG = new stdClass();
        $objAG->number = '08';
        $objAG->text = 'AGOSTO';
        $arr[] = $objAG;


        $objS = new stdClass();
        $objS->number = '09';
        $objS->text = 'SEPTIEMBRE';
        $arr[] = $objS;


        $objO = new stdClass();
        $objO->number = '10';
        $objO->text = 'OCTUBRE';
        $arr[] = $objO;

        $objN = new stdClass();
        $objN->number = '11';
        $objN->text = 'NOVIEMBRE';
        $arr[] = $objN;


        $objD = new stdClass();
        $objD->number = '12';
        $objD->text = 'DICIEMBRE';
        $arr[] = $objD;


        return $arr;

    }


    /**
     * Ex. '2018-01-01', 3
     * return ['2018-01-01', '2018-02-02', '2018-03-03']
     *
     * Ex. '2018-01-01', 3, TRUE
     * return ['Enero', 'Febrero', 'Marzo']
     *
     * @param $date
     * @param $monthCount
     * @param bool $isNameMonth
     * @return array
     */
    public static function findArrMonths($date, $monthCount, $isNameMonth = false)
    {

        $arr = [];

        $aux = $date;
        $arr[] = $aux;

        for ($i = 0; $i < ($monthCount - 1); $i++) {

            $exd_new = date('Y-m-d', strtotime ( '+1 month' , strtotime($aux)));
            $arr[] = $exd_new;
            $aux = $exd_new;
        }


        if($isNameMonth) {

            $arrTmp = [];
            foreach ($arr as $item) {
                $m = substr($item, 5, 2);
                $arrTmp[] = self::monthName($m, 'large');
            }

            return $arrTmp;

        }else{
            return $arr;
        }


    }


    /**
     * Find Months
     *
     * Ex. $startDate = '2018-04-01' and $months = '3'
     * -> return ['01', '04', '07', '10']
     *
     * @param $month
     * @param $starDate
     * @return array
     */
    public static function findArrMonthsByStartDate($starDate, $month)
    {

        $arrDates = [];

        $finalDate = date("Y-m-d", strtotime($starDate."+ 1 year"));
        //dd($finalDate);

        $aux = date("Y-m-d", strtotime($starDate."+ ".$month." month"));
        $arrDates[] = $aux;

        while($aux < $finalDate){
            $newDate = date("Y-m-d", strtotime($aux."+ ".$month." month"));
            $arrDates[] = $newDate;
            $aux = $newDate;
        }

        $arrMonths = [];
        foreach ($arrDates as $date) {
            $arrMonths[] = substr($date, 5, 2);
        }
        asort($arrMonths);

        return $arrMonths;

    }


    /**
     * 2022-10-01 10:00:00 and 4
     *
     * return  2022-10-01 14:00:00
     */
    public static function findDateByHour($date, $hour): string
    {
        return date("Y-m-d H:i:s", strtotime($date."+ " . $hour . " hours"));
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



def create_helper_file(full_path):
    """
    Genera un archivo

    Args:
        full_path (str): Ruta completa del proyecto.
    """
    styles_path = os.path.join(full_path, "app", "Utilities", "Helpers")

    # Crear la carpeta si no existe
    if not os.path.exists(styles_path):
        os.makedirs(styles_path)
        print_message(f"Carpeta creada: {styles_path}", GREEN)

    # Ruta completa del archivo
    file_path = os.path.join(styles_path, "HelperFile.php")

    # Contenido por defecto
    content = r"""<?php

namespace App\Utilities\Helpers;
use Illuminate\Support\Facades\File;


/**********************************************
*
*  Method Generic to Write File
*
* ***********************
*/

class HelperFile
{

    /**
     * @param $path
     * @return false|resource|null
     */
    public function createFile($path)
    {

        try {

            return fopen(public_path($path), 'x+'); //create square_account handler

        } catch (\Exception $e) {
            echo $e->getMessage();
            return null;
        }
    }


    public function createFieldLine($str, $length)
    {

        if (strlen($str) <= $length) {

            $restNumber = $length - strlen($str);
            $filler = '';

            if ($restNumber > 0) {

                for ($i = 0; $i < $restNumber; $i++) {
                    $filler .= ' ';
                }

                return $str . $filler;

            }

            return $str;

        } else {
            return '@@@@@@@ EXCEDE EL LIMITE@@@@@@';
        }
    }


    public function createFiller($length)
    {
        $filler = '';
        for ($i = 0; $i < $length; $i++) {
            $filler .= ' ';
        }
        return $filler;
    }


    public function writeLine($handle, $line)
    {
        fwrite($handle, $line);
    }


    public function writeLineBreak($handle)
    {
//        fwrite($this->handle, "\r");
        fwrite($handle, chr(0x0D) . chr(0x0A));
    }


    //Idem to up Diference is Static
    public static function zFill($valor, $long = 0)
    {
        return str_pad($valor, $long, '0', STR_PAD_LEFT);
    }


    public function closeFile($handle)
    {
        try {

            fclose($handle);

        } catch (\Exception $e) {

            //$this->setClassErrorResponse($e);
        }
    }


    public function replaceSpecialChars($value)
    {
        $unwanted_array = array('Š' => 'S', 'š' => 's', 'Ž' => 'Z', 'ž' => 'z', 'À' => 'A', 'Á' => 'A', 'Â' => 'A', 'Ã' => 'A', 'Ä' => 'A', 'Å' => 'A', 'Æ' => 'A', 'Ç' => 'C', 'È' => 'E', 'É' => 'E',
            'Ê' => 'E', 'Ë' => 'E', 'Ì' => 'I', 'Í' => 'I', 'Î' => 'I', 'Ï' => 'I', 'Ñ' => 'N', 'Ò' => 'O', 'Ó' => 'O', 'Ô' => 'O', 'Õ' => 'O', 'Ö' => 'O', 'Ø' => 'O', 'Ù' => 'U',
            'Ú' => 'U', 'Û' => 'U', 'Ü' => 'U', 'Ý' => 'Y', 'Þ' => 'B', 'ß' => 'Ss', 'à' => 'a', 'á' => 'a', 'â' => 'a', 'ã' => 'a', 'ä' => 'a', 'å' => 'a', 'æ' => 'a', 'ç' => 'c',
            'è' => 'e', 'é' => 'e', 'ê' => 'e', 'ë' => 'e', 'ì' => 'i', 'í' => 'i', 'î' => 'i', 'ï' => 'i', 'ð' => 'o', 'ñ' => 'n', 'ò' => 'o', 'ó' => 'o', 'ô' => 'o', 'õ' => 'o',
            'ö' => 'o', 'ø' => 'o', 'ù' => 'u', 'ú' => 'u', 'û' => 'u', 'ý' => 'y', 'þ' => 'b', 'ÿ' => 'y');
        $str = strtr($value, $unwanted_array);
        return $str;
    }



    /**********************************************
     *
     * Method Generic to Read File
     *
     ************************/


    public static function listFilesIntoDir($pathDir)
    {
        $arrayFiles = array();

        $directorio = opendir($pathDir); //ruta actual
        while ($file = readdir($directorio)) //obtenemos un archivo y luego otro sucesivamente
        {
            //if (!is_dir($square_account) && $square_account != '.DS_Store' && $square_account != '..') {
            if (!is_dir($file) && $file != '.DS_Store') {
                $arrayFiles[] = $file;
                //echo "[" . $square_account . "]<br />"; //de ser un directorio lo envolvemos entre corchetes
            } /*else {
                echo $square_account . "<br />";
            }*/
        }

        //Order Array
        asort($arrayFiles);

        return $arrayFiles;
    }


    /**
     * Open File only MODE READ
     * Ex. $pathFile = files/mile/mile.csv
     *
     * @param $pathFile
     * @return bool|resource|null
     */

    public function openFileToRead($pathFile)
    {

        try {

            //return fopen(public_path($pathFile), 'r'); //create square_account handler
            return fopen($pathFile, 'r'); //create square_account handler

        } catch (\Exception $e) {
            //echo $e->getMessage();
            return null;
            //$this->setClassErrorResponse($e);
        }

    }


    public function checkLengthLine($handle, $totalLine)
    {

        $line = 1;

        while (!feof($handle)) {
            $strLine = fgets($handle);

            echo $strLine . "<br>";

            $length = strlen($strLine);

            if ($length != $totalLine) {
                return "Error Line: " . $line . ' Cantidad: ' . $length;
            }

            $line++;

        }

        return null;

    }


    public static function formatSizeUnits($bytes)
    {
        if ($bytes >= 1073741824) {
            $bytes = number_format($bytes / 1073741824, 2) . ' GB';
        } elseif ($bytes >= 1048576) {
            $bytes = number_format($bytes / 1048576, 2) . ' MB';
        } elseif ($bytes >= 1024) {
            $bytes = number_format($bytes / 1024, 2) . ' KB';
        } elseif ($bytes > 1) {
            $bytes = $bytes . ' bytes';
        } elseif ($bytes == 1) {
            $bytes = $bytes . ' byte';
        } else {
            $bytes = '0 bytes';
        }

        return $bytes;
    }


    /**
     * @param $type
     * @return string
     */
    public static function checkApplicationType($type): string
    {

        if(strtolower($type) == 'pdf'){
            return 'data:application/' . $type;
        }

        if(strtolower($type) == 'png' ||
            strtolower($type) == 'jpg' ||
            strtolower($type) == 'jpeg'
        ){
            return 'data:image/' . $type;
        }


        if(strtolower($type) == 'xlxs' ||
            strtolower($type) == 'xlx'
        ){
            return 'data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet/' . $type;
        }

        return '';

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

