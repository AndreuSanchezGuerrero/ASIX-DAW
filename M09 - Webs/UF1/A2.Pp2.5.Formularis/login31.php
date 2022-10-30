    <!-- Crea una pàgina senzilla amb html de nom loginXX.html que contingui un formulari on es demani el nom, el XX i un password (així com el botó d'enviament), de tal manera que quan li fem un clic, la informació s'envia a una pàgina loginXX.php que mostra el nom i la XX en color blau i amb tipus títol (H2) i el password subratllat amb mida lletra 16. És valorarà la utilització de funcions en la resolució de l’exercici i la utilització d’estils en arxiu CSS. (2.0p).-->
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" type="text/css" href="CSS.css">
            <title>Exercici 1</title>
        </head>
        <body>
            <h1>Exercici 1</h1>
            <?php
            $nom = $_POST['nom'];
            $XX = $_POST['XX'];
            $password = $_POST['password'];
            echo "<h2>El teu nom és $nom</h2>";
            echo "<h2>El teu XX és $XX</h2>";
            echo "<h2 class=psw>El teu password és $password</h2>";
            ?>
        </body>
    </html>
