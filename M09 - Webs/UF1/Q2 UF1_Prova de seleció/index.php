<!--Demo de una app web que usa PHP per a practicar la taula del 6 i del 7.
Concideracions:
Tenim varis usuaris en banejats enmagatzemats en un .txt separats per;
Pagines a fer:
Pagina de conexio a la base de dades
Pagina de login per entrar a la app
Pagina amb la app  la cual nomes s'ha de poder entrar si l'usuari esta validat
Pagina amb el css

Fem el fitxer de login-->

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Login</title>
    </head>
    <body>
        <div class="login">
            <h1>Login</h1>
            <form action="index.php" method="post">
                <input type="text" name="usuari" placeholder="usuariname" required="required" />
                <input type="password" name="pass" placeholder="Password" required="required" />
                <button type="submit" class="btn btn-primary btn-block btn-large">Let me in.</button>
            </form>
        </div>
        <?php
            if (isset($_POST["usuari"]) && isset($_POST["pass"])) {
                $usuari = $_POST["usuari"];
                $pass = $_POST["pass"];
                $file = fopen("ban.txt", "r");
                $ban = fread($file, filesize("ban.txt"));
                $ban = explode(";", $ban);
                if (in_array($usuari, $ban)) {
                    echo "You are banned, you can't enter the app.";
                } else {
                    setcookie("usuari", $usuari, time() + 3600);
                    header("Location: app.php");
                }
            }
        ?>
    </body>
</html>

