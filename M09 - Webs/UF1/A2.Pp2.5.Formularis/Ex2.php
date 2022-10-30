    <!-- Crea un formulari que et permeti generar amb dades entrades per l’usuari l’estructura de l’exercici 4 Pp2.2 (la matriu de cercles), segons les files i columnes que s’especifiquin (s’ha de validar que s’han omplert els dos valors, que són nombres i que són > que zero). És valorarà la utilització de funcions en la resolució de l’exercici i la utilització d’estils en arxiu CSS. (3.5p).-->
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" type="text/css" href="CSS.css">
            <title>Exercici 2</title>
            <title>Exercisi 2</title>
        </head>
        <body>
            <h1>Exercici 2</h1>
            <?php
            $files = $_POST['files'];
            $columnes = $_POST['columnes'];
            if ($files > 0 && $columnes > 0) {
                echo "<table>";
                for ($i = 0; $i < $files; $i++) {
                    echo "<tr>";
                    for ($j = 0; $j < $columnes; $j++) {
                        echo "<td><div class='circle'></div></td>";
                    }
                    echo "</tr>";
                }
                echo "</table>";
            } else {
                echo "<h2>Has d'introduir un número major que 0</h2>";
            }
            ?>
        </body>
    </html>
