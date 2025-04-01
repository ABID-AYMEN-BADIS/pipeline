<?php
/**
 * Description du fichier : index.php
 * Il utilise la classe MesDates pour afficher la date de demain
 * php version  8.3.11
 * 
 * @category Dev
 * @package  Nom
 * @author   Aymen Badis <votre.email@mail.com>
 * @license  Licence 
 * @link     http://alloallo.com/
 */

namespace UPJV;
/**
 * Description du fichier : index.php
 * Il utilise la classe MesDates pour afficher la date de demain
 * php version  8.3.11
 * 
 * @category Dev
 * @package  Nom
 * @author   Aymen Badis <votre.email@mail.com>
 * @license  Licence 
 * @link     http://alloallo.com/
 */
class MesDates
{
    /**
     * Description du fichier : index.php
     * Il utilise la classe MesDates pour afficher la date de demain
     * php version  8.3.11
     * 
     * @category Dev
     * @package  Nom
     * @author   Aymen Badis <votre.email@mail.com>
     * @license  Licence 
     * @link     http://alloallo.com/
     * @return   string La date de demain au format JSON
     */
    public function demain()
    {

        $dateDemain = new \DateTime();
        $dateDemain->modify('+1 day');


        $formattedDate = $dateDemain->format('d-m-Y');

        @return
        return json_encode(['demain' => $formattedDate]);
    }
}
