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
            #No cal comprovar si la incidencia existeix ja que si a la pagina anterior apareix el boto de modificar es que existeix
            include 'Connectar.php';
            #Fem una funció per a modificar la incidencia
            function modificar(){
                #Declarem les variables
                $id = $_POST['id'];
                $dspositiu = $_POST['dispositiu'];
                $solicitat = $_POST['solicitat'];
                $correu = $_POST['correu'];
                #Comprovem que els camps no estigui buits
                if($id != "" && $dspositiu != "" && $solicitat != "" && $correu != ""){
                    $conn = connectar();
                    $sql = "UPDATE incidencies SET dispositiu = '$dspositiu', solicitat = '$solicitat', correu = '$correu' WHERE id = '$id'";
                    $conn->exec($sql);
                    tancar($conn);
                    echo "<p>La incidencia s'ha modificat correctament</p>";
                    header("refresh:3; url= Mostrar.php");
                }else{
                    echo "<p>Has d'omplir tots els camps</p>";
                    header("refresh:3; url= Modificar.php?id=".$id);
                }
            }
            #Si s'ha premut el botó de modificar la modifiquem sino mostrem el formulari
            if(isset($_POST["modificar"])){
                modificar();
            } else {
                #Obrim un formulari per a modificar les dades de la incidencia
                echo "<form action='Modificar.php' method='post'>";
                #Agafem les dades de la incidencia que volem modificar
                $id = $_GET['id'];
                $sql = "SELECT * FROM incidencies WHERE id = $id";
                $conn = connectar();
                $result = $conn->query($sql);
                #Mostrem les dades de la incidencia
                while($row = $result->fetch()) {
                    #Aquesta part crec que m'he complicat molt pero funciona com vull
                    echo "<label for='id'>Id:</label>";
                    echo "<input type='number' name='id' id='id' value='".$row["id"]."' readonly><br>";
                    echo "<label for='dispositiu'>Dispositiu:</label>";
                    echo "<select name='dispositiu' id='dispositiu'>";
                    echo "<option value='Ordenador' ".($row["dispositiu"] == "Ordenador" ? "selected" : "").">Ordenador</option>";
                    echo "<option value='Impressora' ".($row["dispositiu"] == "Impressora" ? "selected" : "").">Impressora</option>";
                    echo "<option value='Monitor' ".($row["dispositiu"] == "Monitor" ? "selected" : "").">Monitor</option>";
                    echo "<option value='Portàtil' ".($row["dispositiu"] == "Portàtil" ? "selected" : "").">Portàtil</option>";
                    echo "<option value='Escàner' ".($row["dispositiu"] == "Escàner" ? "selected" : "").">Escàner</option>";
                    echo "<option value='Teclat' ".($row["dispositiu"] == "Teclat" ? "selected" : "").">Teclat</option>";
                    echo "<option value='Servidor' ".($row["dispositiu"] == "Servidor" ? "selected" : "").">Servidor</option>";
                    echo "<option value='Router' ".($row["dispositiu"] == "Router" ? "selected" : "").">Router</option>";
                    echo "<option value='Switch' ".($row["dispositiu"] == "Switch" ? "selected" : "").">Switch</option>";
                    echo "</select><br>";
                    echo "<label for='data'>Data:</label>";
                    echo "<input type='date' name='data' id='data' value='".$row["data"]."' readonly><br>";
                    echo "<label for='solicitat'>Sol·licitat:</label>";
                    echo "<input type='text' name='solicitat' id='solicitat' value='".$row["solicitat"]."'><br>";
                    echo "<label for='correu'>Correu Sol·licitant:</label>";
                    echo "<input type='email' name='correu' id='correu' value='".$row["correu"]."'><br>";
                    echo "<label for='descripcio'>Descripció:</label>";
                    echo "<textarea name='descripcio' id='descripcio' rows='4' cols='50' readonly>".$row["descripcio"]."</textarea><br>";
                    }
                tancar($conn);
                echo "<input type='submit' name='modificar' value='Modificar'>";
                echo "</form>";
            }
        ?>
        <a href="Mostrar.php" class="t"><button>Tornar</button></a>
    </body>
</html>