<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Incidencies</title>
    </head>
    <body>
        <h1>Incidencies</h1>
        <form action="" method="post">
            <label for="id">Id:</label>
            <input type="number" name="id" id="id"><br>
            <label for="dispositiu">Dispositiu:</label>
            <select name="dispositiu" id="dispositiu">
                <option value="Ordenador">Ordenador</option>
                <option value="Impressora">Impressora</option>
                <option value="Monitor">Monitor</option>
                <option value="Portàtil">Portàtil</option>
                <option value="Escàner">EScaner</option>
                <option value="Teclat">Teclat</option>
                <option value="Servidor">Servidor</option>
                <option value="Router">Router</option>
                <option value="Switch">Switch</option>
            </select><br>
            <label for="data">Data:</label>
            <input type="date" name="data" id="data"><br>
            <label for="solicitat">Sol·licitat:</label>
            <input type="text" name="solicitat" id="solicitat"><br>
            <label for="correu">Correu Sol·licitant:</label>
            <input type="email" name="correu" id="correu"><br>
            <label for="descripcio">Descripció de la incidència:</label>
            <textarea name="descripcio" id="descripcio" cols="30" rows="10"></textarea><br>
            <button type="submit" name="afegir" value="afegir" formaction="index.php">Afegir</button>
            <button type="submit" name="mostrar" value="Mostrar" formaction="Mostrar.php">Mostrar</button>
        </form>
        <?php
            #Si s'ha premut el boto afegir, afegim la incidencia a la base de dades
            if(isset($_POST['afegir'])){
                #Importem la funcio per a connectar de l'arxiu Connectar.php
                include 'Connectar.php';
                $conn = connectar();
                $id = $_POST['id'];
                $dispositiu = $_POST['dispositiu'];
                $data = $_POST['data'];
                $solicitat = $_POST['solicitat'];
                $correu = $_POST['correu'];
                $descripcio = $_POST['descripcio'];
                #Comprovem que no hi hagi cap camp buit ni que la incidencia ja existeixi
                if($id != "" && $dispositiu != "" && $data != "" && $solicitat != "" && $correu != "" && $descripcio != ""){
                    $sql = "SELECT * FROM incidencies WHERE id = $id";
                    $resultat = $conn->query($sql);
                    if($resultat->rowCount() == 0){
                        $sql = "INSERT INTO incidencies VALUES ($id, '$dispositiu', '$data', '$solicitat', '$correu', '$descripcio')";
                        $resultat = $conn->query($sql);
                        echo "<p>Incidència afegida correctament</p>";
                    }else{
                        echo "<p>L'incidència ja existeix</p>";
                    }
                }else{
                    echo "<p>Hi ha camps buits</p>";
                }
                tancar($conn);
            }
        ?>
    </body>
</html>
