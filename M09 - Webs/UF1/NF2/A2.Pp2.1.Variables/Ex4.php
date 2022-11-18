<DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 4</title>
        <h1>Exercici 4</h1>
    </head>
    <body>
        <?php
        echo "On es troba l'arrel de documents web del servidor: ".$_SERVER['DOCUMENT_ROOT']."<br>";
        echo "Quina versió d'Apache està funcionant: ".$_SERVER['SERVER_SOFTWARE']."<br>";
        echo "Quin tipus de navegador està visualitzant la plana web: ".$_SERVER['HTTP_USER_AGENT']."<br>";
        echo "Des de quina adreça IP s'estan connectant: ".$_SERVER['REMOTE_ADDR']."<br>";
        echo "Timestamp (Request time): quan s'ha connectat el client per demanar la plana? ".$_SERVER['REQUEST_TIME']."<br>";
        echo "Si actualitzes la plana, canvia algun valor? Per què creus que passa? <br> Si, canvia el timestamp(SERVER['REQUEST_TIME']) ja que cada cop q es recarrega estem a un temps diferent<br>";
        ?>
    </body>