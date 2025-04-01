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

require_once "./src/MesDates.php";

$objDate = new \UPJV\MesDates();

echo $objDate->demain();
