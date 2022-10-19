<DOCTYPE html>
<html>
    <head>
        <meta charset=UTF-8>
        <link rel=stylesheet type=text/css href=CSS.css>
        <title>Exercici 1</title>
        <h1>Exercici 3</h1>
        <title>Exercisi 3</title>
    </head>
    <body>
        <?php
            $mesosdeAny = array("Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre");
            echo "Els mesos de l'any són: " . $mesosdeAny[0] . ", " . $mesosdeAny[1] . ", " . $mesosdeAny[2] . ", " . $mesosdeAny[3] . ", " . $mesosdeAny[4] . ", " . $mesosdeAny[5] . ", " . $mesosdeAny[6] . ", " . $mesosdeAny[7] . ", " . $mesosdeAny[8] . ", " . $mesosdeAny[9] . ", " . $mesosdeAny[10] . ", " . $mesosdeAny[11] . ". Està formada per: " . count($mesosdeAny) . " mesos.";
            sort($mesosdeAny);
            echo "<br><br>Els mesos de l'any ordenats alfabèticament són: <br>";
            foreach ($mesosdeAny as $mes) {
                echo $mes . "<br>";
            }
        ?>
    </body>
</html>
