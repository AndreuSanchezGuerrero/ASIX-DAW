<DOcTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 3</title>
        <h1>Exercici 3</h1>
    </head>
    <body>
        <?php
        $a=31;
        $b=15;
        $c=15;
        echo "La suma de $a , $b i $c és ".($a+$b+$c).".<br>";
        echo "El valor més petit és ".min($a,$b,$c).".<br>";
        echo "El valor més gran és ".max($a,$b,$c).".<br>";
        echo "La mitjana entre els tres és ".(($a+$b+$c)/3).".<br>";
        ?>
    </body>