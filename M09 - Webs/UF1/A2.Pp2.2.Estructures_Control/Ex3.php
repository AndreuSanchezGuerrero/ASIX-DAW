<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 3</title>   
        <h1>Exercici 3</h1>
    </head>
    <body>
        <?php
            for ($i = 0; $i < 231; $i++) {
                if (($i%50 == 0) && ($i != 0)) {
                    echo "--------------------------------------------------<br>";
                } else if (($i%10 == 0) && ($i != 0)) {
                    echo ".......................................................<br>";
                } else if (($i%5 == 0) && ($i != 0)) {
                    echo "<br>";
                }
                echo "Estic aprenent a programar en PHP<br>";
            }
        ?>
    </body>
</html>
