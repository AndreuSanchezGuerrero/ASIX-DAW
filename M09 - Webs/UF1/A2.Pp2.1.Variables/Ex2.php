<DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 2</title>
        <h1>Exercici 2</h1>
    </head>
    <body>
        <?php
        $a=31;
        $b=15;
        echo "La suma entre $a i $b és ".($a+$b).".<br>";
        echo "La resta entre $a i $b és ".($a-$b).".<br>";
        echo "El producte entre $a i $b és ".($a*$b).".<br>";
        echo "La divisió entre $a i $b és ".($a/$b).".<br>";
        echo "El mòdul entre $a i $b és ".($a%$b).".<br>";
        echo "El valor més alt dels mostrats és ".max($a+$b,$a-$b,$a*$b,$a/$b,$a%$b).".<br>";
        ?>
    </body>
