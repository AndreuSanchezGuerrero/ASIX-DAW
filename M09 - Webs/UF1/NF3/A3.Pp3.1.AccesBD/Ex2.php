<!--Exercici 2 – Canvia la pàgina del formulari que es fa implementar en l’activitat corresponent per tal de poder afegir incidències a aquesta bases de dades. Decideix tu com a analista programador de l’aplicació com decidim si una incidència ja està entrada a la base de dades, si això passa no s’hi afegirà, es valorarà com aquest fet s’adverteix-hi a l’usuari així com la imprescindible utilització de funcions (s’ha de fer servir un fitxer de connexió tal i com es mostra a les captures). (6.5p)
-->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 2</title>
    </head>
    <body>
        <h1>Exercici 2</h1>
        <form action="Ex2-3.php" method="post">
            <label for="id">Id:</label>
            <input type="number" name="id" id="id"><br>
            <label for="dispositiu">Dispositiu:</label>
            <select name="dispositiu" id="dispositiu">
                <option value="Ordenador">Ordenador</option>
                <option value="Impressora">Impressora</option>
                <option value="Monitor">Monitor</option>
                <option value="Portàtil">Portàtil</option>
                <option value="EScaner">EScaner</option>
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
            <input type="submit" name="enviar" value="Enviar">
            #Fem q en fer clic a enviar afeguixi a la base de dades i torni a la pàgina principal
            <?php
                
            <input type="submit" name="mostrar" value="Mostrar">
            </form>
    </body>
</html>
