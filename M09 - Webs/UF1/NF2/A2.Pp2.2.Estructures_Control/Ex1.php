<DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 1</title>   
        <h1>Exercici 1</h1>
    </head>
    <article class="wrapper">
    <body>
        <?php
            $v31 = 31;
            $es_divisible = ($v31%3) == 0;
            if ($es_divisible) {
                echo "El número $v31 és divisible per 3";
            } else {
                echo "El número $v31 no és divisible per 3";
            }
        ?>
    </body>
</html>