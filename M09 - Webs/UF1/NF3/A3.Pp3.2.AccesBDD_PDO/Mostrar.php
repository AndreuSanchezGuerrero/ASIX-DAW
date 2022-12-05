<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Incidencies</title>
    </head>
    <body>
        <h1>Incidencies</h1>
        <?php 
        include 'Connectar.php';
        #Fem una funció per a mostrar totes les incidencies amb els seus respectius botons per a modificar o eliminar
        function mostrar(){
            $conn = connectar();
            $sql = "SELECT * FROM incidencies";
            $result = $conn->query($sql);
            if ($result->rowCount() > 0) {
                echo "<table><tr><th>ID</th><th>Dispositiu</th><th>Data</th><th>Solicitat</th><th>Correu</th><th>Descripció</th></tr>";
                while($row = $result->fetch()) {
                    echo "<tr><td>" . $row["id"]. "</td><td>" . $row["dispositiu"]. "</td><td>" . $row["data"]. "</td><td>" . $row["solicitat"]. "</td><td>" . $row["correu"]. "</td><td>" . $row["descripcio"]. "</td><td><a href='Modificar.php?id=".$row["id"]."'><img src='Modificar.png' width='20px' height='20px'></a></td><td><a href='Eliminar.php?id=".$row["id"]."'><img src='Eliminar.png' width='20px' height='20px'></a></td></tr>";
                }
                echo "</table>";
            } else {
                echo "0 results";
            }
            tancar($conn);
        }
        mostrar();
        ?>
        <a href="index.php" class="t"><button>Tornar</button></a>
    </body>
</html>








