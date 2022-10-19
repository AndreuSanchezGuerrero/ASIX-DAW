<DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 2</title>   
        <h1>Exercici 2</h1>
    </head>
    <body>
        <ul>
            <?php
                for ($i = 31; $i < 31+600; $i++) {
                    $es_divisible = ($i%3) == 0;
                    if ($es_divisible) {
                        echo "<li><span style='color: green;'>El número $i és divisible per 3</span></li>";
                    } else {
                        echo "<li><span style='color: red;'>El número $i no és divisible per 3</span></li>";
                    }
                }
            ?>
        </ul>
    </body>
</html>
