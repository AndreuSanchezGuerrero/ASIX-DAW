<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 5</title>   
        <h1>Exercici 5</h1>
    </head>
    <body>
        <?php
            $random = rand(0,3);
            echo $random;
            echo "<br>";
            echo "<br>";
            if ($random == 0) {
                echo "<svg height='100' width='100'>
                    <circle cx='50' cy='50' r='40' fill='white' />
                </svg>";
            } else if ($random == 3) {
                echo "<svg height='100' width='100'>
                    <polygon points='50,0 100,100 0,100' fill='white' />
                </svg>";
            }
        ?>
    </body>
</html>
