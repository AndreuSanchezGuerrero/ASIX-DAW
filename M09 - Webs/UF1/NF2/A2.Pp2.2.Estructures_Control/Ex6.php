<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 6</title>   
        <h1>Exercici 6</h1>
    </head>
    <body>
        <?php
            for ($i = 0; $i < 3; $i++) {
                $random1 = rand(0,2);
                $random2 = rand(0,2);
                echo "Jugador 1: ";
                if ($random1 == 0) {
                    echo "Pedra";
                } else if ($random1 == 1) {
                    echo "Paper";
                } else if ($random1 == 2) {
                    echo "Tisora";
                }
                echo "<br>";
                echo "Jugador 2: ";
                if ($random2 == 0) {
                    echo "Pedra";
                } else if ($random2 == 1) {
                    echo "Paper";
                } else if ($random2 == 2) {
                    echo "Tisora";
                }
                echo "<br>";
                if ($random1 == $random2) {
                    echo "Empat";
                } else if ($random1 == 0 && $random2 == 1) {
                    echo "Guanya jugador 2";
                } else if ($random1 == 0 && $random2 == 2) {
                    echo "Guanya jugador 1";
                } else if ($random1 == 1 && $random2 == 0) {
                    echo "Guanya jugador 1";
                } else if ($random1 == 1 && $random2 == 2) {
                    echo "Guanya jugador 2";
                } else if ($random1 == 2 && $random2 == 0) {
                    echo "Guanya jugador 2";
                } else if ($random1 == 2 && $random2 == 1) {
                    echo "Guanya jugador 1";
                }
                echo "<br>";
                echo "<br>";
            }
        ?>
    </body>