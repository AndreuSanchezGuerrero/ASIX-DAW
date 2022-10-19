<DOCTYPE html>
<html>
    <head>
        <meta charset=UTF-8>
        <link rel=stylesheet type=text/css href=CSS.css>
        <title>Exercici 1</title>
        <h1>Exercici 4</h1>
        <title>Exercisi 4</title>
    </head>
    <body>
        <?php
            $cotxe = array(
                "Marca" => array("Seat", "Renault", "Fiat"),
                "Model" => array("Ibiza", "Megane", "Punto"),
                "Any" => array(2010, 2011, 2012),
                "Versions" => array("1.4", "1.6", "1.8")
                );
            echo "<table>";
            echo "<tr>";
            echo "<th>Marca</th>";
            echo "<th>Model</th>";
            echo "<th>Any</th>";
            echo "<th>Versions</th>";
            echo "</tr>";
            for ($i = 0; $i < count($cotxe["Marca"]); $i++) {
                echo "<tr>";
                echo "<td>" . $cotxe["Marca"][$i] . "</td>";
                echo "<td>" . $cotxe["Model"][$i] . "</td>";
                echo "<td>" . $cotxe["Any"][$i] . "</td>";
                echo "<td>";
                $versions = rand(1, 3);
                for ($j = 0; $j < $versions; $j++) {
                    echo $cotxe["Versions"][$j] . " ";
                }
                echo "</td>";
                echo "</tr>";
            }
            echo "</table>";
        ?>
    </body>
</html>
