<DOCTYPE html>
<html>
    <head>
        <meta charset=UTF-8>
        <link rel=stylesheet type=text/css href=CSS.css>
        <h1>Exercici 2</h1>
        <title>Exercisi 2</title>
    </head>
    <body>
    <table>
        <tr class="r">
            <th class="r">Iteració</th>
            <th class="r">Temps For</th>
            <th class="r">Temps While</th>
        </tr>
    <table>
        <?php
            $tempsFor = 0;
            $tempsWhile = 0;
            $tempsForMin = 1000;
            $tempsWhileMin = 1000;
            $tempsForMax = 0;
            $tempsWhileMax = 0;
            $tempsForMitjana = 0;
            $tempsWhileMitjana = 0;
            for ($i = 0; $i < 20; $i++) {
                $tempsFor = microtime(true);
                for ($j = 0; $j < 2**22; $j++) {
                    $j = $j;
                }
                $tempsFor = microtime(true) - $tempsFor;
                if ($tempsFor < $tempsForMin) {
                    $tempsForMin = $tempsFor;
                }
                if ($tempsFor > $tempsForMax) {
                    $tempsForMax = $tempsFor;
                }
                $tempsForMitjana += $tempsFor;
                $tempsWhile = microtime(true);
                $j = 0;
                while ($j < 2**22) {
                    $j = $j;
                    $j++;
                }
                $tempsWhile = microtime(true) - $tempsWhile;
                if ($tempsWhile < $tempsWhileMin) {
                    $tempsWhileMin = $tempsWhile;
                }
                if ($tempsWhile > $tempsWhileMax) {
                    $tempsWhileMax = $tempsWhile;
                }
                $tempsWhileMitjana += $tempsWhile;
                #Taula amb els resultats de cada iteració
                echo "<table>
                        <tr>
                            <td>$i</td>
                            <td>$tempsFor</td>
                            <td>$tempsWhile</td>
                        </tr>
                    </table>";
            }
            $tempsForMitjana /= 20;
            $tempsWhileMitjana /= 20;
            $diferencia = $tempsForMitjana - $tempsWhileMitjana;
            echo "<br>";
            echo "<table>
                    <tr>
                        <th></th>
                        <th>For</th>
                        <th>While</th>
                    </tr>
                    <tr>
                        <td>Temps mínim</td>
                        <td>$tempsForMin</td>
                        <td>$tempsWhileMin</td>
                    </tr>
                    <tr>
                        <td>Temps màxim</td>
                        <td>$tempsForMax</td>
                        <td>$tempsWhileMax</td>
                    </tr>
                    <tr>
                        <td>Temps mitjà</td>
                        <td>$tempsForMitjana</td>
                        <td>$tempsWhileMitjana</td>
                    </tr>
                </table><br><br>";
            if ($tempsForMitjana < $tempsWhileMitjana) {
                echo "El guanyador és el for amb una diferencia de $diferencia";
            } else {
                echo "El guanyador és el while amb una diferencia de $diferencia";  
            }
        ?>
    </body>
</html>
