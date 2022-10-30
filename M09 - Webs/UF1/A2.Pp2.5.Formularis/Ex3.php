<!-- Crea un formulari que ens serveixi per omplir els diferents camps necessaris per la gestió d’incidències informàtiques, de tal manera que quan l’enviem arribem a la pàgina on se’ns ha d’omplir un array amb els valors omplerts al formulari. Ara cal que aquest es mostri per pantalla (es valorarà la utilització de funcions en la resolució proposta així com la utilització d’estils en arxiu CSS)... (4.0p)-->
<!-- 	Id: (enter) 
		Dispositiu: (string)
        Data: (string)-> Date() 
		Sol·licitat (String)
		Correu Sol·licitant (String)
		Descripció de la incidència-->

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 3</title>
        <title>Exercisi 3</title>
    </head>
    <body>
        <h1>Exercici 3</h1>
        <?php
        $id = $_POST['id'];
        $dispositiu = $_POST['dispositiu'];
        $data = $_POST['data'];
        $solicitat = $_POST['solicitat'];
        $correu = $_POST['correu'];
        $descripcio = $_POST['descripcio'];
        $array = array($id, $dispositiu, $data, $solicitat, $correu, $descripcio);
        echo "<table>";
        echo "<tr><th>Id</th><th>Dispositiu</th><th>Data</th><th>Sol·licitat</th><th>Correu</th><th>Descripció</th></tr>";
        echo "<tr><td>$id</td><td>$dispositiu</td><td>$data</td><td>$solicitat</td><td>$correu</td><td>$descripcio</td></tr>";
        echo "</table>";
        ?>
    </body>
</html>

