
<!--Demo de una app web que usa PHP per a practicar la taula del 6 i del 7.
Concideracions:
Tenim varis usuaris en banejats enmagatzemats en un .txt separats per;
Pagines a fer:
Pagina de conexio a la base de dades
Pagina de login per entrar a la app
Pagina amb la app  la cual nomes s'ha de poder entrar si l'usuari esta validat
Pagina amb el css

Fem el fitxer de la app:
1. Verifiquem la cookie per veure si l'usuari esta validat
    Si no ho esta, redirigeix a la pagina de login
    Si ho esta, mostra la app web 
2. Primer validem si l'usuari esta a la base de dades, si no ho esta l'afeim amb la puntuacó  del seu record a 0
3. Mostrem un menu per selecionar si vol jugar o veure el record global de la app web -->

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>App</title>
    </head>
    <body>
        <?php
            if (!isset($_COOKIE["usuari"]) || isset($_POST["logout"]) || $_COOKIE["usuari"] == "") {
                setcookie("usuari", "", time() - 3600);
                header("Location: index.php");
            } 
            include "connectar.php";

            $usuari = $_COOKIE["usuari"];
            $conn = connectar();
            $sql = "SELECT * FROM records WHERE usuari = '$usuari'";
            $result = $conn->query($sql); 
            if ($result->rowCount() > 0) {
                $sql = "INSERT INTO records (usuari, record) VALUES ('$usuari', 0)";
                $conn->query($sql);
            }
            #Mostrem missatge de welcome i la puntuacio del record de l'usuari
            $sql = "SELECT record FROM records WHERE usuari = '$usuari'";
            $result = $conn->query($sql);
            $row = $result->fetch();
            $record = $row["record"];
            if ($record == 0) {
                $record = "0";
            }
            echo "Welcome, $usuari <br> Your record is $record"; 
        ?>
        <br>
        <br>
        <form action="app.php" method="post">
            <input type="submit" name="play" value="Play" formaction="play.php">
            <input type="submit" name="record" value="Records Globals" formaction="record.php">
        </form>
        <br>
        <br>
        <form action="index.php" method="post">
            <input type="submit" name="logout" value="Logout">
        </form>
    </body>
</html>