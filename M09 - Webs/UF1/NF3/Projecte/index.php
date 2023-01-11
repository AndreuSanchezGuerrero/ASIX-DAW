<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>El temps</title>
    </head>
    <div id="menu">
            <ul>
                <?php
                include 'conectar.php';
                $conn = connectar();
                $sql = "SELECT MAX(temp) AS max, MIN(temp) AS min FROM meteo";
                $result = $conn->query($sql);
                if ($result->rowCount() > 0) {
                    while($row = $result->fetch()) {
                        echo "<li id='esq' id='temps'><img src='imatges/calendar.png' width='30' height='30'> T.màx: " . sprintf("%.1f", $row["max"]). "ºC</li>";
                        echo "<li id='esq' id='temps'><img src='imatges/maxmin.png' width='30' height='30'> T.mín: " . sprintf("%.1f", $row["min"]). "ºC</li>";
                    }
                } else {
                    echo "0 results";
                }
                tancar($conn);
                ?>
                <?php
                $sql = "SELECT * FROM meteo ORDER BY id DESC LIMIT 1";
                $result = $conn->query($sql);
                if ($result->rowCount() > 0) {
                    while($row = $result->fetch()) {
                        echo "<li id='dreta' id='temps'><img src='imatges/temp.png' width='30' height='30'> " . $row["temp"]. "ºC</li>";
                        echo "<li id='dreta' id='temps'><img src='imatges/humitat.png' width='30' height='30'> " . $row["humidity"]. "%</li>";
                        echo "<li id='dreta' id='temps'><img src='imatges/precipitacio.png' width='30' height='30'> " . $row["precip"]. "mm</li>";
                        echo "<li id='dreta' id='temps'><img src='imatges/vent.png' width='30' height='30'> " . $row["windspeed"]. "km/h</li>";
                        echo "<li id='dreta' id='temps'><img src='imatges/direccio.png' width='30' height='30'> " . $row["winddir"]. "º</li>";
                    }
                } else {
                    echo "0 results";
                }
                tancar($conn);
            ?>
            </ul>
        </div>
    <body>
        <h1>Temps actual</h1>
        <?php
            include 'grafics.php';
        ?>
        <img src="imatges/grafics/temperatura.png" alt="Temperatura">
        <img src="imatges/grafics/humitat.png" alt="Humitat">
        <img src="imatges/grafics/precipitacio.png" alt="Precipitacio">
        <img src="imatges/grafics/velocitat.png" alt="Vent">
    </body>
    <script>
    setInterval(function(){
        location.reload();
    }, 10000);
    </script>
</html>