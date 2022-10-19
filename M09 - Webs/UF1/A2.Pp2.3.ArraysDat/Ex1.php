<DOCTYPE html>
<html>
    <head>
        <meta charset=UTF-8>
        <link rel=stylesheet type=text/css href=CSS.css>
        <title>Exercici 1</title>
        <h1>Exercici 1</h1>
        <title>Exercisi 1</title>
    </head>
    <body>
        <?php
            $dataNaixement = mktime(0,0,0,12,12,1999);
            $dataActual = time();
            $diferencia = $dataActual - $dataNaixement;
            $hores = floor($diferencia / 3600);
            $minuts = floor(($diferencia - ($hores * 3600)) / 60);
            $segons = $diferencia - ($hores * 3600) - ($minuts * 60);
            echo "<br>Han passat <b>$hores</b> hores, <b>$minuts</b> minuts i <b>$segons</b> segons des del meu naixement";
        ?>
    </body>
</html>
