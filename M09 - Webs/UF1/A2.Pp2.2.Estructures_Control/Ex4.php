<DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 4</title>   
        <h1>Exercici 4</h1>
    </head>
    <body>
        <?php
            $x = 2;
            $y = 10;
            for ($i = 0; $i < $x; $i++) {
                for ($j = 0; $j < $y; $j++) {
                    echo "<div class='circle'></div>";
                }
                echo "<br>";
            }
        ?>
    </body>
</html>